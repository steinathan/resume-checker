<template>
  <!-- begin:: Body -->
  <div class="page d-flex flex-row flex-column-fluid">
    <div id="kt_wrapper" class="wrapper d-flex flex-column flex-row-fluid">
      <KTHeader />

      <!-- begin:: Content Head -->
      <KTToolbar v-if="subheaderDisplay" />
      <!-- end:: Content Head -->

      <!-- begin:: Content -->
      <div
        id="kt_content"
        class="d-flex flex-column-fluid align-items-start"
        :class="{
          'container-fluid': contentWidthFluid,
          'container-xxl': !contentWidthFluid,
        }"
      >
        <!-- begin:: Aside Left -->
        <KTAside
          v-if="asideEnabled"
          :lightLogo="themeLightLogo"
          :darkLogo="themeDarkLogo"
        />
        <!-- end:: Aside Left -->
        <!-- begin:: Content Body -->
        <div class="content flex-row-fluid">
          <RouterView />
        </div>
        <!-- end:: Content Body -->
      </div>
      <!-- end:: Content -->
      <KTFooter />
    </div>
  </div>
  <!-- end:: Body -->
  <KTScrollTop />
  <UploadResume />
  <ScanJobModdal />
</template>

<script lang="ts">
import {
  defineComponent,
  nextTick,
  onBeforeMount,
  onMounted,
  watch,
} from "vue";
import { RouterView, useRoute } from "vue-router";
import KTAside from "@/layouts/main-layout/aside/Aside.vue";
import KTHeader from "@/layouts/main-layout/header/Header.vue";
import KTFooter from "@/layouts/main-layout/footer/Footer.vue";
import LayoutService from "@/core/services/LayoutService";
import KTToolbar from "@/layouts/main-layout/toolbar/Toolbar.vue";
import KTScrollTop from "@/layouts/main-layout/extras/ScrollTop.vue";
import { reinitializeComponents } from "@/core/plugins/keenthemes";
import {
  asideEnabled,
  contentWidthFluid,
  loaderEnabled,
  loaderLogo,
  subheaderDisplay,
  themeDarkLogo,
  themeLightLogo,
  toolbarDisplay,
} from "@/core/helpers/config";
import supabase from "@/core/services/supabase";
import type { User } from "@/stores/auth";
import { useAuthStore } from "@/stores/auth";
import UploadResume from "@/components/UploadResume.vue";
import ScanJobModdal from "@/components/ScanJobModdal.vue";
import axios from "@/core/services/ApiService2";
import { runPostLogin } from "@/core/services/hooks";

export default defineComponent({
  name: "master-layout",
  components: {
    ScanJobModdal,
    UploadResume,
    RouterView,
    KTAside,
    KTHeader,
    KTFooter,
    KTToolbar,
    KTScrollTop,
  },
  setup() {
    const route = useRoute();

    onBeforeMount(() => {
      LayoutService.init();
    });

    const authStore = useAuthStore();

    onMounted(async () => {
      await runPostLogin();
      nextTick(() => {
        reinitializeComponents();
      });
    });

    watch(
      () => route.path,
      () => {
        nextTick(() => {
          reinitializeComponents();
        });
      }
    );

    return {
      toolbarDisplay,
      loaderEnabled,
      contentWidthFluid,
      loaderLogo,
      asideEnabled,
      subheaderDisplay,
      themeLightLogo,
      themeDarkLogo,
    };
  },
});
</script>
