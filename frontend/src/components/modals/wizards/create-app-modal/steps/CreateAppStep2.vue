<template>
  <!--begin::Step 2-->
  <div data-kt-stepper-element="content">
    <div class="w-100">
      <!--begin::Input group-->
      <div class="fv-row">
        <!--begin::Label-->
        <label class="d-flex align-items-center fs-5 fw-semobold mb-4">
          <span class="required">Select Framework</span>
          <i
            class="fas fa-exclamation-circle ms-2 fs-7"
            v-tooltip
            title="Specify your apps framework"
          ></i>
        </label>
        <!--end::Label-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer mb-5">
          <!--begin:Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin:Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-warning">
                <i class="fab fa-html5 text-warning fs-2x"></i>
              </span>
            </span>
            <!--end:Icon-->

            <!--begin:Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">HTML5</span>

              <span class="fs-7 text-muted">Base Web Projec</span>
            </span>
            <!--end:Info-->
          </span>
          <!--end:Label-->

          <!--begin:Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="framework"
              value="1"
            />
          </span>
          <!--end:Input-->
        </label>
        <!--end::Option-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer mb-5">
          <!--begin:Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin:Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-success">
                <i class="fab fa-react text-success fs-2x"></i>
              </span>
            </span>
            <!--end:Icon-->

            <!--begin:Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">ReactJS</span>
              <span class="fs-7 text-muted"
                >Robust and flexible app framework</span
              >
            </span>
            <!--end:Info-->
          </span>
          <!--end:Label-->

          <!--begin:Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="framework"
              value="2"
            />
          </span>
          <!--end:Input-->
        </label>
        <!--end::Option-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer mb-5">
          <!--begin:Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin:Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-danger">
                <i class="fab fa-angular text-danger fs-2x"></i>
              </span>
            </span>
            <!--end:Icon-->

            <!--begin:Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">Angular</span>
              <span class="fs-7 text-muted">Powerful data mangement</span>
            </span>
            <!--end:Info-->
          </span>
          <!--end:Label-->

          <!--begin:Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="framework"
              value="3"
            />
          </span>
          <!--end:Input-->
        </label>
        <!--end::Option-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer">
          <!--begin:Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin:Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-primary">
                <i class="fab fa-vuejs text-primary fs-2x"></i>
              </span>
            </span>
            <!--end:Icon-->

            <!--begin:Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">Vue</span>
              <span class="fs-7 text-muted"
                >Lightweight and responsive framework</span
              >
            </span>
            <!--end:Info-->
          </span>
          <!--end:Label-->

          <!--begin:Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="framework"
              value="4"
            />
          </span>
          <!--end:Input-->
        </label>
        <!--end::Option-->

        <ErrorMessage
          class="fv-plugins-message-container invalid-feedback"
          name="framework"
        />
      </div>
      <!--end::Input group-->
    </div>
  </div>
  <!--end::Step 2-->
</template>

<script setup lang="ts">
import { ErrorMessage, Field } from "vee-validate";
</script>
