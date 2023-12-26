<template>
  <!--begin::Tables Widget 9-->

  <div class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Your Resumes</span>

        <span class="text-muted mt-1 fw-semobold fs-7"
          >{{ resumes.length }} resume(s)</span
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
      <!--begin::Table container-->
      <EmptyState
        v-if="resumes.length === 0"
        type="job_scan"
        title="No Resume"
        description="Upload a resume to get started"
      ></EmptyState>

      <div class="table-responsive">
        <!--begin::Table-->
        <table
          class="table table-row-dashed table-row-gray-300 align-middle gs-0 gy-4"
        >
          <!--begin::Table head-->
          <thead>
            <tr class="fw-bold text-muted">
              <th class="w-25px">
                <div
                  class="form-check form-check-sm form-check-custom form-check-solid"
                >
                  <input
                    class="form-check-input"
                    type="checkbox"
                    @change="
                      checkedRows.length === 6
                        ? (checkedRows.length = 0)
                        : (checkedRows = [0, 1, 2, 3, 4, 5])
                    "
                  />
                </div>
              </th>
              <th class="min-w-150px">Name</th>
              <th class="min-w-150px">Score</th>
              <th class="min-w-140px">Issues</th>
              <th class="min-w-120px">Improvements</th>
              <!--              <th class="min-w-140px">Done</th>-->
              <th class="min-w-100px text-end">Actions</th>
            </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
            <template v-for="(resume, index) in resumes" :key="index">
              <tr>
                <td>
                  <div
                    class="form-check form-check-sm form-check-custom form-check-solid"
                  >
                    <input
                      class="form-check-input widget-9-check"
                      type="checkbox"
                      :value="index"
                      v-model="checkedRows"
                    />
                  </div>
                </td>

                <!-- name -->
                <td>
                  <div class="d-flex align-items-center">
                    <div class="d-flex justify-content-start flex-column">
                      <router-link
                        :to="{
                          name: 'single-resume',
                          params: { resume_id: resume.id },
                        }"
                        class="text-dark fw-bold text-hover-primary fs-6"
                        >{{ resume.name }}</router-link
                      >
                      <span
                        class="text-muted fw-semobold text-muted d-block fs-7"
                        >{{
                          moment(resume.created_at).format(
                            "MMMM Do YYYY, h:mm:ss a"
                          )
                        }}</span
                      >
                    </div>
                  </div>
                </td>

                <!-- resume score -->
                <td>
                  <span
                    class="text-dark fw-bold text-hover-primary d-block fs-6"
                    >{{ resume.analysis?.total_score }}/10</span
                  >
                  <span class="text-muted fw-semobold text-muted d-block fs-7"
                    >Overall rating</span
                  >
                  <div class="progress h-6px w-100">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      :style="{
                        background: getColorCodeByPercentage(
                          resume.analysis?.total_score * 10
                        ),
                        width: resume.analysis?.total_score * 10 + '%',
                      }"
                      aria-valuemin="0"
                      aria-valuemax="10"
                    ></div>
                  </div>
                </td>

                <!-- issues -->
                <td class="text-end">
                  <div class="d-flex flex-column w-100 me-2">
                    <div class="d-flex flex-stack mb-2">
                      <span class="text-muted me-2 fs-7 fw-bolder">
                        {{ resume.analysis?.total_issues }}
                      </span>
                    </div>
                  </div>
                </td>

                <!-- improvements -->
                <td class="text-end">
                  <div class="d-flex flex-column w-100 me-2">
                    <div class="d-flex flex-stack mb-2">
                      <span class="text-muted me-2 fs-7 fw-semobold">
                        {{ resume.analysis?.total_improvements }}
                      </span>
                    </div>
                  </div>
                </td>

                <!-- sections done -->
                <!--                <td class="text-end">-->
                <!--                  <div class="d-flex flex-column w-100 me-2">-->
                <!--                    <div class="d-flex flex-stack mb-2">-->
                <!--                      <div class="text-muted me-2 fs-7 fw-semobold">-->
                <!--                        {{ resume.analysis?.total_done }}-->
                <!--                      </div>-->
                <!--                    </div>-->
                <!--                  </div>-->
                <!--                </td>-->

                <!-- actions -->
                <td class="text-end">
                  <!--                  <a-->
                  <!--                    href="#"-->
                  <!--                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"-->
                  <!--                  >-->
                  <!--                    <KTIcon icon-name="pencil" icon-class="fs-3" />-->
                  <!--                  </a>-->

                  <a
                    href="#"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm"
                  >
                    <KTIcon icon-name="trash" icon-class="fs-3" />
                  </a>
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
import { onMounted, ref } from "vue";
import type { Resume } from "../../../../types";
import { getColorCodeByPercentage } from "@/core/helpers/color";
import moment from "moment";
import EmptyState from "@/components/EmptyState.vue";

const checkedRows = ref<Array<number>>([]);
const resumes = ref<Resume[]>([]);

onMounted(async () => {
  resumes.value = await get("/resumes", {});
});
</script>
