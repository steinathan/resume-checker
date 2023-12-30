import { computed, ref } from "vue";
import { defineStore } from "pinia";
import type {
  ATSAnalysisJobData,
  Resume,
  ResumeLLMAnalysis,
} from "../../types";
import { get } from "@/core/services/ApiService2";

export const useResumeStore = defineStore("resume", () => {
  const singleScan = ref<ATSAnalysisJobData>({} as ATSAnalysisJobData);
  const resume = ref<Resume>({} as Resume);
  const resumes = ref<Resume[]>([]);
  const jobScans = ref<ATSAnalysisJobData[]>([]);

  function setResume(r: Resume) {
    resume.value = r;
  }
  function setJobScan(s: ATSAnalysisJobData) {
    singleScan.value = s;
  }

  function setResumes(rs: Resume[]) {
    resumes.value = rs;
  }

  function setJobScans(scans: ATSAnalysisJobData[]) {
    jobScans.value = scans;
  }

  async function fetchResume(id) {
    const resume = await get<Resume>("/resumes/" + id, {});
    setResume(resume);
  }

  return {
    resume,
    resumes,
    jobScans,
    singleScan,
    setJobScan,
    setJobScans,
    setResumes,
    setResume,
    fetchResume,
  };
});
