from __future__ import annotations

import os

import requests
import json
from typing import List, Any, Dict
from pydantic import Field, BaseModel
from datetime import datetime, timedelta

CLIENT_ID = os.environ.get("LIGHTCAST_CLIENT_ID")
CLIENT_SECRET = os.environ.get("LIGHTCAST_CLIENT_SECRET")


class APISkill(BaseModel):
    skill_id: str = Field(description="the id of the skill found")
    name: str = Field(description="the value of the skill found")
    # description: str = Field(description="the description of the skill found")


class AtsSkill(APISkill):
    is_match: bool = Field(description="job skill is match from resume")


class MatchingResult(BaseModel):
    ats_skills: List[AtsSkill] = Field(
        description="List of re-shaped skills matching from job")
    resume_skills: List[APISkill] = Field(
        description="List of skills found in the resume")


# noinspection PyMethodMayBeStatic
class SkillExtractor:
    resume_skills: List[APISkill] = []
    job_skills: List[APISkill] = []
    bearer: str | None = None

    def __init__(self, resume_skills: List[APISkill] | None = None):
        self.access_token_info = self.get_access_token_info()
        self.resume_skills = resume_skills or []

    def get_access_token_info(self):
        """ normalizes the access token info
        Returns:
            Dict[str, str]: normalized access token info
        """

        access_token_info = self.get_access_token()
        return {
            'access_token': access_token_info['access_token'],
            'expires_at': datetime.utcnow() + timedelta(seconds=access_token_info['expires_in']),
            'token_type': access_token_info['token_type'],
            'scope': access_token_info['scope']
        }

    def refresh_access_token(self):
        now = datetime.utcnow()
        expires_at = self.access_token_info['expires_at']

        # If the access token has expired or will expire in the next minute, refresh it
        if now >= expires_at - timedelta(minutes=1) or self.bearer is None:
            new_token_info = self.get_access_token_info()
            self.bearer = new_token_info['access_token']
            self.access_token_info = new_token_info

    def get_access_token(self):
        url = "https://auth.emsicloud.com/connect/token"
        payload = f"client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials&scope=emsi_open"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print("[SkillExtractor] got access token")
        return response.json()

    def get_skills(self, text: str) -> List[APISkill]:
        self.refresh_access_token()

        url = "https://emsiservices.com/skills/versions/latest/extract"
        querystring = {"language": "en"}
        data = {"text": text, "confidenceThreshold": 0.6}
        payload = json.dumps(data)
        headers = {
            'Authorization': f"Bearer {self.bearer}",
            'Content-Type': "application/json"
        }

        response = requests.request(
            "POST", url, data=payload, headers=headers, params=querystring)

        body = response.json()
        return self.from_api_skills(body)

    def from_api_skills(self, dataArr: Dict[str, List[Any]]) -> List[APISkill]:
        """ converts the result of the api call to something we can use """
        skills: List[APISkill] = []

        for data in dataArr["data"]:
            name = data["skill"]["name"]
            description = data["skill"]["description"]
            skill_id = data["skill"]["id"]
            skills.append(
                APISkill(skill_id=skill_id, name=name)
            )

        return skills

    def to_ats_skills(self, resume_skills: List[APISkill], job_skills: List[APISkill]) -> List["AtsSkill"]:
        skills = []

        for skill in job_skills:
            match = skill.skill_id in [s.skill_id for s in resume_skills]
            skills.append(
                AtsSkill(**skill.model_dump(), is_match=match))

        return skills

    def process_ats_skills(self, user_resume: str, job_description: str) -> MatchingResult:
        """ """
        self.resume_skills = self.get_skills(user_resume)
        self.job_skills = self.get_skills(job_description)

        skills = self.to_ats_skills(self.resume_skills, self.job_skills)

        # matched_skills = [skill for skill in skills if skill.is_match]
        # unmatched_skills = [skill for skill in skills if not skill.is_match]

        result = MatchingResult(
            ats_skills=skills,
            resume_skills=self.resume_skills,
        )

        return result
