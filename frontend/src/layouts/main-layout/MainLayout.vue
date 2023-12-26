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
  <KTMessengerDrawer />
  <KTActivityDrawer />
  <KTCreateApp />
  <KTInviteFriendsModal />

  <KTToolbarButtons />
  <KTHelpDrawer />
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
import KTActivityDrawer from "@/layouts/main-layout/drawers/ActivityDrawer.vue";
import KTCreateApp from "@/components/modals/wizards/create-app-modal/CreateAppModal.vue";
import KTInviteFriendsModal from "@/components/modals/general/InviteFriendsModal.vue";
import KTToolbarButtons from "@/layouts/main-layout/extras/ToolbarButtons.vue";
import KTHelpDrawer from "@/layouts/main-layout/extras/HelpDrawer.vue";
import KTMessengerDrawer from "@/layouts/main-layout/extras/MessengerDrawer.vue";
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

export default defineComponent({
  name: "master-layout",
  components: {
    RouterView,
    KTAside,
    KTHeader,
    KTFooter,
    KTToolbar,
    KTScrollTop,
    KTCreateApp,
    KTInviteFriendsModal,
    KTActivityDrawer,
    KTToolbarButtons,
    KTHelpDrawer,
    KTMessengerDrawer,
  },
  setup() {
    const route = useRoute();

    onBeforeMount(() => {
      LayoutService.init();
    });

    onMounted(() => {
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
