<template>
  <!--begin::Timeline item-->
  <div class="timeline-item">
    <!--begin::Timeline line-->
    <div class="timeline-line w-40px"></div>
    <!--end::Timeline line-->

    <!--begin::Timeline icon-->
    <div class="timeline-icon symbol symbol-circle symbol-40px">
      <div class="symbol-label bg-light">
        <KTIcon icon-name="pencil" icon-class="fs-2 text-gray-500" />
      </div>
    </div>
    <!--end::Timeline icon-->

    <!--begin::Timeline content-->
    <div class="timeline-content mb-10 mt-n1">
      <!--begin::Timeline heading-->
      <div class="pe-3 mb-5">
        <!--begin::Title-->
        <div class="fs-5 fw-semobold mb-2">
          3 new application design concepts added:
        </div>
        <!--end::Title-->

        <!--begin::Description-->
        <div class="d-flex align-items-center mt-1 fs-6">
          <!--begin::Info-->
          <div class="text-muted me-2 fs-7">Created at 4:23 PM by</div>
          <!--end::Info-->

          <!--begin::User-->
          <div
            class="symbol symbol-circle symbol-25px"
            data-bs-toggle="tooltip"
            data-bs-boundary="window"
            data-bs-placement="top"
            title="Marcus Dotson"
          >
            <img :src="getAssetPath('media/avatars/300-2.jpg')" alt="img" />
          </div>
          <!--end::User-->
        </div>
        <!--end::Description-->
      </div>
      <!--end::Timeline heading-->

      <!--begin::Timeline details-->
      <div class="overflow-auto pb-5">
        <div
          class="d-flex align-items-center border border-dashed border-gray-300 rounded min-w-700px p-7"
        >
          <!--begin::Item-->
          <div class="overlay me-10">
            <!--begin::Image-->
            <div class="overlay-wrapper">
              <img
                alt="img"
                class="rounded w-150px"
                :src="getAssetPath('media/stock/600x400/img-29.jpg')"
              />
            </div>
            <!--end::Image-->
            <!--begin::Link-->
            <div class="overlay-layer bg-dark bg-opacity-10 rounded">
              <a href="#" class="btn btn-sm btn-primary btn-shadow">Explore</a>
            </div>
            <!--end::Link-->
          </div>
          <!--end::Item-->
          <!--begin::Item-->
          <div class="overlay me-10">
            <!--begin::Image-->
            <div class="overlay-wrapper">
              <img
                alt="img"
                class="rounded w-150px"
                :src="getAssetPath('media/stock/600x400/img-31.jpg')"
              />
            </div>
            <!--end::Image-->
            <!--begin::Link-->
            <div class="overlay-layer bg-dark bg-opacity-10 rounded">
              <a href="#" class="btn btn-sm btn-primary btn-shadow">Explore</a>
            </div>
            <!--end::Link-->
          </div>
          <!--end::Item-->
          <!--begin::Item-->
          <div class="overlay">
            <!--begin::Image-->
            <div class="overlay-wrapper">
              <img
                alt="img"
                class="rounded w-150px"
                :src="getAssetPath('media/stock/600x400/img-40.jpg')"
              />
            </div>
            <!--end::Image-->
            <!--begin::Link-->
            <div class="overlay-layer bg-dark bg-opacity-10 rounded">
              <a href="#" class="btn btn-sm btn-primary btn-shadow">Explore</a>
            </div>
            <!--end::Link-->
          </div>
          <!--end::Item-->
        </div>
      </div>
      <!--end::Timeline details-->
    </div>
    <!--end::Timeline content-->
  </div>
  <!--end::Timeline item-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";

export default defineComponent({
  name: "item-5",
  components: {},
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
