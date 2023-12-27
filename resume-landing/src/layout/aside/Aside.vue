<template>
  <!--begin::Aside-->
<div>hh</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, onUpdated } from "vue";
import { useI18n } from "vue-i18n";
import { ToggleComponent } from "@/assets/ts/components/_ToggleComponent";
import KTMenu from "@/layout/aside/Menu.vue";
import { asideTheme } from "@/core/helpers/config";

export default defineComponent({
  name: "KTAside",
  components: {
    // KTMenu,
  },
  props: {
    lightLogo: String,
    darkLogo: String,
  },
  setup() {
    const { t } = useI18n();

    onMounted(() => {
      ToggleComponent.reinitialization();
    });

    onUpdated(() => {
      ToggleComponent.bootstrap();
    });

    return {
      asideTheme,
      t,
    };
  },
});
</script>
