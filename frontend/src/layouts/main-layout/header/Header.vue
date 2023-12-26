<template>
  <!--begin::Header-->
  <div
    id="kt_header"
    class="header align-items-stretch"
    :data-kt-sticky="isHeaderSticky"
    data-kt-sticky-name="header"
    data-kt-sticky-offset="{default: '200px', lg: '300px'}"
  >
    <!--begin::Container-->
    <div
      :class="{
        'container-fluid': headerWidthFluid,
        'container-xxl': !headerWidthFluid,
      }"
      class="d-flex align-items-center"
    >
      <!--begin::Aside mobile toggle-->
      <div
        class="d-flex topbar align-items-center d-lg-none ms-n2 me-3"
        title="Show aside menu"
      >
        <div
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          id="kt_header_menu_mobile_toggle"
        >
          <KTIcon icon-name="abstract-14" icon-class="fs-1" />
        </div>
      </div>
      <!--end::Aside mobile toggle-->

      <!--begin::Mobile logo-->
      <div class="header-logo me-5 me-md-10 flex-grow-1 flex-lg-grow-0">
        <router-link to="/dashboard">
          <img
            alt="Logo"
            :src="getAssetPath('media/logos/demo2.png')"
            class="logo-default h-25px"
          />
          <img
            alt="Logo"
            :src="getAssetPath('media/logos/demo2-sticky.png')"
            class="logo-sticky h-25px"
          />
        </router-link>
      </div>
      <!--end::Mobile logo-->

      <!--begin::Wrapper-->
      <div
        class="d-flex align-items-stretch justify-content-between flex-lg-grow-1"
      >
        <!--begin::Navbar-->
        <div class="d-flex align-items-stretch" id="kt_header_nav">
          <KTMenu></KTMenu>
        </div>
        <!--end::Navbar-->

        <!--begin::Topbar-->
        <div class="d-flex align-items-stretch flex-shrink-0">
          <KTTopbar></KTTopbar>
        </div>
        <!--end::Topbar-->
      </div>
      <!--end::Wrapper-->
    </div>
    <!--end::Container-->
  </div>
  <!--end::Header-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { computed, defineComponent } from "vue";
import KTTopbar from "@/layouts/main-layout/header/Topbar.vue";
import KTMenu from "@/layouts/main-layout/header/Menu.vue";

import {
  asideDisplay,
  headerFixed,
  headerFixedOnMobile,
  headerLeft,
  headerWidthFluid,
} from "@/core/helpers/config";

export default defineComponent({
  name: "KTHeader",
  components: {
    KTTopbar,
    KTMenu,
  },
  setup() {
    const isHeaderSticky = computed(() => {
      if (window.innerWidth > 768) {
        return headerFixed.value;
      } else {
        return headerFixedOnMobile.value;
      }
    });

    return {
      headerWidthFluid,
      headerLeft,
      asideDisplay,
      isHeaderSticky,
      getAssetPath,
    };
  },
});
</script>
