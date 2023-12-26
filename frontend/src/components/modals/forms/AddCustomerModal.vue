<template>
  <div
    class="modal fade"
    id="kt_modal_add_customer"
    ref="addCustomerModalRef"
    tabindex="-1"
    aria-hidden="true"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-650px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Modal header-->
        <div class="modal-header" id="kt_modal_add_customer_header">
          <!--begin::Modal title-->
          <h2 class="fw-bold">Add a Customer</h2>
          <!--end::Modal title-->

          <!--begin::Close-->
          <div
            id="kt_modal_add_customer_close"
            data-bs-dismiss="modal"
            class="btn btn-icon btn-sm btn-active-icon-primary"
          >
            <KTIcon icon-name="cross" icon-class="fs-1" />
          </div>
          <!--end::Close-->
        </div>
        <!--end::Modal header-->
        <!--begin::Form-->
        <el-form
          @submit.prevent="submit()"
          :model="formData"
          :rules="rules"
          ref="formRef"
        >
          <!--begin::Modal body-->
          <div class="modal-body py-10 px-lg-17">
            <!--begin::Scroll-->
            <div
              class="scroll-y me-n7 pe-7"
              id="kt_modal_add_customer_scroll"
              data-kt-scroll="true"
              data-kt-scroll-activate="{default: false, lg: true}"
              data-kt-scroll-max-height="auto"
              data-kt-scroll-dependencies="#kt_modal_add_customer_header"
              data-kt-scroll-wrappers="#kt_modal_add_customer_scroll"
              data-kt-scroll-offset="300px"
            >
              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="required fs-6 fw-semobold mb-2">Name</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="name">
                  <el-input
                    v-model="formData.name"
                    type="text"
                    placeholder=""
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">
                  <span class="required">Email</span>

                  <i
                    class="fas fa-exclamation-circle ms-1 fs-7"
                    data-bs-toggle="tooltip"
                    title="Email address must be active"
                  ></i>
                </label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="email">
                  <el-input v-model="formData.email" />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-15">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Description</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="description">
                  <el-input v-model="formData.description" type="text" />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Billing toggle-->
              <div
                class="fw-bold fs-3 rotate collapsible mb-7"
                data-bs-toggle="collapse"
                href="#kt_modal_add_customer_billing_info"
                role="button"
                aria-expanded="false"
                aria-controls="kt_customer_view_details"
              >
                Shipping Information
                <span class="ms-2 rotate-180">
                  <KTIcon icon-name="down" icon-class="fs-3" />
                </span>
              </div>
              <!--end::Billing toggle-->

              <!--begin::Billing form-->
              <div
                id="kt_modal_add_customer_billing_info"
                class="collapse show"
              >
                <!--begin::Input group-->
                <div class="d-flex flex-column mb-7 fv-row">
                  <!--begin::Label-->
                  <label class="required fs-6 fw-semobold mb-2"
                    >Address Line 1</label
                  >
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-form-item prop="addressLine">
                    <el-input v-model="formData.addressLine" />
                  </el-form-item>
                  <!--end::Input-->
                </div>
                <!--end::Input group-->

                <!--begin::Input group-->
                <div class="d-flex flex-column mb-7 fv-row">
                  <!--begin::Label-->
                  <label class="fs-6 fw-semobold mb-2">Address Line 2</label>
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-input v-model="formData.addressLine2" />
                  <!--end::Input-->
                </div>
                <!--end::Input group-->

                <!--begin::Input group-->
                <div class="d-flex flex-column mb-7 fv-row">
                  <!--begin::Label-->
                  <label class="required fs-6 fw-semobold mb-2">Town</label>
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-form-item prop="town">
                    <el-input v-model="formData.town" />
                  </el-form-item>
                  <!--end::Input-->
                </div>
                <!--end::Input group-->

                <!--begin::Input group-->
                <div class="row g-9 mb-7">
                  <!--begin::Col-->
                  <div class="col-md-6 fv-row">
                    <!--begin::Label-->
                    <label class="required fs-6 fw-semobold mb-2"
                      >State / Province</label
                    >
                    <!--end::Label-->

                    <!--begin::Input-->
                    <el-form-item prop="state">
                      <el-input v-model="formData.state" />
                    </el-form-item>
                    <!--end::Input-->
                  </div>
                  <!--end::Col-->

                  <!--begin::Col-->
                  <div class="col-md-6 fv-row">
                    <!--begin::Label-->
                    <label class="required fs-6 fw-semobold mb-2"
                      >Post Code</label
                    >
                    <!--end::Label-->

                    <!--begin::Input-->
                    <el-form-item prop="postCode">
                      <el-input v-model="formData.postCode" />
                    </el-form-item>
                    <!--end::Input-->
                  </div>
                  <!--end::Col-->
                </div>
                <!--end::Input group-->

                <!--begin::Input group-->
                <div class="d-flex flex-column mb-7 fv-row">
                  <!--begin::Label-->
                  <label class="fs-6 fw-semobold mb-2">
                    <span class="required">Country</span>

                    <i
                      class="fas fa-exclamation-circle ms-1 fs-7"
                      data-bs-toggle="tooltip"
                      title="Country of origination"
                    ></i>
                  </label>
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-select v-model="formData.country">
                    <el-option value="">Select a Country...</el-option>
                    <el-option
                      v-for="(item, i) in countries"
                      :key="`countries-select-option-${i}`"
                      :value="item.code"
                    >
                      {{ item.name }}
                    </el-option>
                  </el-select>
                  <!--end::Input-->
                </div>
                <!--end::Input group-->

                <!--begin::Input group-->
                <div class="fv-row mb-7">
                  <!--begin::Wrapper-->
                  <div class="d-flex flex-stack">
                    <!--begin::Label-->
                    <div class="me-5">
                      <!--begin::Label-->
                      <label class="fs-6 fw-semobold"
                        >Use as a billing adderess?</label
                      >
                      <!--end::Label-->

                      <!--begin::Input-->
                      <div class="fs-7 fw-semobold text-muted">
                        If you need more info, please check budget planning
                      </div>
                      <!--end::Input-->
                    </div>
                    <!--end::Label-->

                    <!--begin::Switch-->
                    <label
                      class="form-check form-switch form-check-custom form-check-solid"
                    >
                      <!--begin::Input-->
                      <input
                        class="form-check-input"
                        name="billing"
                        type="checkbox"
                        value="1"
                        id="kt_modal_add_customer_billing"
                        checked
                      />
                      <!--end::Input-->

                      <!--begin::Label-->
                      <span
                        class="form-check-label fw-semobold text-muted"
                        for="kt_modal_add_customer_billing"
                      >
                        Yes
                      </span>
                      <!--end::Label-->
                    </label>
                    <!--end::Switch-->
                  </div>
                  <!--begin::Wrapper-->
                </div>
                <!--end::Input group-->
              </div>
              <!--end::Billing form-->
            </div>
            <!--end::Scroll-->
          </div>
          <!--end::Modal body-->

          <!--begin::Modal footer-->
          <div class="modal-footer flex-center">
            <!--begin::Button-->
            <button
              type="reset"
              id="kt_modal_add_customer_cancel"
              class="btn btn-light me-3"
            >
              Discard
            </button>
            <!--end::Button-->

            <!--begin::Button-->
            <button
              :data-kt-indicator="loading ? 'on' : null"
              class="btn btn-lg btn-primary"
              type="submit"
            >
              <span v-if="!loading" class="indicator-label">
                Submit
                <KTIcon icon-name="arrow-right" icon-class="fs-2 me-2 me-0" />
              </span>
              <span v-if="loading" class="indicator-progress">
                Please wait...
                <span
                  class="spinner-border spinner-border-sm align-middle ms-2"
                ></span>
              </span>
            </button>
            <!--end::Button-->
          </div>
          <!--end::Modal footer-->
        </el-form>
        <!--end::Form-->
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, ref } from "vue";
import { hideModal } from "@/core/helpers/dom";
import { countries } from "@/core/data/countries";
import Swal from "sweetalert2/dist/sweetalert2.js";

export default defineComponent({
  name: "add-customer-modal",
  components: {},
  setup() {
    const formRef = ref<null | HTMLFormElement>(null);
    const addCustomerModalRef = ref<null | HTMLElement>(null);
    const loading = ref<boolean>(false);
    const formData = ref({
      name: "Sean Bean",
      email: "sean@dellito.com",
      description: "",
      addressLine: "101, Collins Street",
      addressLine2: "",
      town: "Melbourne",
      state: "Victoria",
      postCode: "3000",
      country: "US",
    });

    const rules = ref({
      name: [
        {
          required: true,
          message: "Customer name is required",
          trigger: "change",
        },
      ],
      email: [
        {
          required: true,
          message: "Customer email is required",
          trigger: "change",
        },
      ],
      addressLine: [
        {
          required: true,
          message: "Address 1 is required",
          trigger: "change",
        },
      ],
      town: [
        {
          required: true,
          message: "Town is required",
          trigger: "change",
        },
      ],
      state: [
        {
          required: true,
          message: "State is required",
          trigger: "change",
        },
      ],
      postCode: [
        {
          required: true,
          message: "Post code is required",
          trigger: "change",
        },
      ],
    });

    const submit = () => {
      if (!formRef.value) {
        return;
      }

      formRef.value.validate((valid: boolean) => {
        if (valid) {
          loading.value = true;

          setTimeout(() => {
            loading.value = false;

            Swal.fire({
              text: "Form has been successfully submitted!",
              icon: "success",
              buttonsStyling: false,
              confirmButtonText: "Ok, got it!",
              heightAuto: false,
              customClass: {
                confirmButton: "btn btn-primary",
              },
            }).then(() => {
              hideModal(addCustomerModalRef.value);
            });
          }, 2000);
        } else {
          Swal.fire({
            text: "Sorry, looks like there are some errors detected, please try again.",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Ok, got it!",
            heightAuto: false,
            customClass: {
              confirmButton: "btn btn-primary",
            },
          });
          return false;
        }
      });
    };

    return {
      formData,
      rules,
      submit,
      formRef,
      loading,
      addCustomerModalRef,
      getAssetPath,
      countries,
    };
  },
});
</script>
