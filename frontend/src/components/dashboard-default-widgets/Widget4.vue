<template>
  <div class="card card-flush" :class="className">
    <!--begin::Header-->
    <div class="card-header pt-5">
      <!--begin::Title-->
      <h3 class="card-title text-gray-800 fw-bold">External Links</h3>
      <!--end::Title-->
      <!--begin::Toolbar-->
      <div class="card-toolbar">
        <!--begin::Menu-->
        <button
          class="btn btn-icon btn-color-gray-400 btn-active-color-primary justify-content-end"
          data-kt-menu-trigger="click"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-overflow="true"
        >
          <KTIcon
            icon-name="dots-square"
            icon-class="fs-1 text-gray-300 me-n1"
          />
        </button>
        <Dropdown2 />
        <!--end::Menu-->
      </div>
      <!--end::Toolbar-->
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div class="card-body pt-5">
      <template v-for="(item, i) in items" :key="i">
        <!--begin::Item-->
        <div class="d-flex flex-stack">
          <!--begin::Section-->
          <a href="#" class="text-primary fw-semibold fs-6 me-2">{{
            item.description
          }}</a>
          <!--end::Section-->
          <!--begin::Action-->
          <button
            type="button"
            class="btn btn-icon btn-sm h-auto btn-color-gray-400 btn-active-color-primary justify-content-end"
          >
            <KTIcon icon-name="exit-right-corner" icon-class="fs-2" />
          </button>
          <!--end::Action-->
        </div>
        <!--end::Item-->

        <div
          v-if="items.length - 1 !== i"
          class="separator separator-dashed my-3"
        ></div>
      </template>
    </div>
    <!--end::Body-->
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import Dropdown2 from "@/components/dropdown/Dropdown2.vue";

export default defineComponent({
  name: "default-dashboard-widget-4",
  components: {
    Dropdown2,
  },
  props: {
    className: { type: String, required: false },
  },
  setup() {
    const items = [
      {
        description: "Avg. Client Rating",
        statistics: "7.8",
        inc: true,
        number: "true",
      },
      {
        description: "Instagram Followers",
        statistics: "730k",
        inc: false,
        number: "false",
      },
      {
        description: "Google Ads CPC",
        statistics: "$2.09",
        inc: true,
        number: "false",
      },
    ];

    return {
      items,
      getAssetPath,
    };
  },
});
</script>
