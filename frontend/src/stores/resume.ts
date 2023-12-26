import { computed, ref } from "vue";
import { defineStore } from "pinia";
import type { Resume, ResumeLLMAnalysis } from "../../types";

export const useResumeStore = defineStore("resume", () => {
  const resume = ref<Resume>({} as Resume);
  const resumes = ref<Resume[]>([]);

  function setResume(r: Resume) {
    console.log(r);
    resume.value = r;
  }

  function setResumes(rs: Resume[]) {
    resumes.value = rs;
  }

  return {
    resume,
    resumes,
    setResumes,
    setResume,
  };
});
