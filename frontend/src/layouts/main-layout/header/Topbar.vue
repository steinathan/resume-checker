<template>
  <!--begin::Toolbar wrapper-->
  <div class="d-flex align-items-stretch flex-shrink-0">
    <div class="topbar d-flex align-items-stretch flex-shrink-0">
      <!--begin::Search-->
      <div class="d-flex align-items-stretch ms-1 ms-lg-3">
        <KTSearch></KTSearch>
      </div>
      <!--end::Search-->

      <!--begin::Activities-->
      <div class="d-flex align-items-center ms-1 ms-lg-3">
        <!--begin::drawer toggle-->
        <div
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          id="kt_activities_toggle"
        >
          <KTIcon icon-name="chart-simple" icon-class="fs-1" />
        </div>
        <!--end::drawer toggle-->
      </div>
      <!--end::Activities-->

      <!--begin::Notifications-->
      <div class="d-flex align-items-center ms-1 ms-lg-3">
        <!--begin::Menu-->
        <div
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          data-kt-menu-trigger="click"
          data-kt-menu-attach="parent"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-flip="bottom"
        >
          <KTIcon icon-name="element-plus" icon-class="fs-1" />
        </div>
        <KTNotificationsMenu></KTNotificationsMenu>
        <!--end::Menu-->
      </div>
      <!--end::Notifications-->

      <!--begin::Chat-->
      <div class="d-flex align-items-center ms-1 ms-lg-3">
        <!--begin::Menu wrapper-->
        <div
          class="btn btn-icon btn-active-light-primary btn-custom position-relative w-30px h-30px w-md-40px h-md-40px"
          id="kt_drawer_chat_toggle"
        >
          <KTIcon icon-name="message-text-2" icon-class="fs-1" />

          <span
            class="bullet bullet-dot bg-success h-6px w-6px position-absolute translate-middle top-0 start-50 animation-blink"
          >
          </span>
        </div>
        <!--end::Menu wrapper-->
      </div>
      <!--end::Chat-->

      <!--begin::Quick links-->
      <div class="d-flex align-items-center ms-1 ms-lg-3">
        <!--begin::Menu-->
        <div
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          data-kt-menu-trigger="click"
          data-kt-menu-attach="parent"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-flip="bottom"
        >
          <KTIcon icon-name="element-11" icon-class="fs-1" />
        </div>
        <KTQuickLinksMenu></KTQuickLinksMenu>
        <!--end::Menu-->
      </div>
      <!--end::Quick links-->

      <!--begin::Theme mode-->
      <div class="d-flex align-items-center ms-1 ms-lg-3">
        <!--begin::Menu toggle-->
        <a
          href="#"
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          data-kt-menu-trigger="{default:'click', lg: 'hover'}"
          data-kt-menu-attach="parent"
          data-kt-menu-placement="bottom-end"
        >
          <KTIcon
            icon-name="night-day"
            icon-class="theme-light-show fs-2 fs-md-1"
          />
          <KTIcon icon-name="moon" icon-class="theme-dark-show fs-2 fs-md-1" />
        </a>
        <!--begin::Menu toggle-->
        <KTThemeModeSwitcher></KTThemeModeSwitcher>
      </div>
      <!--end::Theme mode-->

      <!--begin::User-->
      <div
        class="d-flex align-items-center me-n3 ms-1 ms-lg-3"
        id="kt_header_user_menu_toggle"
      >
        <!--begin::Menu-->
        <div
          class="btn btn-icon btn-active-light-primary btn-custom w-30px h-30px w-md-40px h-md-40px"
          data-kt-menu-trigger="click"
          data-kt-menu-attach="parent"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-flip="bottom"
        >
          <img
            :src="getAssetPath('media/avatars/300-2.jpg')"
            alt="metronic"
            class="h-30px w-30px rounded"
          />
        </div>
        <KTUserMenu></KTUserMenu>
        <!--end::Menu-->
      </div>
      <!--end::User -->
    </div>
  </div>
  <!--end::Toolbar wrapper-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import KTSearch from "@/layouts/main-layout/search/Search.vue";
import KTNotificationsMenu from "@/layouts/main-layout/menus/NotificationsMenu.vue";
import KTQuickLinksMenu from "@/layouts/main-layout/menus/QuickLinksMenu.vue";
import KTUserMenu from "@/layouts/main-layout/menus/UserAccountMenu.vue";
import KTThemeModeSwitcher from "@/layouts/main-layout/theme-mode/ThemeModeSwitcher.vue";

export default defineComponent({
  name: "layout-topbar",
  components: {
    KTNotificationsMenu,
    KTQuickLinksMenu,
    KTUserMenu,
    KTSearch,
    KTThemeModeSwitcher,
  },
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
