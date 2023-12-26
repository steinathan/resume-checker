<template>
  <!--begin::Step 5-->
  <div data-kt-stepper-element="content">
    <div class="w-100 text-center">
      <!--begin::Heading-->
      <h1 class="fw-bold text-dark mb-3">Release!</h1>
      <!--end::Heading-->

      <!--begin::Description-->
      <div class="text-muted fw-semobold fs-3">
        Submit your app to kickstart your project.
      </div>
      <!--end::Description-->

      <!--begin::Illustration-->
      <div class="text-center px-4 py-15">
        <img
          :src="getIllustrationsPath('9.png')"
          alt=""
          class="mw-100 mh-300px"
        />
      </div>
      <!--end::Illustration-->
    </div>
  </div>
  <!--end::Step 5-->
</template>

<script setup lang="ts">
import { getIllustrationsPath } from "@/core/helpers/assets";
</script>
