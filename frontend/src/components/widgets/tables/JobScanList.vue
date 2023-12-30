<template>
  <div class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Latest Job Scans</span>
        <span class="text-muted mt-1 fw-semobold fs-7"
          >{{ scans.length }} JobScan(s)</span
        >
      </h3>
      <!--      <div class="card-toolbar">-->
      <!--        <ul class="nav">-->
      <!--          <li class="nav-item">-->
      <!--            <a-->
      <!--              class="nav-link btn btn-sm btn-color-muted btn-active btn-active-light-primary fw-bold px-4 me-1 active"-->
      <!--              data-bs-toggle="tab"-->
      <!--              href="#kt_table_widget_5_tab_1"-->
      <!--              >Month</a-->
      <!--            >-->
      <!--          </li>-->
      <!--          <li class="nav-item">-->
      <!--            <a-->
      <!--              class="nav-link btn btn-sm btn-color-muted btn-active btn-active-light-primary fw-bold px-4 me-1"-->
      <!--              data-bs-toggle="tab"-->
      <!--              href="#kt_table_widget_5_tab_2"-->
      <!--              >Week</a-->
      <!--            >-->
      <!--          </li>-->
      <!--          <li class="nav-item">-->
      <!--            <a-->
      <!--              class="nav-link btn btn-sm btn-color-muted btn-active btn-active-light-primary fw-bold px-4"-->
      <!--              data-bs-toggle="tab"-->
      <!--              href="#kt_table_widget_5_tab_3"-->
      <!--              >Day</a-->
      <!--            >-->
      <!--          </li>-->
      <!--        </ul>-->
      <!--      </div>-->
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body py-3">
      <div class="tab-content">
        <!--begin::Tap pane-->
        <EmptyState
          v-if="scans.length === 0"
          type="job_scan"
          title="It's lonely here"
          description="You have no job scans, click the button below to get started"
        />
        <div
          v-else
          class="tab-pane fade active show"
          id="kt_table_widget_5_tab_1"
        >
          <!--begin::Table container-->
          <div class="table-responsive">
            <!--begin::Table-->
            <table
              class="table table-row-dashed table-row-gray-200 align-middle gs-0 gy-4"
            >
              <!--begin::Table head-->
              <thead>
                <tr class="fw-bold text-muted">
                  <!--                  <th class="p-0 w-50px"></th>-->
                  <th class="p-0">Score</th>
                  <th class="p-0">Name</th>
                  <th class="p-0">Scanned At</th>
                  <th class="p-0">Cover letterID</th>
                  <th class="p-0">Resume ID</th>
                  <!--                  <th class="p-0 min-w-50px text-end">Action</th>-->
                </tr>
              </thead>
              <!--end::Table head-->
              <!--begin::Table body-->
              <tbody>
                <template v-for="scan in scans" :key="scan.id">
                  <tr>
                    <!--                    <td>-->
                    <!--                      <div class="symbol symbol-45px me-2">-->
                    <!--                        <span class="symbol-label">-->
                    <!--                          <img-->
                    <!--                            :src="-->
                    <!--                              getAssetPath('media/svg/brand-logos/plurk.svg')-->
                    <!--                            "-->
                    <!--                            class="h-50 align-self-center"-->
                    <!--                            alt=""-->
                    <!--                          />-->
                    <!--                        </span>-->
                    <!--                      </div>-->
                    <!--                    </td>-->
                    <td class="text-muted fw-bolder fs-1">
                      <span
                        :style="`color: ${getColorCodeByPercentage(
                          scan.ats_analysis?.score * 10
                        )}`"
                        >{{ scan.ats_analysis?.score }}</span
                      >
                    </td>
                    <td>
                      <router-link
                        :to="{
                          name: 'single-scan',
                          params: {
                            scan_id: scan.id,
                          },
                          query: {
                            from: 'dashboard',
                          },
                        }"
                      >
                        <span
                          class="text-dark fw-bold text-hover-primary mb-1 fs-6"
                          >{{ scan?.ats_analysis?.job_title }}
                        </span>
                        <span class="text-muted fw-semobold d-block">
                          {{ scan?.ats_analysis?.company_name }}</span
                        >
                      </router-link>
                    </td>
                    <td>
                      {{
                        moment(scan.created_at).format(
                          "MMMM Do YYYY, h:mm:ss a"
                        )
                      }}
                    </td>
                    <!--                    <td>-->
                    <!--                      <span-->
                    <!--                        class="badge badge-secondary text-truncate"-->
                    <!--                        style="max-width: 150px"-->
                    <!--                      >-->
                    <!--                        {{ scan.job_url || scan.job_description }}...-->
                    <!--                      </span>-->
                    <!--                    </td>-->
                    <td class="">
                      {{ scan.cover_letter_id || "non generated" }}
                    </td>
                    <td class="">
                      <router-link
                        :to="{
                          name: 'single-resume',
                          params: {
                            resume_id: scan.resume_id,
                          },
                          query: {
                            from: 'dashboard',
                          },
                        }"
                      >
                        {{ scan.resume_id }}
                      </router-link>
                    </td>
                    <!--                    <td class="text-end">-->
                    <!--                      <a-->
                    <!--                        href=""-->
                    <!--                        class="btn btn-sm btn-icon btn-bg-light btn-active-color-primary"-->
                    <!--                      >-->
                    <!--                        <KTIcon icon-name="arrow-right" icon-class="fs-2" />-->
                    <!--                      </a>-->
                    <!--                    </td>-->
                  </tr>
                </template>
              </tbody>
              <!--end::Table body-->
            </table>
          </div>
          <!--end::Table-->
        </div>
        <!--end::Tap pane-->
      </div>
    </div>
    <!--end::Body-->
  </div>
</template>

<script lang="ts" setup>
import { getAssetPath } from "@/core/helpers/assets";
import EmptyState from "@/components/EmptyState.vue";
import { onMounted, ref } from "vue";
import { get } from "@/core/services/ApiService2";
import type { JobScan } from "../../../../types";
import { getColorCodeByPercentage } from "@/core/helpers/color";
import moment from "moment";
import { storeToRefs } from "pinia";
import { useResumeStore } from "@/stores/resume";

const resumeStore = useResumeStore();
const { jobScans: scans } = storeToRefs(resumeStore);

onMounted(async () => {
  const _scans = await get<JobScan[]>("/job/scans", {});
  resumeStore.setJobScans(_scans);
});
</script>
