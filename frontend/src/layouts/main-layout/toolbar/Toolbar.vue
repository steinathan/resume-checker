<template>
  <!--begin::Toolbar-->
  <div class="toolbar py-5 py-lg-15" id="kt_toolbar">
    <!--begin::Container-->
    <div
      id="kt_toolbar_container"
      :class="{
        'container-fluid': toolbarWidthFluid,
        'container-xxl': !toolbarWidthFluid,
      }"
      class="d-flex flex-stack flex-wrap"
    >
      <PageTitle />

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

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import PageTitle from "@/layouts/main-layout/toolbar/PageTitle.vue";
import Dropdown1 from "@/components/dropdown/Dropdown1.vue";
import { toolbarWidthFluid } from "@/core/helpers/config";

export default defineComponent({
  name: "KToolbar",
  components: {
    Dropdown1,
    PageTitle,
  },
  setup() {
    return {
      toolbarWidthFluid,
      getAssetPath,
    };
  },
});
</script>
