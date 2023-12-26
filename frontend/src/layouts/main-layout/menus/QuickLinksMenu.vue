<template>
  <!--begin::Menu-->
  <div
    class="menu menu-sub menu-sub-dropdown menu-column w-250px w-lg-325px"
    data-kt-menu="true"
  >
    <!--begin::Heading-->
    <div
      class="d-flex flex-column flex-center bgi-no-repeat rounded-top px-9 py-10"
      :style="{
        backgroundImage: `url(${getAssetPath(
          '/media/misc/menu-header-bg.jpg'
        )})`,
      }"
    >
      <!--begin::Title-->
      <h3 class="text-white fw-semobold mb-3">Quick Links</h3>
      <!--end::Title-->

      <!--begin::Status-->
      <span class="badge bg-success py-2 px-3">25 pending tasks</span>
      <!--end::Status-->
    </div>
    <!--end::Heading-->

    <!--begin:Nav-->
    <div class="row g-0">
      <!--begin:Item-->
      <div class="col-6">
        <a
          href="#"
          class="d-flex flex-column flex-center h-100 p-6 bg-hover-light border-end border-bottom"
        >
          <KTIcon icon-name="euro" icon-class="fs-3x text-success mb-2" />
          <span class="fs-5 fw-semobold text-gray-800 mb-0">Accounting</span>
          <span class="fs-7 text-gray-400">eCommerce</span>
        </a>
      </div>
      <!--end:Item-->

      <!--begin:Item-->
      <div class="col-6">
        <a
          href="#"
          class="d-flex flex-column flex-center h-100 p-6 bg-hover-light border-bottom"
        >
          <KTIcon icon-name="sms" icon-class="fs-3x text-success mb-2" />
          <span class="fs-5 fw-semobold text-gray-800 mb-0"
            >Administration</span
          >
          <span class="fs-7 text-gray-400">Console</span>
        </a>
      </div>
      <!--end:Item-->

      <!--begin:Item-->
      <div class="col-6">
        <a
          href="#"
          class="d-flex flex-column flex-center h-100 p-6 bg-hover-light border-end"
        >
          <KTIcon
            icon-name="abstract-41"
            icon-class="fs-3x text-success mb-2"
          />
          <span class="fs-5 fw-semobold text-gray-800 mb-0">Projects</span>
          <span class="fs-7 text-gray-400">Pending Tasks</span>
        </a>
      </div>
      <!--end:Item-->

      <!--begin:Item-->
      <div class="col-6">
        <a
          href="#"
          class="d-flex flex-column flex-center h-100 p-6 bg-hover-light"
        >
          <KTIcon icon-name="briefcase" icon-class="fs-3x text-success mb-2" />
          <span class="fs-5 fw-semobold text-gray-800 mb-0">Customers</span>
          <span class="fs-7 text-gray-400">Latest cases</span>
        </a>
      </div>
      <!--end:Item-->
    </div>
    <!--end:Nav-->

    <!--begin::View more-->
    <div class="py-2 text-center border-top">
      <a href="#" class="btn btn-color-gray-600 btn-active-color-primary">
        View All
        <KTIcon icon-name="arrow-right" icon-class="fs-5" />
      </a>
    </div>
    <!--end::View more-->
  </div>
  <!--end::Menu-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";

export default defineComponent({
  name: "kt-quick-links-menu",
  components: {},
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
