<template>
  <!--begin::Stat-->
  <div
    class="border border-gray-300 border-dashed rounded min-w-125px py-3 px-4 me-6 mb-3"
  >
    <!--begin::Number-->
    <div class="d-flex align-items-center">
      <KTIcon
        v-if="score < 6"
        icon-name="arrow-down"
        icon-class="fs-3 text-danger me-2"
      />
      <KTIcon v-else icon-name="arrow-up" icon-class="fs-3 text-success me-2" />
      <div
        class="fs-2 fw-bold"
        data-kt-countup="true"
        :data-kt-countup-value="score"
      >
        {{ score }}/10
      </div>
    </div>
    <!--end::Number-->

    <!--begin::Label-->
    <div class="fw-semobold fs-6 text-gray-400">{{ title }}</div>
    <!--end::Label-->
  </div>
  <!--end::Stat-->
</template>

<script setup lang="ts">
import KTIcon from "@/core/helpers/kt-icon/KTIcon.vue";

defineProps({
  title: String,
  score: Number,
});
</script>
