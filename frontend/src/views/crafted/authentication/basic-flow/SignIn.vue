<template>
  <!--begin::Wrapper-->
  <div class="w-lg-500px p-10">
    <!--begin::Form-->
    <VForm class="form w-100" id="kt_login_signin_form">
      <!--begin::Heading-->
      <div class="text-center mb-10">
        <!--begin::Title-->
        <h1 class="text-dark mb-3">Sign In</h1>
        <!--end::Title-->

        <!--begin::Link-->
        <div class="text-gray-400 fw-semobold fs-4">
          We'll create an account if you're new else we'll log you in
        </div>
        <!--end::Link-->
      </div>
      <!--begin::Heading-->

      <!--      <div class="mb-10 bg-light-info p-8 rounded">-->
      <!--        <div class="text-info">-->
      <!--          Use account <strong>admin@demo.com</strong> and password-->
      <!--          <strong>demo</strong> to continue.-->
      <!--        </div>-->
      <!--      </div>-->

      <!--      &lt;!&ndash;begin::Input group&ndash;&gt;-->
      <!--      <div class="fv-row mb-10">-->
      <!--        &lt;!&ndash;begin::Label&ndash;&gt;-->
      <!--        <label class="form-label fs-6 fw-bold text-dark">Email</label>-->
      <!--        &lt;!&ndash;end::Label&ndash;&gt;-->

      <!--        &lt;!&ndash;begin::Input&ndash;&gt;-->
      <!--        <Field-->
      <!--            tabindex="1"-->
      <!--            class="form-control form-control-lg form-control-solid"-->
      <!--            type="text"-->
      <!--            name="email"-->
      <!--            autocomplete="off"-->
      <!--        />-->
      <!--        &lt;!&ndash;end::Input&ndash;&gt;-->
      <!--        <div class="fv-plugins-message-container">-->
      <!--          <div class="fv-help-block">-->
      <!--            <ErrorMessage name="email"/>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--      &lt;!&ndash;end::Input group&ndash;&gt;-->

      <!--      &lt;!&ndash;begin::Input group&ndash;&gt;-->
      <!--      <div class="fv-row mb-10">-->
      <!--        &lt;!&ndash;begin::Wrapper&ndash;&gt;-->
      <!--        <div class="d-flex flex-stack mb-2">-->
      <!--          &lt;!&ndash;begin::Label&ndash;&gt;-->
      <!--          <label class="form-label fw-bold text-dark fs-6 mb-0">Password</label>-->
      <!--          &lt;!&ndash;end::Label&ndash;&gt;-->

      <!--          &lt;!&ndash;begin::Link&ndash;&gt;-->
      <!--          <router-link to="/password-reset" class="link-primary fs-6 fw-bold">-->
      <!--            Forgot Password ?-->
      <!--          </router-link>-->
      <!--          &lt;!&ndash;end::Link&ndash;&gt;-->
      <!--        </div>-->
      <!--        &lt;!&ndash;end::Wrapper&ndash;&gt;-->

      <!--        &lt;!&ndash;begin::Input&ndash;&gt;-->
      <!--        <Field-->
      <!--            tabindex="2"-->
      <!--            class="form-control form-control-lg form-control-solid"-->
      <!--            type="password"-->
      <!--            name="password"-->
      <!--            autocomplete="off"-->
      <!--        />-->
      <!--        &lt;!&ndash;end::Input&ndash;&gt;-->
      <!--        <div class="fv-plugins-message-container">-->
      <!--          <div class="fv-help-block">-->
      <!--            <ErrorMessage name="password"/>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--      &lt;!&ndash;end::Input group&ndash;&gt;-->

      <!--begin::Actions-->
      <div class="text-center">
        <!--begin::Submit button-->
        <!--        <button-->
        <!--            tabindex="3"-->
        <!--            type="submit"-->
        <!--            ref="submitButton"-->
        <!--            id="kt_sign_in_submit"-->
        <!--            class="btn btn-lg btn-primary w-100 mb-5"-->
        <!--        >-->
        <!--          <span class="indicator-label"> Continue </span>-->

        <!--          <span class="indicator-progress">-->
        <!--            Please wait...-->
        <!--            <span-->
        <!--                class="spinner-border spinner-border-sm align-middle ms-2"-->
        <!--            ></span>-->
        <!--          </span>-->
        <!--        </button>-->
        <!--        &lt;!&ndash;end::Submit button&ndash;&gt;-->

        <!--begin::Separator-->
        <!--        <div class="text-center text-muted text-uppercase fw-bold mb-5">or</div>-->
        <!--end::Separator-->

        <!--begin::Google link-->
        <a
          href="#"
          @click="onGoogleClick"
          class="btn btn-flex flex-center btn-light btn-lg w-100 mb-5"
        >
          <img
            alt="Logo"
            :src="getAssetPath('media/svg/brand-logos/google-icon.svg')"
            class="h-20px me-3"
          />
          Continue with Google
        </a>
        <!--end::Google link-->

        <!--begin::Google link-->
        <!--        <a-->
        <!--            href="#"-->
        <!--            class="btn btn-flex flex-center btn-light btn-lg w-100 mb-5"-->
        <!--        >-->
        <!--          <img-->
        <!--              alt="Logo"-->
        <!--              :src="getAssetPath('media/svg/brand-logos/facebook-4.svg')"-->
        <!--              class="h-20px me-3"-->
        <!--          />-->
        <!--          Continue with Facebook-->
        <!--        </a>-->
        <!--end::Google link-->

        <!--begin::Google link-->
        <!--        <a href="#" class="btn btn-flex flex-center btn-light btn-lg w-100">-->
        <!--          <img-->
        <!--              alt="Logo"-->
        <!--              :src="getAssetPath('media/svg/brand-logos/apple-black.svg')"-->
        <!--              class="h-20px me-3"-->
        <!--          />-->
        <!--          Continue with Apple-->
        <!--        </a>-->
        <!--end::Google link-->
      </div>
      <!--end::Actions-->
    </VForm>
    <!--end::Form-->
  </div>
  <!--end::Wrapper-->
</template>

<script lang="ts" setup>
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted, ref } from "vue";
import { ErrorMessage, Field, Form as VForm } from "vee-validate";
import { useAuthStore, type User } from "@/stores/auth";
import { useRouter } from "vue-router";
import Swal from "sweetalert2/dist/sweetalert2.js";
import * as Yup from "yup";
import supabase from "@/core/services/supabase";

const store = useAuthStore();
const router = useRouter();
const submitButton = ref<HTMLButtonElement | null>(null);

//Create form validation object
const login = Yup.object().shape({
  email: Yup.string().email().required().label("Email"),
  password: Yup.string().min(4).required().label("Password"),
});

const onGoogleClick = () => {
  supabase.auth.signInWithOAuth({
    provider: "google",
    options: {
      queryParams: {
        redirectTo: `${window.location.origin}/sign-in`,
        access_type: "offline",
        prompt: "consent",
      },
    },
  });
};

onMounted(async () => {
  const { data } = await supabase.auth.getUser();

  if (data && data.user) {
    const { data: sessionData, error } = await supabase.auth.getSession();
    const { session } = sessionData;
    // @ts-ignore
    data.user.api_token = session?.access_token;
    store.setAuth(data.user as unknown as User);
    window.location.replace(window.location.origin + "/dashboard");
  } else {
    console.warn("user not logged in");
  }
});
</script>
