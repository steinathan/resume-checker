<template>
  <div class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Latest Job Scans</span>
        <span class="text-muted mt-1 fw-semobold fs-7">0 JobScan</span>
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
          v-if="true"
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
                <tr class="border-0">
                  <th class="p-0 w-50px"></th>
                  <th class="p-0 min-w-150px"></th>
                  <th class="p-0 min-w-140px"></th>
                  <th class="p-0 min-w-110px"></th>
                  <th class="p-0 min-w-50px"></th>
                </tr>
              </thead>
              <!--end::Table head-->
              <!--begin::Table body-->
              <tbody>
                <tr>
                  <td>
                    <div class="symbol symbol-45px me-2">
                      <span class="symbol-label">
                        <img
                          :src="getAssetPath('media/svg/brand-logos/plurk.svg')"
                          class="h-50 align-self-center"
                          alt=""
                        />
                      </span>
                    </div>
                  </td>
                  <td>
                    <a
                      href="#"
                      class="text-dark fw-bold text-hover-primary mb-1 fs-6"
                      >Brad Simmons</a
                    >
                    <span class="text-muted fw-semobold d-block"
                      >Movie Creator</span
                    >
                  </td>
                  <td class="text-end text-muted fw-semobold">React, HTML</td>
                  <td class="text-end">
                    <span class="badge badge-light-success">Approved</span>
                  </td>
                  <td class="text-end">
                    <a
                      href="#"
                      class="btn btn-sm btn-icon btn-bg-light btn-active-color-primary"
                    >
                      <KTIcon icon-name="arrow-right" icon-class="fs-2" />
                    </a>
                  </td>
                </tr>
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
</script>
