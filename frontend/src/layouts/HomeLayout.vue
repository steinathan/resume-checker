<template>
  <div class="d-flex flex-column flex-root" id="kt_app_root">
    <HomeHeader />
    <router-view />
    <HomeFooter />
  </div>
</template>
<script setup lang="ts">
import HomeHeader from "@/components/home/HomeHeader.vue";
import HomeFooter from "@/components/home/HomeFooter.vue";
import { onMounted } from "vue";
import supabase from "@/core/services/supabase";
import { useAuthStore, type User } from "@/stores/auth";
const store = useAuthStore();

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
