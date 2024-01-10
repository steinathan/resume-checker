<template>
  <!--begin::Tables Widget 9-->

  <div class="fs-4 px-5">
    {{ singleScan.ats_analysis?.summary }}
  </div>

  <!--  Title match -->
  <ScanSection
    title="Job Title Match"
    :explanation="analysis?.title_match?.explanation"
    :checked="analysis?.title_match.match"
    :suggestion="analysis?.title_match?.suggestion"
  />

  <!--  <ScanSection-->
  <!--    title="Education Requirement"-->
  <!--    :explanation="analysis?.education.explanation"-->
  <!--    :issues="analysis?.education.issues"-->
  <!--    :score="analysis?.education.score"-->
  <!--    :suggestion="analysis?.education?.suggestion"-->
  <!--    hide-checked-->
  <!--  />-->

  <ScanSection
    title="Avoidable Keywords"
    :explanation="analysis?.avoidable_keywords.explanation"
    :issues="analysis?.avoidable_keywords.issues"
    :score="analysis?.avoidable_keywords.score"
    :suggestion="analysis?.avoidable_keywords?.suggestion"
    hide-checked
  />

  <!--  Skill comparison-->
  <div class="py-2">
    <Notice
      classes="rounded-3"
      color="info"
      title="Tip"
      body="Match the skills in your resume to the exact spelling in the job description. Prioritize skills that appear most frequently in the job description."
    ></Notice>
  </div>

  <div class="mb-5 mb-xl-8 card my-10">
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Skills Comparison</span
        ><span class="text-muted mt-1 fw-semibold fs-7">
          Skills we found from the job description that may or may not be an
          exact match in your resume
        </span>
      </h3>
    </div>
    <div class="card-body pt-3">
      <div class="table-responsive">
        <table
          class="table table-row-dashed table-row-gray-300 align-middle gs-0 gy-4"
        >
          <thead>
            <tr class="border-0 fw-bold text-muted">
              <!--              <th class="">ID</th>-->
              <th class="">Name</th>
              <th class="text-center">Job Match</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="skill in sortSkills(skillAnalysis.ats_skills)"
              :key="skill.skill_id"
            >
              <!--              <td>-->
              <!--                <span-->
              <!--                  class="text-muted fw-bold text-hover-primary d-block mb-1 fs-6"-->
              <!--                  >{{ skill.skill_id }}</span-->
              <!--                >-->
              <!--              </td>-->
              <td>
                <span
                  class="text-gray-900 fw-bold text-hover-primary d-block mb-1 fs-6"
                  >{{ skill.name }}</span
                >
              </td>
              <td class="text-center">
                <span v-if="skill.is_match">
                  <i class="fas fa-check-circle text-success fs-2"></i>
                </span>
                <span v-else>
                  <i class="fas fa-xmark-circle text-danger fs-4"></i>
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- end comparison -->
</template>

<script lang="ts" setup>
import { get } from "@/core/services/ApiService2";
import { computed, onMounted, ref, watchEffect } from "vue";
import type {
  ATSAnalysis,
  ATSAnalysisSection,
  AtsSkill,
  Resume,
  ResumeLLMAnalysis,
  ResumeSection,
  SkillsAnalysis,
} from "../../../types";
import { useRoute } from "vue-router";
import { useResumeStore } from "@/stores/resume";
import { storeToRefs } from "pinia";
import _ from "lodash";
import Notice from "@/components/Notice.vue";
import ScanSection from "@/components/jobScan/ScanSection.vue";
import Swal from "sweetalert2";

type rev = {
  heading: string;
  section: ATSAnalysisSection;
};
const items = ref<rev[]>([]);
const resumeStore = useResumeStore();

const { singleScan } = storeToRefs(resumeStore);
const analysis = computed<ATSAnalysis>(() => {
  return singleScan.value.ats_analysis;
});

const skillAnalysis = computed<SkillsAnalysis>(() => {
  return singleScan.value?.skills_analysis || {};
});

const skillsCount = computed<Record<string, any>>(() => {
  const atsSkills = singleScan.value?.skills_analysis?.ats_skills || [];
  const matched = atsSkills?.filter((s) => s.is_match);
  const unmatched = atsSkills?.filter((s) => !s.is_match);
  return {
    matched: matched,
    unmatched: unmatched,
  };
});

function sortSkills(skills: AtsSkill[]) {
  // @ts-ignore
  return skills?.sort((a, b) => b.is_match - a.is_match) || [];
}

watchEffect(() => {
  if (!analysis.value) {
    return;
  }
  Object.entries(analysis.value).forEach(([heading, section]) => {
    if (typeof section === "object") {
      items.value.push({
        heading: _.upperFirst(_.lowerCase(_.upperCase(heading))),
        section: section,
      });
    }
  });
});
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
