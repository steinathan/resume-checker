<template>
  <div class="mt-10">
    <Pricing @select="handlePriceSelect" hide-background />
  </div>
</template>

<script lang="ts" setup>
import { loadStripe } from "@stripe/stripe-js";
import Pricing from "@/components/home/Pricing.vue";
import { useAuthStore } from "@/stores/auth";
import { storeToRefs } from "pinia";

const authStore = useAuthStore();
const { user } = storeToRefs(authStore);

const key = import.meta.env.VITE_APP_STRIPE_PUB_KEY;
const stripePromise = loadStripe(key);

function handlePriceSelect(val) {
  const params = {
    user_id: user.value.id,
    email_address: user.value.email,
    plan_name: val,
  };
  redirectToCheckout(params);
}

const baseURL = import.meta.env.VITE_APP_API_URL;
const redirectToCheckout = async (params: Record<string, string> = {}) => {
  const stripe = await stripePromise;

  const response = await fetch(`${baseURL}/stripe/get-checkout-url`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(params),
  });

  const session = await response.json();

  // Redirect the user to the hosted checkout page
  const result = await stripe!.redirectToCheckout({
    sessionId: session.id,
  });

  if (result.error) {
    console.error(result.error.message);
  }
};
</script>

<style>
/* Your component styles go here */
</style>
