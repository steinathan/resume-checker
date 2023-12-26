<template>
  <div :class="className">
    <!--begin::Body-->
    <div
      class="card-body d-flex flex-column justify-content-between mt-9 bgi-no-repeat bgi-size-cover bgi-position-x-center pb-0"
    >
      <!--begin::Wrapper-->
      <div class="mb-10">
        <!--begin::Title-->
        <div class="fs-2hx text-gray-800 text-center mb-13">
          <span class="me-2 fw-bold"> {{ title }} </span>
          <div class="text-muted fs-5">
            {{ description }}
          </div>
        </div>
        <!--end::Title-->

        <!--begin::Action-->
        <div v-if="type === 'resume'" class="text-center">
          <button
            data-bs-toggle="modal"
            data-bs-target="#upload_resume_modal"
            class="btn btn-sm btn-dark fw-bold"
          >
            Upload new resume
          </button>
        </div>

        <div v-if="type === 'job_scan'" class="text-center">
          <button
            class="btn btn-sm btn-dark fw-bold"
            data-bs-toggle="modal"
            data-bs-target="#new-collection-modal"
            title="scan new job"
          >
            Scan new Job
          </button>
          <!--begin::Action-->
        </div>
      </div>
      <!--begin::Wrapper-->

      <!--begin::Illustration-->
      <img
        class="mx-auto h-150px h-lg-200px theme-light-show"
        :src="getAssetPath('media/illustrations/unitedpalms-1/13.png')"
        alt=""
      />
      <img
        class="mx-auto h-150px h-lg-200px theme-dark-show"
        :src="getAssetPath('media/illustrations/unitedpalms-1/13-dark.svg')"
        alt=""
      />
      <!--end::Illustration-->
    </div>
    <!--end::Body-->
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";

export default defineComponent({
  name: "EmptyState",
  components: {},
  props: {
    className: { type: String, required: false },
    title: { type: String, required: false },
    description: { type: String, required: false },
    type: { type: String, required: true },
  },
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
