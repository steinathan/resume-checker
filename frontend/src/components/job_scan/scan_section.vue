<script setup lang="ts">
import Notice from "@/components/Notice.vue";
import { getColorCodeByPercentage } from "@/core/helpers/color";

defineProps({
  title: String,
  explanation: String,
  suggestion: String,
  issues: Array<String>,
  checked: Boolean,
  hideChecked: Boolean,
  score: Number,
  done: Array<String>,
});
</script>

<template>
  <div class="card my-10">
    <div class="card-body">
      <div class="mb-3">
        <a href="#" class="card-title fw-bolder text-hover-primary fs-2">
          {{ title }}
        </a>
        <span
          class="float-end section-score"
          :style="`color:${getColorCodeByPercentage(score * 10)}`"
          >{{ score }}</span
        >
      </div>
      <span class="float-end text-gray-800 text-hover-primary fs-1 me-1">
        <i
          v-if="!hideChecked"
          class="fa"
          :class="[
            checked
              ? 'fa-check-circle text-success'
              : 'fa-xmark-circle text-danger',
          ]"
          style="font-size: xx-large"
        ></i>
      </span>

      <!--  issues  -->
      <div class="mb-3 fs-4 me-1" v-if="issues && issues.length === 0">
        <i class="fas fa-check-circle text-success fs-2"></i>
        Great job
      </div>
      <ul>
        <li class="mb-3 fs-4 me-1" v-for="(li, i) in issues" :key="i">
          <i class="fas fa-circle-exclamation text-danger fs-2"></i>
          {{ li }}
        </li>
      </ul>

      <!--  done  -->
      <ul>
        <li class="mb-3 fs-4 me-1" v-for="(li, i) in done" :key="i">
          <i class="fas fa-check-circle text-success fs-2"></i>
          {{ li }}
        </li>
      </ul>

      <!-- explanation -->
      <p class="fs-5 m-0">
        {{ explanation }}
      </p>
      <Notice
        v-if="suggestion"
        classes="rounded-3 mt-5"
        color="warning"
        title="Suggestion"
        :body="suggestion"
      ></Notice>
    </div>
  </div>
</template>

<style scoped lang="scss">
.section-score {
  font-weight: bolder;
  font-size: 40px;
}
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
