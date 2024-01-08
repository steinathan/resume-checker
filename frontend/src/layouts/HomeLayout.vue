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
</script>