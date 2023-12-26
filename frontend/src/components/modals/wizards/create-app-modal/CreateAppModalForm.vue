<template>
  <!--begin::Form-->
  <form class="form" id="kt_modal_create_app_form" @submit="handleStep">
    <CreateAppStep1></CreateAppStep1>
    <CreateAppStep2></CreateAppStep2>
    <CreateAppStep3></CreateAppStep3>
    <CreateAppStep4></CreateAppStep4>
    <CreateAppStep5></CreateAppStep5>

    <!--begin::Actions-->
    <div class="d-flex flex-stack pt-10">
      <!--begin::Wrapper-->
      <div class="me-2">
        <button
          type="button"
          class="btn btn-lg btn-light-primary me-3"
          data-kt-stepper-action="previous"
          @click="previousStep()"
        >
          <KTIcon icon-name="arrow-left" icon-class="fs-3 me-1" />
          Back
        </button>
      </div>
      <!--end::Wrapper-->

      <!--begin::Wrapper-->
      <div>
        <button
          type="submit"
          class="btn btn-lg btn-primary"
          v-if="currentStepIndex === totalSteps - 1"
          @click="formSubmit()"
        >
          <span class="indicator-label">
            Submit
            <KTIcon icon-name="arrow-right" icon-class="fs-3 ms-2 me-0" />
          </span>
          <span class="indicator-progress">
            Please wait...
            <span
              class="spinner-border spinner-border-sm align-middle ms-2"
            ></span>
          </span>
        </button>

        <button v-else type="submit" class="btn btn-lg btn-primary">
          Continue
          <KTIcon icon-name="arrow-right" icon-class="fs-3 ms-1 me-0" />
        </button>
      </div>
      <!--end::Wrapper-->
    </div>
    <!--end::Actions-->
  </form>
  <!--end::Form-->
</template>

<script setup lang="ts">
import { computed, nextTick, onMounted, ref } from "vue";

import Swal from "sweetalert2/dist/sweetalert2.js";
import { useForm } from "vee-validate";
import * as Yup from "yup";
import { StepperComponent } from "@/assets/ts/components";
import type {
  ICreateApp,
  IStep1,
  IStep2,
  IStep3,
  IStep4,
} from "@/components/modals/wizards/create-app-modal/types";
import CreateAppStep1 from "@/components/modals/wizards/create-app-modal/steps/CreateAppStep1.vue";
import CreateAppStep2 from "@/components/modals/wizards/create-app-modal/steps/CreateAppStep2.vue";
import CreateAppStep3 from "@/components/modals/wizards/create-app-modal/steps/CreateAppStep3.vue";
import CreateAppStep4 from "@/components/modals/wizards/create-app-modal/steps/CreateAppStep4.vue";
import CreateAppStep5 from "@/components/modals/wizards/create-app-modal/steps/CreateAppStep5.vue";

interface Props {
  stepperEl: HTMLElement | null;
}

const props = defineProps<Props>();

const currentStepIndex = ref(0);
const stepperObj = ref<StepperComponent | null>(null);

onMounted(() => {
  nextTick(() => {
    if (props.stepperEl) {
      stepperObj.value = StepperComponent.createInsance(props.stepperEl);
    }
  });
});

const formData = ref<ICreateApp>({
  appName: "",
  category: "1",
  framework: "1",
  dbName: "",
  dbType: "1",
  nameOnCard: "Max Doe",
  cardNumber: "4111 1111 1111 1111",
  cardExpiryMonth: "1",
  cardExpiryYear: "2",
  cardCvv: "123",
  saveCard: "1",
});

const formInitData = ref<ICreateApp>(formData.value);

const createAppSchema = [
  Yup.object({
    appName: Yup.string().required().label("App name"),
    category: Yup.string().required().label("Category"),
  }),
  Yup.object({
    framework: Yup.string().required().label("Framework"),
  }),
  Yup.object({
    dbName: Yup.string().required().label("Database name"),
    dbType: Yup.string().required().label("Database engine"),
  }),
  Yup.object({
    nameOnCard: Yup.string().required().label("Name"),
    cardNumber: Yup.string().required().label("Card Number"),
    cardExpiryMonth: Yup.string().required().label("Expiration Month"),
    cardExpiryYear: Yup.string().required().label("Expiration Year"),
    cardCvv: Yup.string().required().label("CVV"),
  }),
];

// extracts the individual step schema
const currentSchema = computed(() => {
  return createAppSchema[currentStepIndex.value];
});

const totalSteps = computed(() => {
  if (stepperObj.value) {
    return stepperObj.value.totalStepsNumber;
  } else {
    return 1;
  }
});

const { resetForm, handleSubmit } = useForm<IStep1 | IStep2 | IStep3 | IStep4>({
  validationSchema: currentSchema,
  initialValues: formData.value,
});

const previousStep = () => {
  currentStepIndex.value--;

  if (!stepperObj.value) {
    return;
  }

  stepperObj.value.goPrev();
};

const handleStep = handleSubmit((values) => {
  console.log(values);

  formData.value = {
    ...formData.value,
    ...values,
  };

  resetForm({
    values: {
      ...formData.value,
    },
  });

  currentStepIndex.value++;

  if (!stepperObj.value) {
    return;
  }

  stepperObj.value.goNext();
});

const formSubmit = () => {
  Swal.fire({
    text: "All is cool! Now you submit this form",
    icon: "success",
    buttonsStyling: false,
    confirmButtonText: "Ok, got it!",
    heightAuto: false,
    customClass: {
      confirmButton: "btn fw-semobold btn-light-primary",
    },
  }).then(() => {
    stepperObj.value?.goFirst();
    currentStepIndex.value = 0;

    resetForm({
      values: {
        ...formInitData.value,
      },
    });
  });
};
</script>
