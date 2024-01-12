import { ref } from "vue";
import { defineStore } from "pinia";
import ApiService from "@/core/services/ApiService";
import JwtService from "@/core/services/JwtService";
import supabase from "@/core/services/supabase";

export interface User {
  id: string;
  name: string;
  full_name: string;
  surname: string;
  email: string;
  password: string;
  pro?: string;
  api_token: string;
  profile_url?: string;
  disabled: false;
  stripe_customer_id: string;
  stripe_subscription_id: string;
  stripe_subscription_status: string;
  stripe_subscription_current_period_start: number;
  stripe_subscription_current_period_end: number;
  stripe_subscription_cancel_at_period_end: boolean;
}

export const useAuthStore = defineStore("auth", () => {
  const errors = ref({});
  const user = ref<User>({} as User);
  const isAuthenticated = ref(!!JwtService.getToken());

  function setAuth(authUser: User) {
    const name = authUser.name ?? authUser.email?.split("@")[0];
    authUser.profile_url = `https://ui-avatars.com/api/?name=${name}&background=0D8ABC&color=fff`;
    isAuthenticated.value = true;
    user.value = authUser;
    errors.value = {};
    JwtService.saveToken(user.value.api_token);
  }

  function setError(error: any) {
    errors.value = { ...error };
  }

  function purgeAuth() {
    isAuthenticated.value = false;
    user.value = {} as User;
    errors.value = [];
    JwtService.destroyToken();
  }

  function logout() {
    supabase.auth.signOut().catch(console.error);
    purgeAuth();
  }

  return {
    errors,
    user,
    isAuthenticated,
    logout,
    setAuth,
  };
});
