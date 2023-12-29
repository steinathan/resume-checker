export interface AllBaseModel {
  id?: string | null;
  created_at: string;
  updated_at: string;
}

export interface ResumeSection {
  issues: string[];
  improvements: string[];
  done: string[];
  score: number;
}

export interface ResumeLLMAnalysis {
  sections_count: number;
  total_score: number;
  total_issues: number;
  total_improvements: number;
  total_done: number;

  contact_info: ResumeSection;
  education: ResumeSection;
  experience: ResumeSection;
  skills: ResumeSection;
  summary: ResumeSection;
  personal_projects: ResumeSection;
  date_formatting: ResumeSection;
  section_headings: ResumeSection;
}

export interface Resume extends AllBaseModel {
  user_id: string;
  src: string;
  name: string;
  text?: string | null;
  analysis?: ResumeLLMAnalysis | null;
}

// TODO: refactor

export interface ATSAnalysisSection {
  values: string[];
  explanation: string;
  issues: string[];
  suggestion: string;
  score: number;
}

export interface SkillsAnalysis {
  ats_skills: Array<{
    skill_id: string;
    name: string;
    is_match: boolean;
  }>;
}

export interface ATSAnalysis {
  education: ATSAnalysisSection;
  // met_skills: ATSAnalysisSection;
  // unmet_skills: ATSAnalysisSection;
  // resume_skills: ATSAnalysisSection;
  avoidable_keywords: ATSAnalysisSection;
  score: number;
  explanation: string;
  job_title: string;
  company_name: string;
  skills_analysis: SkillsAnalysis;
}

export interface ATSAnalysisJobData {
  id: string;
  created_at: string;
  updated_at: string;
  user_id: string;
  resume_id: string;
  cover_letter_id: string;
  job_url: string;
  job_description: string;
  ats_analysis: ATSAnalysis;
}
