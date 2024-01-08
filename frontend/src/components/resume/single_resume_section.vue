<template>
  <!--begin::Tables Widget 9-->
  <!--  <div class="card" v-if="items.length > 0">-->
  <!--    &lt;!&ndash;begin::Header&ndash;&gt;-->
  <!--    <div class="card-header border-0 pt-5">-->
  <!--      <h3 class="card-title align-items-start flex-column">-->
  <!--        <span class="card-label fw-bold fs-3 mb-1">Analysis Result</span>-->

  <!--        <span class="text-muted mt-1 fw-semobold fs-7"-->
  <!--          >{{ analysis?.total_issues }} Issues,-->
  <!--          {{ analysis?.total_improvements }} areas can be improved</span-->
  <!--        >-->
  <!--      </h3>-->

  <!--      &lt;!&ndash;      <div&ndash;&gt;-->
  <!--      &lt;!&ndash;        class="card-toolbar"&ndash;&gt;-->
  <!--      &lt;!&ndash;        data-bs-toggle="tooltip"&ndash;&gt;-->
  <!--      &lt;!&ndash;        data-bs-placement="top"&ndash;&gt;-->
  <!--      &lt;!&ndash;        data-bs-trigger="hover"&ndash;&gt;-->
  <!--      &lt;!&ndash;        title="Click to add a user"&ndash;&gt;-->
  <!--      &lt;!&ndash;      >&ndash;&gt;-->
  <!--      &lt;!&ndash;        <a&ndash;&gt;-->
  <!--      &lt;!&ndash;          href="#"&ndash;&gt;-->
  <!--      &lt;!&ndash;          class="btn btn-sm btn-light-primary"&ndash;&gt;-->
  <!--      &lt;!&ndash;          data-bs-toggle="modal"&ndash;&gt;-->
  <!--      &lt;!&ndash;          data-bs-target="#kt_modal_invite_friends"&ndash;&gt;-->
  <!--      &lt;!&ndash;        >&ndash;&gt;-->
  <!--      &lt;!&ndash;          <KTIcon icon-name="plus" icon-class="fs-3" />&ndash;&gt;-->
  <!--      &lt;!&ndash;          New Member&ndash;&gt;-->
  <!--      &lt;!&ndash;        </a>&ndash;&gt;-->
  <!--      &lt;!&ndash;      </div>&ndash;&gt;-->
  <!--    </div>-->
  <!--    &lt;!&ndash;end::Header&ndash;&gt;-->

  <!--    &lt;!&ndash;begin::Body&ndash;&gt;-->
  <!--    <div class="card-body py-3">-->
  <!--      <div class="table-responsive">-->
  <!--        &lt;!&ndash;begin::Table&ndash;&gt;-->
  <!--        <table-->
  <!--          class="table table-row-dashed table-row-gray-300 align-middle gs-0 gy-4"-->
  <!--        >-->
  <!--          &lt;!&ndash;begin::Table head&ndash;&gt;-->
  <!--          <thead>-->
  <!--            <tr class="fw-bold text-muted">-->
  <!--              <th class="min-w-150px">Section</th>-->
  <!--              <th class="min-w-140px">Issues</th>-->
  <!--              <th class="min-w-120px">Improvements</th>-->
  <!--              <th class="min-w-140px">Done</th>-->
  <!--            </tr>-->
  <!--          </thead>-->
  <!--          &lt;!&ndash;end::Table head&ndash;&gt;-->

  <!--          &lt;!&ndash;begin::Table body&ndash;&gt;-->
  <!--          <tbody>-->
  <!--            <template v-for="(item, index) in items" :key="index">-->
  <!--              <tr>-->
  <!--                &lt;!&ndash; heading &ndash;&gt;-->
  <!--                <td>-->
  <!--                  <div class="d-flex align-items-center">-->
  <!--                    <div class="d-flex justify-content-start flex-column">-->
  <!--                      <a class="text-dark fw-bold text-hover-primary fs-6">-->
  <!--                        {{ item.heading }}</a-->
  <!--                      >-->
  <!--                      &lt;!&ndash;                      <span&ndash;&gt;-->
  <!--                      &lt;!&ndash;                        class="text-muted fw-semobold text-muted d-block fs-7"&ndash;&gt;-->
  <!--                      &lt;!&ndash;                        >{{ "createdAt" }}</span&ndash;&gt;-->
  <!--                      &lt;!&ndash;                      >&ndash;&gt;-->
  <!--                    </div>-->
  <!--                  </div>-->
  <!--                </td>-->

  <!--                &lt;!&ndash; issues &ndash;&gt;-->
  <!--                <td>-->
  <!--                  <span v-if="item.section.issues?.length == 0">-->
  <!--                    <i class="fas fa-shield-cat text-info fs-4"></i>-->

  <!--                    No issue</span-->
  <!--                  >-->
  <!--                  <ul>-->
  <!--                    <li-->
  <!--                      v-for="(issue, i) in item.section.issues"-->
  <!--                      :key="i"-->
  <!--                      class="text-capitalize"-->
  <!--                    >-->
  <!--                      <i class="fas fa-xmark-circle text-danger fs-4"></i>-->
  <!--                      {{ issue }}-->
  <!--                    </li>-->
  <!--                  </ul>-->
  <!--                  &lt;!&ndash;                  <span class="text-muted fw-semobold text-muted d-block fs-7"&ndash;&gt;-->
  <!--                  &lt;!&ndash;                    >issues found in your resume</span&ndash;&gt;-->
  <!--                  &lt;!&ndash;                  >&ndash;&gt;-->
  <!--                </td>-->

  <!--                &lt;!&ndash; improvements &ndash;&gt;-->
  <!--                <td>-->
  <!--                  <div class="d-flex flex-column float-end w-100 me-2">-->
  <!--                    <div class="d-flex flex-stack mb-2">-->
  <!--                      <span v-if="item.section.improvements?.length == 0">-->
  <!--                        <i class="fas fa-shield-cat text-info fs-4"></i>-->
  <!--                        No improvements to make</span-->
  <!--                      >-->

  <!--                      <ul>-->
  <!--                        <li-->
  <!--                          v-for="(improvement, i) in item.section.improvements"-->
  <!--                          :key="i"-->
  <!--                          class="text-capitalize"-->
  <!--                        >-->
  <!--                          <i class="fas fa-pen text-warning"></i>-->
  <!--                          {{ improvement }}-->
  <!--                        </li>-->
  <!--                      </ul>-->
  <!--                    </div>-->
  <!--                  </div>-->
  <!--                </td>-->

  <!--                &lt;!&ndash; sections done &ndash;&gt;-->
  <!--                <td class="">-->
  <!--                  <div class="d-flex flex-column w-100 me-2">-->
  <!--                    <div class="d-flex flex-stack mb-2">-->
  <!--                      <div class="me-2 fs-7 fw-semobold">-->
  <!--                        <span v-if="item.section.done?.length == 0">-->
  <!--                          <i class="fas fa-shield-cat text-info fs-4"></i>-->
  <!--                          No improvements</span-->
  <!--                        >-->

  <!--                        <ul>-->
  <!--                          <li-->
  <!--                            class="text-capitalize"-->
  <!--                            v-for="(done, i) in item.section.done"-->
  <!--                            :key="i"-->
  <!--                          >-->
  <!--                            <i-->
  <!--                              class="fas fa-check-circle text-success fs-2"-->
  <!--                            ></i>-->
  <!--                            {{ done }}-->
  <!--                          </li>-->
  <!--                        </ul>-->
  <!--                      </div>-->
  <!--                    </div>-->
  <!--                  </div>-->
  <!--                </td>-->
  <!--              </tr>-->
  <!--            </template>-->
  <!--          </tbody>-->
  <!--          &lt;!&ndash;end::Table body&ndash;&gt;-->
  <!--        </table>-->
  <!--        &lt;!&ndash;end::Table&ndash;&gt;-->
  <!--      </div>-->
  <!--      &lt;!&ndash;end::Table container&ndash;&gt;-->
  <!--    </div>-->
  <!--    &lt;!&ndash;begin::Body&ndash;&gt;-->
  <!--  </div>-->
  <!--end::Tables Widget 9-->
  <!-- scan section -->
  <span class="fs-4 px-5"
    >{{ analysis?.total_issues }} Issues,
    {{ analysis?.total_improvements }} areas can be improved on your
    resume</span
  >
  <ScanSection
    title="Summary"
    :issues="analysis?.summary?.issues"
    :score="analysis?.summary?.score"
    :suggestion="analysis?.summary?.improvements"
    :done="analysis?.summary?.done"
    hide-checked
  />

  <ScanSection
    title="Contact Information"
    :issues="analysis?.contact_info?.issues"
    :score="analysis?.contact_info?.score"
    :suggestion="analysis?.contact_info?.improvements"
    :done="analysis?.contact_info?.done"
    hide-checked
  />
  <ScanSection
    title="Education"
    :issues="analysis?.education?.issues"
    :score="analysis?.education?.score"
    :suggestion="analysis?.education?.improvements"
    :done="analysis?.education?.done"
    hide-checked
  />

  <ScanSection
    title="Experience"
    :issues="analysis?.experience?.issues"
    :score="analysis?.experience?.score"
    :suggestion="analysis?.experience?.improvements"
    :done="analysis?.experience?.done"
    hide-checked
  />

  <ScanSection
    title="Skills"
    :issues="analysis?.skills?.issues"
    :score="analysis?.skills?.score"
    :suggestion="analysis?.skills?.improvements"
    :done="analysis?.skills?.done"
    hide-checked
  />

  <ScanSection
    title="Personal Projects"
    :issues="analysis?.personal_projects?.issues"
    :score="analysis?.personal_projects?.score"
    :suggestion="analysis?.personal_projects?.improvements"
    :done="analysis?.personal_projects?.done"
    hide-checked
  />

  <ScanSection
    title="Date Formatting"
    :issues="analysis?.date_formatting?.issues"
    :score="analysis?.date_formatting?.score"
    :suggestion="analysis?.date_formatting?.improvements"
    :done="analysis?.date_formatting?.done"
    hide-checked
  />

  <ScanSection
    title="Interests"
    :issues="analysis?.interests?.issues"
    :score="analysis?.interests?.score"
    :suggestion="analysis?.interests?.improvements"
    :done="analysis?.interests?.done"
    hide-checked
  />

  <ScanSection
    title="Section Headings"
    :issues="analysis?.section_headings?.issues"
    :score="analysis?.section_headings?.score"
    :suggestion="analysis?.section_headings?.improvements"
    :done="analysis?.section_headings?.done"
    hide-checked
  />

  <ScanSection
    title="Word Count"
    :issues="analysis?.word_count?.issues"
    :score="analysis?.word_count?.score"
    :suggestion="analysis?.word_count?.improvements"
    :done="analysis?.word_count?.done"
    hide-checked
  />

  <ScanSection
    title="File Info"
    :issues="analysis?.file_info?.issues"
    :score="analysis?.file_info?.score"
    :suggestion="analysis?.file_info?.improvements"
    :done="analysis?.file_info?.done"
    hide-checked
  />

  <div class="card my-10">
    <div class="card-body">
      <h1 class="card-title fw-bolder text-hover-primary fs-2">Skills</h1>
      <p class="fs-4">
        skills enable you to perform job-specific duties and responsibilities.
        You can learn skills in the classroom, training courses, and on the job.
        These skills are typically focused on teachable tasks and measurable
        abilities such as the use of tools, equipment, or software. skills have
        a high impact on your match score.
      </p>
      <span
        v-for="skill in resumeSkills"
        :key="skill.id"
        class="min-w-175px pe-2"
      >
        <span
          class="badge badge-light-primary text-muted fs-3 m-1 p-3 text-hover-primary"
        >
          {{ skill.name }}</span
        >
      </span>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed, onMounted, ref, watchEffect } from "vue";
import type { Resume, ResumeLLMAnalysis, ResumeSection } from "../../../types";
import { useResumeStore } from "@/stores/resume";
import { storeToRefs } from "pinia";
import _ from "lodash";
import ScanSection from "@/components/jobScan/ScanSection.vue";

type rev = {
  heading: string;
  section: ResumeSection;
};
const items = ref<rev[]>([]);
const resumeStore = useResumeStore();
const { resume } = storeToRefs(resumeStore);
const analysis = computed<ResumeLLMAnalysis>(
  () => resume?.value?.analysis || ({} as ResumeLLMAnalysis)
);

const resumeSkills = computed<any[]>(() => resume?.value?.skills || []);

watchEffect(() => {
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
