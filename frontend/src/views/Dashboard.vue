<template>
  <div class="row mb-10">
    <div class="col-4">
      <div class="card-xl-stretch mb-xl-8 bg-primary card hoverable">
        <div class="card-body">
          <i class="ki-duotone ki-element-11 text-white fs-3x mx-n1"
            ><span class="path1"></span><span class="path2"></span
            ><span class="path3"></span><span class="path4"></span
          ></i>
          <div class="text-inverse-primary fw-bold fs-2 mb-2 mt-5">0</div>
          <div class="text-inverse-primary fw-semibold fs-7">
            Total Resume Scans
          </div>
        </div>
      </div>
      <!--      <MixedWidget7 chart-color="primary" chart-height="150"></MixedWidget7>-->
    </div>

    <div class="col-4">
      <div class="card-xl-stretch mb-xl-8 bg-dark card hoverable">
        <div class="card-body">
          <i class="ki-duotone ki-plus text-gray-100 fs-3x mx-n1"><!----></i>
          <div class="text-inverse-dark fw-bold fs-2 mb-2 mt-5">0</div>
          <div class="text-inverse-dark fw-semibold fs-7">Improvements</div>
        </div>
      </div>
      <!--      <MixedWidget10 chart-color="primary" chart-height="150"></MixedWidget10>-->
    </div>
    <div class="col-4">
      <div class="card-xl-stretch mb-xl-8 bg-info card hoverable">
        <div class="card-body">
          <i class="ki-duotone ki-chart-pie-simple text-white fs-3x mx-n1"
            ><span class="path1"></span><span class="path2"></span
          ></i>
          <div class="text-inverse-info fw-bold fs-2 mb-2 mt-5">0/10</div>
          <div class="text-inverse-info fw-semibold fs-7">
            Resume Score Rating
          </div>
        </div>
      </div>
    </div>
  </div>

  <Resumes class="card-xxl-stretch mb-10 mb-xl-8"></Resumes>
  <JobMatchers class="card-xxl-stretch mb-5 mb-xxl-8"></JobMatchers>
  <!--end::Dashboard-->
</template>

<script lang="ts" setup>
import Resumes from "@/components/widgets/tables/ResumeList.vue";
import JobMatchers from "@/components/widgets/tables/Widget5.vue";
import MixedWidget7 from "@/components/widgets/mixed/Widget7.vue";
import MixedWidget10 from "@/components/widgets/mixed/Widget10.vue";
</script>
