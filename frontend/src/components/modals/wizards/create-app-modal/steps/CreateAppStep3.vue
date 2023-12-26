<template>
  <!--begin::Step 3-->
  <div data-kt-stepper-element="content">
    <div class="w-100">
      <!--begin::Input group-->
      <div class="fv-row mb-10">
        <!--begin::Label-->
        <label class="required fs-5 fw-semobold mb-2"> Database Name </label>
        <!--end::Label-->

        <!--begin::Input-->
        <Field
          type="text"
          class="form-control form-control-lg form-control-solid"
          name="dbName"
          placeholder=""
        />
        <ErrorMessage
          class="fv-plugins-message-container invalid-feedback"
          name="dbName"
        />
        <!--end::Input-->
      </div>
      <!--end::Input group-->

      <!--begin::Input group-->
      <div class="fv-row">
        <!--begin::Label-->
        <label class="d-flex align-items-center fs-5 fw-semobold mb-4">
          <span class="required">Select Database Engine</span>

          <i
            class="fas fa-exclamation-circle ms-2 fs-7"
            v-tooltip
            title="Select your app database engine"
          ></i>
        </label>
        <!--end::Label-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer mb-5">
          <!--begin::Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin::Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-success">
                <i class="fas fa-database text-success fs-2x"></i>
              </span>
            </span>
            <!--end::Icon-->

            <!--begin::Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">MySQL</span>

              <span class="fs-7 text-muted">Basic MySQL database</span>
            </span>
            <!--end::Info-->
          </span>
          <!--end::Label-->

          <!--begin::Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="dbType"
              value="1"
            />
          </span>
          <!--end::Input-->
        </label>
        <!--end::Option-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer mb-5">
          <!--begin::Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin::Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-danger">
                <i class="fab fa-google text-danger fs-2x"></i>
              </span>
            </span>
            <!--end::Icon-->

            <!--begin::Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">Firebase</span>

              <span class="fs-7 text-muted"
                >Google based app data management</span
              >
            </span>
            <!--end::Info-->
          </span>
          <!--end::Label-->

          <!--begin::Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="dbType"
              value="2"
            />
          </span>
          <!--end::Input-->
        </label>
        <!--end::Option-->

        <!--begin:Option-->
        <label class="d-flex flex-stack cursor-pointer">
          <!--begin::Label-->
          <span class="d-flex align-items-center me-2">
            <!--begin::Icon-->
            <span class="symbol symbol-50px me-6">
              <span class="symbol-label bg-light-warning">
                <i class="fab fa-amazon text-warning fs-2x"></i>
              </span>
            </span>
            <!--end::Icon-->

            <!--begin::Info-->
            <span class="d-flex flex-column">
              <span class="fw-bold fs-6">DynamoDB</span>

              <span class="fs-7 text-muted">Amazon Fast NoSQL Database</span>
            </span>
            <!--end::Info-->
          </span>
          <!--end::Label-->

          <!--begin::Input-->
          <span class="form-check form-check-custom form-check-solid">
            <Field
              class="form-check-input"
              type="radio"
              name="dbType"
              value="3"
            />
          </span>
          <!--end::Input-->
        </label>
        <!--end::Option-->

        <ErrorMessage
          class="fv-plugins-message-container invalid-feedback"
          name="dbType"
        />
      </div>
      <!--end::Input group-->
    </div>
  </div>
  <!--end::Step 3-->
</template>

<script setup lang="ts">
import { ErrorMessage, Field } from "vee-validate";
</script>
