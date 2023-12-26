<template>
  <!--begin::Dashboard-->
  <div class="row mb-10">
    <div class="col-6">
      <MixedWidget7 chart-color="primary" chart-height="150"></MixedWidget7>
    </div>

    <div class="col-6">
      <MixedWidget10 chart-color="primary" chart-height="150"></MixedWidget10>
    </div>
  </div>

  <Resumes widget-classes="card-xxl-stretch mb-5 mb-xl-8"></Resumes>

  <JobMatchers widget-classes="card-xxl-stretch mb-5 mb-xxl-8"></JobMatchers>
  <!--end::Dashboard-->
</template>

<script lang="ts" setup>
import Resumes from "@/components/widgets/tables/ResumeList.vue";
import JobMatchers from "@/components/widgets/tables/Widget5.vue";
import MixedWidget7 from "@/components/widgets/mixed/Widget7.vue";
import MixedWidget10 from "@/components/widgets/mixed/Widget10.vue";
</script>
