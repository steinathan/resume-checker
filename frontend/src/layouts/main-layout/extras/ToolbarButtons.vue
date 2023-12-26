<template>
  <div
    class="engage-toolbar d-flex position-fixed px-5 fw-bold zindex-2 top-50 end-0 transform-90 mt-20 gap-2"
  >
    <!--begin::Help drawer toggle-->
    <button
      id="kt_help_toggle"
      class="engage-help-toggle btn btn-flex h-35px bg-body btn-color-gray-700 btn-active-color-gray-900 shadow-sm px-5 rounded-top-0"
      title="Learn & Get Inspired"
      data-bs-toggle="tooltip"
      data-bs-placement="left"
      data-bs-dismiss="click"
      data-bs-trigger="hover"
    >
      Help
    </button>
    <!--end::Help drawer toggle-->

    <!--begin::Purchase link-->
    <a
      href="https://1.envato.market/EA4JP"
      target="_blank"
      class="engage-purchase-link btn btn-flex h-35px bg-body btn-color-gray-700 btn-active-color-gray-900 px-5 shadow-sm rounded-top-0"
    >
      Buy Now
    </a>
    <!--end::Purchase link-->
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "kt-toolbar-buttons",
  components: {},
});
</script>
