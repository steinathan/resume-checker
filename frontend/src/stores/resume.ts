import { computed, ref } from "vue";
import { defineStore } from "pinia";
import type { JobScan, Resume, ResumeLLMAnalysis } from "../../types";
import { get } from "@/core/services/ApiService2";

export const useResumeStore = defineStore("resume", () => {
  const singleScan = ref<JobScan>({} as JobScan);
  const resume = ref<Resume>({} as Resume);

  const coverLetter = ref<any>({});

  const resumes = ref<Resume[]>([]);
  const jobScans = ref<JobScan[]>([]);

  function setResume(r: Resume) {
    resume.value = r;
  }
  function setJobScan(s: JobScan) {
    singleScan.value = s;
  }

  function setResumes(rs: Resume[]) {
    resumes.value = rs;
  }

  function setJobScans(scans: JobScan[]) {
    jobScans.value = scans;
  }
  function setCoverLetter(obj: any) {
    coverLetter.value = obj;
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
    coverLetter,
    setCoverLetter,
    setJobScan,
    setJobScans,
    setResumes,
    setResume,
    fetchResume,
  };
});
