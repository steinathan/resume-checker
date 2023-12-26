<template>
  <!--begin::Tables Widget 9-->
  <div class="card" v-if="items.length > 0">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Analysis Result</span>

        <span class="text-muted mt-1 fw-semobold fs-7"
          >{{ analysis?.total_issues }} Issues,
          {{ analysis?.total_improvements }} areas can be improved</span
        >
      </h3>

      <!--      <div-->
      <!--        class="card-toolbar"-->
      <!--        data-bs-toggle="tooltip"-->
      <!--        data-bs-placement="top"-->
      <!--        data-bs-trigger="hover"-->
      <!--        title="Click to add a user"-->
      <!--      >-->
      <!--        <a-->
      <!--          href="#"-->
      <!--          class="btn btn-sm btn-light-primary"-->
      <!--          data-bs-toggle="modal"-->
      <!--          data-bs-target="#kt_modal_invite_friends"-->
      <!--        >-->
      <!--          <KTIcon icon-name="plus" icon-class="fs-3" />-->
      <!--          New Member-->
      <!--        </a>-->
      <!--      </div>-->
    </div>
    <!--end::Header-->

    <!--begin::Body-->
    <div class="card-body py-3">
      <div class="table-responsive">
        <!--begin::Table-->
        <table
          class="table table-row-dashed table-row-gray-300 align-middle gs-0 gy-4"
        >
          <!--begin::Table head-->
          <thead>
            <tr class="fw-bold text-muted">
              <th class="min-w-150px">Section</th>
              <th class="min-w-140px">Issues</th>
              <th class="min-w-120px">Improvements</th>
              <th class="min-w-140px">Done</th>
            </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
            <template v-for="(item, index) in items" :key="index">
              <tr>
                <!-- heading -->
                <td>
                  <div class="d-flex align-items-center">
                    <div class="d-flex justify-content-start flex-column">
                      <a class="text-dark fw-bold text-hover-primary fs-6">
                        {{ item.heading }}</a
                      >
                      <!--                      <span-->
                      <!--                        class="text-muted fw-semobold text-muted d-block fs-7"-->
                      <!--                        >{{ "createdAt" }}</span-->
                      <!--                      >-->
                    </div>
                  </div>
                </td>

                <!-- issues -->
                <td>
                  <span v-if="item.section.issues?.length == 0">
                    <i class="fas fa-shield-cat text-info fs-4"></i>

                    No issue</span
                  >
                  <ul>
                    <li
                      v-for="(issue, i) in item.section.issues"
                      :key="i"
                      class="text-capitalize"
                    >
                      <i class="fas fa-xmark-circle text-danger fs-4"></i>
                      {{ issue }}
                    </li>
                  </ul>
                  <!--                  <span class="text-muted fw-semobold text-muted d-block fs-7"-->
                  <!--                    >issues found in your resume</span-->
                  <!--                  >-->
                </td>

                <!-- improvements -->
                <td>
                  <div class="d-flex flex-column float-end w-100 me-2">
                    <div class="d-flex flex-stack mb-2">
                      <span v-if="item.section.improvements?.length == 0">
                        <i class="fas fa-shield-cat text-info fs-4"></i>
                        No improvements to make</span
                      >

                      <ul>
                        <li
                          v-for="(improvement, i) in item.section.improvements"
                          :key="i"
                          class="text-capitalize"
                        >
                          <i class="fas fa-pen text-warning"></i>
                          {{ improvement }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </td>

                <!-- sections done -->
                <td class="">
                  <div class="d-flex flex-column w-100 me-2">
                    <div class="d-flex flex-stack mb-2">
                      <div class="me-2 fs-7 fw-semobold">
                        <span v-if="item.section.done?.length == 0">
                          <i class="fas fa-shield-cat text-info fs-4"></i>
                          No improvements</span
                        >

                        <ul>
                          <li
                            class="text-capitalize"
                            v-for="(done, i) in item.section.done"
                            :key="i"
                          >
                            <i
                              class="fas fa-check-circle text-success fs-2"
                            ></i>
                            {{ done }}
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </td>
              </tr>
            </template>
          </tbody>
          <!--end::Table body-->
        </table>
        <!--end::Table-->
      </div>
      <!--end::Table container-->
    </div>
    <!--begin::Body-->
  </div>
  <!--end::Tables Widget 9-->
</template>

<script lang="ts" setup>
import { get } from "@/core/services/ApiService2";
import { computed, onMounted, ref, watchEffect } from "vue";
import type { Resume, ResumeLLMAnalysis, ResumeSection } from "../../types";
import { useRoute } from "vue-router";
import { useResumeStore } from "@/stores/resume";
import { storeToRefs } from "pinia";
import _ from "lodash";

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
