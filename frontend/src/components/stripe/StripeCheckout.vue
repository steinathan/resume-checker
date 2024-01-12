<template>
  <div>
    <button @click="redirectToCheckout">Subscribe</button>
  </div>
</template>

<script lang="ts" setup>
import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe(
  "pk_test_51OWqHeBSae2LEN6sWpGyrocTqNDU0EshPTznV6EtlqP2Ee88pxcx9GXUBNzfQNfmteI9fx1tHlLjsseP7EYrO3i300rpRNKh8r"
);

const baseURL = import.meta.env.VITE_APP_API_URL;
const redirectToCheckout = async () => {
  const stripe = await stripePromise;

  // Fetch your backend endpoint to create a Checkout Session
  const response = await fetch(`${baseURL}/get-session`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    // You can pass additional data to your server here
    body: JSON.stringify({}),
  });

  const session = await response.json();

  // Redirect the user to the hosted checkout page
  const result = await stripe!.redirectToCheckout({
    sessionId: session.id,
  });

  if (result.error) {
    // Handle any errors that occurred during the redirect
    console.error(result.error.message);
  }
};
</script>

<style>
/* Your component styles go here */
</style>
