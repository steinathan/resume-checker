<template>
  <!-- begin::Scrolltop -->
  <div
    v-if="scrolltopDispaly"
    id="kt_scrolltop"
    ref="kt_scrolltop"
    class="scrolltop"
    data-kt-scrolltop="true"
  >
    <KTIcon icon-name="arrow-up" icon-class="fs-2x" />
  </div>
  <!-- end::Scrolltop -->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted } from "vue";
import { ScrollTopComponent } from "@/assets/ts/components/_ScrollTopComponent";
import { scrolltopDispaly } from "@/core/helpers/config";

export default defineComponent({
  name: "KTScrollTop",
  components: {},
  setup() {
    onMounted(() => {
      ScrollTopComponent.reinitialization();
    });

    return {
      scrolltopDispaly,
      getAssetPath,
    };
  },
});
</script>
