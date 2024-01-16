<template>
  <!--begin::Toolbar-->
  <div v-if="user" class="toolbar py-5 py-lg-15" id="kt_toolbar">
    <!--begin::Container-->
    <div
      id="kt_toolbar_container"
      :class="{
        'container-fluid': toolbarWidthFluid,
        'container-xxl': !toolbarWidthFluid,
      }"
      class="d-flex flex-stack flex-wrap"
    >
      <!--      <div></div>-->
      <Notice
        v-if="user.plan === 'free'"
        classes="border-0 w-fluid"
        color="warning"
        title="You're on a free plan"
        :body="`you have ${user.resume_analysis_remaining} resume analysis and ${user.scans_remaining} scan analysis remaining, consider upgrading your account`"
      ></Notice>

      <!--      <PageTitle />-->

      <!--begin::Actions-->
      <div class="d-flex align-items-center py-3 py-md-1">
        <!--        &lt;!&ndash;begin::Wrapper&ndash;&gt;-->
        <!--        <div class="me-4">-->
        <!--          &lt;!&ndash;begin::Menu&ndash;&gt;-->
        <!--          <a-->
        <!--            href="#"-->
        <!--            class="btn btn-custom btn-active-white btn-flex btn-color-white btn-active-color-primary fw-bold"-->
        <!--            data-kt-menu-trigger="click"-->
        <!--            data-kt-menu-placement="bottom-end"-->
        <!--            data-kt-menu-flip="top-end"-->
        <!--          >-->
        <!--            <KTIcon icon-name="filter" icon-class="fs-5 text-gray-500 me-1" />-->
        <!--            Filter-->
        <!--          </a>-->

        <!--          <Dropdown1></Dropdown1>-->
        <!--          &lt;!&ndash;end::Menu&ndash;&gt;-->
        <!--        </div>-->
        <!--        &lt;!&ndash;end::Wrapper&ndash;&gt;-->

        <!--begin::Button-->
        <button
          data-bs-theme="light"
          class="btn bg-body btn-active-color-primary mx-2"
          data-bs-toggle="modal"
          data-bs-target="#upload_resume_modal"
          id="kt_toolbar_primary_button"
        >
          Upload Resume
        </button>

        <button
          data-bs-theme="light"
          data-bs-toggle="modal"
          class="btn btn-primary btn-active-color-secondary"
          data-bs-target="#scan_job_modal"
          id="kt_toolbar_primary_button"
        >
          Scan Job (ATS)
        </button>
        <!--end::Button-->
      </div>
      <!--end::Actions-->
    </div>
    <!--end::Container-->
  </div>
  <!--end::Toolbar-->
</template>

<script lang="ts" setup>
import PageTitle from "@/layouts/main-layout/toolbar/PageTitle.vue";
import { toolbarWidthFluid } from "@/core/helpers/config";
import Notice from "@/components/Notice.vue";
import { storeToRefs } from "pinia";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();
const { user } = storeToRefs(authStore);
</script>
