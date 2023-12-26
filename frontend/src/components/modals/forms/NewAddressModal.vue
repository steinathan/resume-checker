<template>
  <!--begin::Modal - New Address-->
  <div
    class="modal fade"
    ref="newAddressModalRef"
    id="kt_modal_new_address"
    tabindex="-1"
    aria-hidden="true"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-650px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Form-->
        <VForm
          class="form"
          id="kt_modal_new_address_form"
          @submit="submit"
          :validation-schema="validationSchema"
          v-slot="{ errors }"
        >
          <!--begin::Modal header-->
          <div class="modal-header" id="kt_modal_new_address_header">
            <!--begin::Modal title-->
            <h2>Add New Address</h2>
            <!--end::Modal title-->

            <!--begin::Close-->
            <div
              class="btn btn-sm btn-icon btn-active-color-primary"
              data-bs-dismiss="modal"
            >
              <KTIcon icon-name="cross" icon-class="fs-1" />
            </div>
            <!--end::Close-->
          </div>
          <!--end::Modal header-->

          <!--begin::Modal body-->
          <div class="modal-body py-10 px-lg-17">
            <!--begin::Scroll-->
            <div
              class="scroll-y me-n7 pe-7"
              id="kt_modal_new_address_scroll"
              data-kt-scroll="true"
              data-kt-scroll-activate="{default: false, lg: true}"
              data-kt-scroll-max-height="auto"
              data-kt-scroll-dependencies="#kt_modal_new_address_header"
              data-kt-scroll-wrappers="#kt_modal_new_address_scroll"
              data-kt-scroll-offset="300px"
            >
              <!--begin::Notice-->
              <div
                class="notice d-flex bg-light-warning rounded border-warning border border-dashed mb-9 p-6"
              >
                <KTIcon
                  icon-name="information-5"
                  icon-class="fs-2tx text-warning me-4"
                />
                <!--begin::Wrapper-->
                <div class="d-flex flex-stack flex-grow-1">
                  <!--begin::Content-->
                  <div class="fw-semobold">
                    <h4 class="text-gray-800 fw-bold">Warning</h4>
                    <div class="fs-6 text-gray-600">
                      Updating address may affter to your
                      <a href="#">Tax Location</a>
                    </div>
                  </div>
                  <!--end::Content-->
                </div>
                <!--end::Wrapper-->
              </div>
              <!--end::Notice-->

              <!--begin::Input group-->
              <div class="row mb-5">
                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--begin::Label-->
                  <label class="required fs-5 fw-semobold mb-2"
                    >First name</label
                  >
                  <!--end::Label-->

                  <!--begin::Input-->
                  <Field
                    type="text"
                    class="form-control"
                    :class="errors.firstName ? 'is-invalid' : ''"
                    placeholder=""
                    name="firstName"
                    v-model="newAddressData.firstName"
                  />
                  <ErrorMessage class="invalid-feedback" name="firstName" />
                  <!--end::Input-->
                </div>
                <!--end::Col-->

                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--end::Label-->
                  <label class="required fs-5 fw-semobold mb-2"
                    >Last name</label
                  >
                  <!--end::Label-->

                  <!--end::Input-->
                  <Field
                    type="text"
                    class="form-control"
                    :class="errors.lastName ? 'is-invalid' : ''"
                    placeholder=""
                    name="lastName"
                    v-model="newAddressData.lastName"
                  />
                  <ErrorMessage class="invalid-feedback" name="lastName" />
                  <!--end::Input-->
                </div>
                <!--end::Col-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="d-flex flex-column mb-5 fv-row">
                <!--begin::Label-->
                <label class="d-flex align-items-center fs-5 fw-semobold mb-2">
                  <span class="required">Country</span>
                  <i
                    class="fas fa-exclamation-circle ms-2 fs-7"
                    data-bs-toggle="tooltip"
                    title="Your payment statements may very based on selected country"
                  ></i>
                </label>
                <!--end::Label-->

                <!--begin::Select-->
                <Field
                  name="country"
                  class="form-select"
                  :class="errors.country ? 'is-invalid' : ''"
                  as="select"
                  v-model="newAddressData.country"
                >
                  <option value="">Select a Country...</option>
                  <option
                    v-for="(item, i) in countries"
                    :key="`countries-select-option-${i}`"
                    :value="item.code"
                  >
                    {{ item.name }}
                  </option>
                </Field>

                <ErrorMessage class="invalid-feedback" name="country" />
                <!--end::Select-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="d-flex flex-column mb-5 fv-row">
                <!--begin::Label-->
                <label class="required fs-5 fw-semobold mb-2"
                  >Address Line 1</label
                >
                <!--end::Label-->

                <!--begin::Input-->
                <Field
                  class="form-control"
                  :class="errors.address1 ? 'is-invalid' : ''"
                  placeholder=""
                  name="address1"
                  v-model="newAddressData.address1"
                />
                <ErrorMessage class="invalid-feedback" name="address1" />
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="d-flex flex-column mb-5 fv-row">
                <!--begin::Label-->
                <label class="required fs-5 fw-semobold mb-2"
                  >Address Line 2</label
                >
                <!--end::Label-->

                <!--begin::Input-->
                <Field
                  class="form-control"
                  :class="errors.address2 ? 'is-invalid' : ''"
                  placeholder=""
                  name="address2"
                  v-model="newAddressData.address2"
                />
                <ErrorMessage class="invalid-feedback" name="address2" />
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="d-flex flex-column mb-5 fv-row">
                <!--begin::Label-->
                <label class="fs-5 fw-semobold mb-2">Town</label>
                <!--end::Label-->

                <!--begin::Input-->
                <Field
                  class="form-control"
                  :class="errors.town ? 'is-invalid' : ''"
                  placeholder=""
                  name="town"
                  v-model="newAddressData.town"
                />
                <ErrorMessage class="invalid-feedback" name="town" />
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="row g-9 mb-5">
                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--begin::Label-->
                  <label class="fs-5 fw-semobold mb-2">State / Province</label>
                  <!--end::Label-->

                  <!--begin::Input-->
                  <Field
                    class="form-control"
                    :class="errors.state ? 'is-invalid' : ''"
                    placeholder=""
                    name="state"
                    v-model="newAddressData.state"
                  />
                  <ErrorMessage class="invalid-feedback" name="state" />
                  <!--end::Input-->
                </div>
                <!--end::Col-->

                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--begin::Label-->
                  <label class="fs-5 fw-semobold mb-2">Post Code</label>
                  <!--end::Label-->

                  <!--begin::Input-->
                  <Field
                    class="form-control"
                    :class="errors.postCode ? 'is-invalid' : ''"
                    placeholder=""
                    name="postCode"
                    v-model="newAddressData.postCode"
                  />
                  <ErrorMessage class="invalid-feedback" name="postCode" />
                  <!--end::Input-->
                </div>
                <!--end::Col-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-5">
                <!--begin::Wrapper-->
                <div class="d-flex flex-stack">
                  <!--begin::Label-->
                  <div class="me-5">
                    <!--begin::Label-->
                    <label class="fs-5 fw-semobold"
                      >Use as a billing adderess?</label
                    >
                    <!--end::Label-->

                    <!--begin::Input-->
                    <div class="fs-7 fw-semobold text-gray-400">
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
                    <Field
                      class="form-check-input"
                      :class="errors.postCode ? 'is-invalid' : ''"
                      name="billing"
                      type="checkbox"
                      value="1"
                      checked
                    />
                    <ErrorMessage class="invalid-feedback" name="billing" />
                    <!--end::Input-->

                    <!--begin::Label-->
                    <span class="form-check-label fw-semobold text-gray-400">
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
            <!--end::Scroll-->
          </div>
          <!--end::Modal body-->

          <!--begin::Modal footer-->
          <div class="modal-footer flex-center">
            <!--begin::Button-->
            <button
              type="reset"
              id="kt_modal_new_address_cancel"
              class="btn btn-light me-3"
            >
              Discard
            </button>
            <!--end::Button-->

            <!--begin::Button-->
            <button
              ref="submitButtonRef"
              type="submit"
              id="kt_modal_new_address_submit"
              class="btn btn-primary"
            >
              <span class="indicator-label"> Submit </span>
              <span class="indicator-progress">
                Please wait...
                <span
                  class="spinner-border spinner-border-sm align-middle ms-2"
                ></span>
              </span>
            </button>
            <!--end::Button-->
          </div>
          <!--end::Modal footer-->
        </VForm>
        <!--end::Form-->
      </div>
    </div>
  </div>
  <!--end::Modal - New Address-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, ref } from "vue";
import { ErrorMessage, Field, Form as VForm } from "vee-validate";
import { hideModal } from "@/core/helpers/dom";
import Swal from "sweetalert2/dist/sweetalert2.js";
import * as Yup from "yup";
import { countries } from "@/core/data/countries";

interface NewAddressData {
  firstName: string;
  lastName: string;
  country: string;
  address1: string;
  address2: string;
  town: string;
  state: string;
  postCode: string;
}

export default defineComponent({
  name: "new-address-modal",
  components: {
    ErrorMessage,
    Field,
    VForm,
  },
  setup() {
    const submitButtonRef = ref<null | HTMLButtonElement>(null);
    const newAddressModalRef = ref<null | HTMLElement>(null);

    const newAddressData = ref<NewAddressData>({
      firstName: "",
      lastName: "",
      country: "",
      address1: "",
      address2: "",
      town: "",
      state: "",
      postCode: "",
    });

    const validationSchema = Yup.object().shape({
      firstName: Yup.string().required().label("First name"),
      lastName: Yup.string().required().label("Last name"),
      country: Yup.string().required().label("Country"),
      address1: Yup.string().required().label("Address Line 1"),
      address2: Yup.string().required().label("Address Line 2"),
      town: Yup.string().required().label("Town"),
      state: Yup.string().required().label("State/Province"),
      postCode: Yup.string().required().label("Post code"),
    });

    const submit = () => {
      if (!submitButtonRef.value) {
        return;
      }

      //Disable button
      submitButtonRef.value.disabled = true;
      // Activate indicator
      submitButtonRef.value.setAttribute("data-kt-indicator", "on");

      setTimeout(() => {
        if (submitButtonRef.value) {
          submitButtonRef.value.disabled = false;

          submitButtonRef.value?.removeAttribute("data-kt-indicator");
        }

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
          hideModal(newAddressModalRef.value);
        });
      }, 2000);
    };

    return {
      newAddressData,
      validationSchema,
      submit,
      submitButtonRef,
      newAddressModalRef,
      getAssetPath,
      countries,
    };
  },
});
</script>
