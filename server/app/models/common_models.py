from __future__ import annotations
from datetime import datetime
from typing import ClassVar, Any, List

from pydantic import BaseModel, Field

from app.prompts.ats_job_prompt import AtsJobPromptModel
from app.prompts.resume_analysis_prompt import ResumeSection, ResumeAnalysisResult
from app.skill_extractor.skill_extractor import MatchingResult as SkillExtractorResult, APISkill


class AllBaseModel(BaseModel):
    id: str = ""
    # adding iso format for supabase purposes
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()
    deleted_at: str | None = None
    deleted: bool = False


class User(BaseModel):
    id: str
    email_address: str | None = None
    full_name: str | None = None
    disabled: bool | None = False

    # for free users, 3 scans per day
    scans_remaining: int = Field(3)
    scans_remaining_reached: bool = Field(False)

    resume_analysis_remaining: int = Field(3)
    resume_analysis_limit_reached: bool = Field(False)

    plan: str = Field("free")
    stripe_customer_id: str | None = None
    stripe_subscription_id: str | None = None
    stripe_subscription_status: str | None = None
    stripe_subscription_current_period_start: int | None = None
    stripe_subscription_current_period_end: int | None = None
    stripe_subscription_cancel_at_period_end: bool | None = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.stripe_customer_id:
            self.plan = "paid"
        self.scans_remaining_reached = self.scans_remaining <= 0
        self.resume_analysis_limit_reached = self.resume_analysis_remaining <= 0


class ResumeLLMAnalysis(ResumeAnalysisResult):
    """ ResumeLLMAnalysis is the analysis of the resume after being parsed into an LLM, processed after resume is
    uploaded"""
    sections_count: int = Field(
        description="number of sections analyzed", default=0)
    total_score: float = Field(
        description="Total score for the resume analysis", default=0.0)
    total_issues: int = Field(
        description="total number of issues for the resume analysis", default=0)
    total_improvements: int = Field(
        description="total number of improvements for the resume analysis", default=0)
    total_done: int = Field(
        description="total number of sections done for the resume analysis", default=0)

    class_values: ClassVar[Any] = None

    def __init__(self, **data):
        super().__init__(**data)
        ResumeLLMAnalysis.class_values = self.__dict__.values()
        self.sections_count += sum(isinstance(value, ResumeSection)
                                   for value in ResumeLLMAnalysis.class_values)
        self.calculate_scores()

    def calculate_scores(self) -> None:
        """ calculates scores for all individual sections"""
        total_score = 0.0
        class_values = self.__dict__.values()
        for section_value in class_values:
            if isinstance(section_value, ResumeSection):
                self.total_done += len(section_value.done)
                self.total_improvements += len(section_value.improvements)
                self.total_issues += len(section_value.issues)
                total_score += section_value.score
        rounded_score = round(total_score / self.sections_count,
                              1) if self.sections_count > 0 else 0.0
        self.total_score = float(rounded_score)


class Resume(AllBaseModel):
    user_id: str | None = None
    src: str
    name: str
    text: str | None = None
    skills: List[APISkill] | None = Field(default=[])
    analysis: ResumeLLMAnalysis | None = None


class CoverLetter(AllBaseModel):
    user_id: str | None = None
    resume_id: str | None = None
    scan_id: str | None = None
    text: str
    job_url: str | None = None
    # job_description: str | None = None


class AtsJobScan(AllBaseModel):
    user_id: str
    resume_id: str
    cover_letter_id: str | None = None
    job_url: str | None = Field(default="no url provided")
    job_description: str

    # analysis from LLM
    ats_analysis: AtsJobPromptModel | None = None

    # analysis from Skiller skills
    skills_analysis: SkillExtractorResult | None = None

    # skills score of matched vs unmatched skills
    skills_score: int | None = Field(0)
    job_skills_count: int | None = Field(0)

    def __init__(self, **data):
        super().__init__(**data)

        #  auto compute the matched and unmatched skills if they're empty
        if len(self.skills_analysis.matched_skills) == 0:
            self.skills_analysis.matched_skills = [skill for skill in self.skills_analysis.ats_skills if skill.is_match]
        if len(self.skills_analysis.unmatched_skills) == 0:
            self.skills_analysis.unmatched_skills = [skill for skill in self.skills_analysis.ats_skills if
                                                     not skill.is_match]

        if self.skills_analysis:
            match_count = len(self.skills_analysis.matched_skills)
            self.job_skills_count = len(self.skills_analysis.ats_skills)
            self.skills_score = round(match_count * self.job_skills_count / 10)
