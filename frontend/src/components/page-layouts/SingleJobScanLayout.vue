<template>
  <!--begin::Navbar-->
  <div v-if="singleScan && analysis" class="card mb-5 mb-xxl-8">
    <div class="card-body pt-9 pb-0">
      <!--begin::Details-->
      <div class="d-flex flex-wrap flex-sm-nowrap mb-3">
        <!--begin: Pic-->
        <div class="me-10 mb-4">
          <div>
            <div class="fs-1 fw-bolder">
              <span
                class="total_score"
                :style="{
                  color: getColorCodeByPercentage(analysis?.score * 10),
                }"
              >
                {{ analysis?.score }}
              </span>
              <span class="text-muted score_base"> /10 </span>
            </div>

            <div
              class="position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle border border-4 border-white h-20px w-20px"
            ></div>
          </div>
        </div>
        <!--end::Pic-->

        <!--begin::Info-->
        <div class="flex-grow-1">
          <!--begin::Title-->
          <div
            class="d-flex justify-content-between align-items-start flex-wrap mb-2"
          >
            <!--begin::User-->
            <div class="d-flex flex-column">
              <!--begin::Name-->

              <div class="d-flex align-items-center mb-2">
                <span
                  class="text-gray-800 text-hover-primary fs-2 fw-bold me-1"
                  >{{ singleScan.ats_analysis.job_title }}</span
                >
                <span>
                  <KTIcon
                    title="Analyzed successfully"
                    icon-name="verify"
                    icon-class="fs-1 text-primary"
                  />
                </span>
              </div>
              <!--end::Name-->

              <!--begin::Info-->
              <div class="d-flex flex-wrap fw-semobold fs-6 mb-4 pe-2">
                <span
                  class="d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2"
                >
                  <KTIcon icon-name="calendar" icon-class="fs-4 me-1" />
                  {{ singleScan.created_at }}
                </span>
              </div>
              <!--end::Info-->
              <!--begin::Info-->
              <div class="d-flex flex-wrap fw-semobold fs-6 mb-4 pe-2">
                <span
                  class="d-flex align-items-center text-gray-400 text-hover-primary me-5 mb-2"
                >
                  <KTIcon icon-name="user" icon-class="fs-4 me-1" />
                  {{ analysis.company_name }}
                </span>
              </div>
              <!--end::Info-->
            </div>
            <!--end::User-->

            <!--begin::Actions-->
            <div class="d-flex my-4">
              <!--              <a-->
              <!--                href="#"-->
              <!--                class="btn btn-sm btn-light me-2"-->
              <!--                id="kt_user_follow_button"-->
              <!--              >-->
              <!--                <KTIcon icon-name="check" icon-class="fs-3 d-none" />-->
              <!--                Re-San-->
              <!--              </a>-->

              <!--begin::Menu-->
              <div class="me-0">
                <button
                  class="btn btn-sm btn-icon btn-bg-light btn-active-color-primary"
                  data-kt-menu-trigger="click"
                  data-kt-menu-placement="bottom-end"
                  data-kt-menu-flip="top-end"
                >
                  <i class="bi bi-three-dots fs-3"></i>
                </button>
                <!--                <Dropdown3></Dropdown3>-->
              </div>
              <!--end::Menu-->
            </div>
            <!--end::Actions-->
          </div>
          <!--end::Title-->

          <!--begin::Stats-->
          <div class="d-flex flex-wrap flex-stack">
            <!--begin::Wrapper-->
            <div class="d-flex flex-column flex-grow-1 pe-8">
              <!--begin::Stats-->
              <div
                class="d-flex flex-wrap"
                v-if="analysis && Object.keys(analysis).length > 0"
              >
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.contact_info.score"-->
                <!--                  title="Contact Information"-->
                <!--                />-->
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.education.score"-->
                <!--                  title="Education"-->
                <!--                />-->
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.date_formatting.score"-->
                <!--                  title="Date Formatting"-->
                <!--                />-->
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.experience.score"-->
                <!--                  title="Experience Information"-->
                <!--                />-->
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.personal_projects.score"-->
                <!--                  title="Personal Projects"-->
                <!--                />-->
                <!--                <ResumeHeaderStat-->
                <!--                  :score="analysis.skills.score"-->
                <!--                  title="Skills Section"-->
                <!--                />-->
              </div>
              <!--end::Stats-->
            </div>
            <!--end::Wrapper-->

            <!--begin::Progress-->
            <!--            <div-->
            <!--              class="d-flex align-items-center w-200px w-sm-300px flex-column mt-3"-->
            <!--            >-->
            <!--              <div class="d-flex justify-content-between w-100 mt-auto mb-2">-->
            <!--                <span class="fw-semobold fs-6 text-gray-400"-->
            <!--                  >Profile Compleation</span-->
            <!--                >-->
            <!--                <span class="fw-bold fs-6">50%</span>-->
            <!--              </div>-->

            <!--              <div class="h-5px mx-3 w-100 bg-light mb-3">-->
            <!--                <div-->
            <!--                  class="bg-success rounded h-5px"-->
            <!--                  role="progressbar"-->
            <!--                  style="width: 50%"-->
            <!--                  aria-valuenow="50"-->
            <!--                  aria-valuemin="0"-->
            <!--                  aria-valuemax="100"-->
            <!--                ></div>-->
            <!--              </div>-->
            <!--            </div>-->
            <!--end::Progress-->
          </div>
          <!--end::Stats-->
        </div>
        <!--end::Info-->
      </div>
      <!--end::Details-->

      <!--begin::Navs-->
      <div class="d-flex overflow-auto h-55px">
        <ul
          class="nav nav-stretch nav-line-tabs nav-line-tabs-2x border-transparent fs-5 fw-bold flex-nowrap"
        >
          <!--begin::Nav item-->
          <li class="nav-item">
            <router-link
              :to="`/scans/${singleScan.id}/results`"
              class="nav-link text-active-primary me-6"
              active-class="active"
            >
              ATS Analysis
            </router-link>
          </li>
          <!--end::Nav item-->
          <!--begin::Nav item-->
          <li class="nav-item">
            <router-link
              class="nav-link text-active-primary me-6"
              :to="`/scans/${singleScan.id}/resume`"
              active-class="active"
            >
              Resume
            </router-link>
          </li>
          <!--end::Nav item-->
          <!--begin::Nav item-->
          <li class="nav-item">
            <router-link
              class="nav-link text-active-primary me-6"
              :to="`/scans/${singleScan.id}/cover-letter`"
              active-class="active"
            >
              Cover letter
            </router-link>
          </li>
          <!--end::Nav item-->
        </ul>
      </div>
      <!--begin::Navs-->
    </div>
  </div>
  <!--end::Navbar-->
  <router-view></router-view>
</template>

<script lang="ts" setup>
import Dropdown3 from "@/components/dropdown/Dropdown3.vue";
import { computed, onMounted, ref } from "vue";
import type {
  ATSAnalysis,
  JobScan,
  JobScanResult,
  Resume,
  ResumeLLMAnalysis,
} from "../../../types";
import { useRoute } from "vue-router";
import { get } from "@/core/services/ApiService2";
import ResumeHeaderStat from "@/components/ResumeHeaderStat.vue";
import KTIcon from "@/core/helpers/kt-icon/KTIcon.vue";
import { getColorCodeByPercentage } from "@/core/helpers/color";
import { useResumeStore } from "@/stores/resume";
import { storeToRefs } from "pinia";

const route = useRoute();

const resumeStore = useResumeStore();
const { singleScan } = storeToRefs(resumeStore);
const analysis = computed<ATSAnalysis>(() => {
  return singleScan.value.ats_analysis;
});

onMounted(async () => {
  const scan = await get<JobScanResult>(
    "/job/scans/" + route.params["scan_id"]
  );
  resumeStore.setJobScan(scan?.job_scan);
  resumeStore.setCoverLetter(scan?.cover_letter);

  if (scan && scan.job_scan?.resume_id) {
    await resumeStore.fetchResume(scan.job_scan?.resume_id);
  }
});
</script>

<style>
.total_score {
  font-size: 50px !important;
}
</style>
