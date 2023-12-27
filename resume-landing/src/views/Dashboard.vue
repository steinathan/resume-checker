<template>
  <div
    id="kt_body"
    data-bs-spy="scroll"
    data-bs-target="#kt_landing_menu"
    data-bs-offset="200"
    class="bg-white position-relative"
  >
    <div class="d-flex flex-column flex-root">
      <!-- second  how it works-->
      <div class="mb-n10 mb-lg-n20 z-index-2">
        <HowItWorks />
      </div>

      <!--end::How It Works Section-->
      <!--begin::Statistics Section-->
      <div class="mt-sm-n10">
        <ThingsBetter />
      </div>

      <!--  -->
      <div class="py-10 py-lg-20">
        <OurTeam />
        <!--end::Container-->
      </div>

      <!--end::Team Section-->
      <!--begin::Projects Section-->
      <div class="mb-lg-n15 position-relative z-index-2">
        <!--begin::Container-->
        <OurProject />
        <!--end::Container-->
      </div>

      <!--end::Projects Section-->
      <!--begin::Pricing Section-->

      <!--end::Projects Section-->
      <!--begin::Pricing Section-->
      <div class="mt-sm-n20">
        <Pricing />
      </div>
      <!--end::Pricing Section-->
      <!--begin::Testimonials Section-->

      <div class="mt-20 mb-n20 position-relative z-index-2">
        <!--begin::Container-->
        <Testimonies />
        <!--end::Container-->
      </div>
      <!--end::Testimonials Section-->
      <!--begin::Footer Section-->
    </div>
    <!-- footer -->
  </div>
</template>

<script setup lang="ts">
import HowItWorks from "../components/HowItWorks.vue";
import ThingsBetter from "../components/ThingsBetter.vue";
import OurTeam from "../components/OurTeam.vue";
import OurProject from "../components/OurProject.vue";
import Pricing from "../components/Pricing.vue";
import Testimonies from "../components/Testimonies.vue";
</script>
