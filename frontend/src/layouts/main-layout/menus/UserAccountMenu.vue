<template>
  <!--begin::Menu-->
  <div
    class="menu menu-sub menu-sub-dropdown menu-column menu-rounded menu-gray-600 menu-state-bg-light-primary fw-semobold py-4 fs-6 w-275px"
    data-kt-menu="true"
  >
    <!--begin::Menu item-->
    <div class="menu-item px-3">
      <div class="menu-content d-flex align-items-center px-3">
        <!--begin::Avatar-->
        <div class="symbol symbol-50px me-5">
          <img alt="Logo" :src="user.profile_url" />
        </div>
        <!--end::Avatar-->

        <!--begin::Username-->
        <div class="d-flex flex-column">
          <div class="fw-bold d-flex align-items-center fs-5">
            {{ user.name || user.email?.split("@")[0] }}

            <span
              v-if="user.pro"
              class="badge badge-light-success fw-bold fs-8 px-2 py-1 ms-2"
              >Pro</span
            >
          </div>
          <a href="#" class="fw-semobold text-muted text-hover-primary fs-7">{{
            user.email
          }}</a>
        </div>
        <!--end::Username-->
      </div>
    </div>
    <!--end::Menu item-->

    <!--begin::Menu separator-->
    <div class="separator my-2"></div>
    <!--end::Menu separator-->

    <!--    &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--    <div class="menu-item px-5">-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        My Profile-->
    <!--      </router-link>-->
    <!--    </div>-->
    <!--    &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--    &lt;!&ndash;begin::Menu item&ndash;&gt;-->
    <!--    <div class="menu-item px-5">-->
    <!--      <router-link to="/pages/profile/overview" class="menu-link px-5">-->
    <!--        <span class="menu-text">My Resumes</span>-->
    <!--        <span class="menu-badge">-->
    <!--          <span class="badge badge-light-danger badge-circle fw-bold fs-7"-->
    <!--            >3</span-->
    <!--          >-->
    <!--        </span>-->
    <!--      </router-link>-->
    <!--    </div>-->
    <!--    &lt;!&ndash;end::Menu item&ndash;&gt;-->

    <!--begin::Menu item-->
    <div class="menu-item px-5 my-1">
      <router-link to="/pages/profile/overview" class="menu-link px-5">
        Profile Settings
      </router-link>
    </div>
    <!--end::Menu item-->

    <!--begin::Menu item-->
    <div class="menu-item px-5">
      <a @click="signOut()" class="menu-link px-5"> Sign Out </a>
    </div>
    <!--end::Menu item-->
  </div>
  <!--end::Menu-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { computed, defineComponent } from "vue";
import { useI18n } from "vue-i18n";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";

export default defineComponent({
  name: "kt-user-menu",
  components: {},
  setup() {
    const router = useRouter();
    const i18n = useI18n();

    const authStore = useAuthStore();
    const { user } = storeToRefs(authStore);

    i18n.locale.value = localStorage.getItem("lang")
      ? (localStorage.getItem("lang") as string)
      : "en";

    const countries = {
      en: {
        flag: getAssetPath("media/flags/united-states.svg"),
        name: "English",
      },
      es: {
        flag: getAssetPath("media/flags/spain.svg"),
        name: "Spanish",
      },
    };

    const signOut = () => {
      authStore.logout();
      router.push({ name: "sign-in" });
    };

    const setLang = (lang: string) => {
      localStorage.setItem("lang", lang);
      i18n.locale.value = lang;
    };

    const currentLanguage = computed(() => {
      return i18n.locale.value;
    });

    const currentLangugeLocale = computed(() => {
      return countries[i18n.locale.value as keyof typeof countries];
    });

    return {
      signOut,
      setLang,
      currentLanguage,
      user,
      currentLangugeLocale,
      countries,
      getAssetPath,
    };
  },
});
</script>
