<template>
  <!--begin::Aside-->
  <div
    id="kt_aside"
    class="aside card"
    data-kt-drawer="true"
    data-kt-drawer-name="aside"
    data-kt-drawer-activate="{default: true, lg: false}"
    data-kt-drawer-overlay="true"
    data-kt-drawer-width="{default:'200px', '300px': '250px'}"
    data-kt-drawer-direction="start"
    data-kt-drawer-toggle="#kt_aside_mobile_toggle"
  >
    <!--begin::Aside menu-->
    <div class="aside-menu flex-column-fluid">
      <KTMenu></KTMenu>
    </div>
    <!--end::Aside menu-->

    <!--begin::Footer-->
    <div
      class="aside-footer flex-column-auto pt-5 pb-7 px-5"
      id="kt_aside_footer"
    >
      <a
        href="https://preview.keenthemes.com/metronic8/vue/docs/#/doc-overview"
        class="btn btn-custom btn-primary w-100"
        data-bs-toggle="tooltip"
        data-bs-trigger="hover"
        data-bs-delay-show="8000"
        title="Check out the complete documentation with over 100 components"
      >
        <span class="btn-label">
          {{ t("docsAndComponents") }}
        </span>
        <KTIcon icon-name="document" class="btn-icon fs-2" />
      </a>
    </div>
    <!--end::Footer-->
  </div>
  <!--end::Aside-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import { useI18n } from "vue-i18n";
import KTMenu from "@/layouts/main-layout/aside/Menu.vue";
import { asideTheme } from "@/core/helpers/config";

export default defineComponent({
  name: "KTAside",
  components: {
    KTMenu,
  },
  props: {
    lightLogo: String,
    darkLogo: String,
  },
  setup() {
    const { t } = useI18n();

    return {
      asideTheme,
      t,
      getAssetPath,
    };
  },
});
</script>
