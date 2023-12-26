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
