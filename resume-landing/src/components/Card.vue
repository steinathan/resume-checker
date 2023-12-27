<template>
  <div class="card card-custom gutter-b" :class="classes">
    <div class="card-header" :class="headClass" v-if="hasTitleSlot || title">
      <div class="card-title">
        <slot name="title" v-if="hasTitleSlot"></slot>
        <h3 class="card-label" v-if="!hasTitleSlot">
          {{ title }}
        </h3>
      </div>
      <div class="card-toolbar">
        <slot name="toolbar"></slot>
      </div>
    </div>
    <div
      class="card-body"
      :class="{
        bodyClass,
        'body-fit': bodyFit,
        'body-fluid': bodyFluid,
      }"
    >
      <slot name="body"></slot>
    </div>
    <div class="card-footer" v-if="hasFootSlot">
      <slot name="foot"></slot>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "KTCard",
  components: {},
  props: {
    /**
     * String title
     */
    title: String,
    /**
     * Set card head size. Eg. md, lg, sm, etc.
     */
    headSize: String,
    /**
     * Set card to fluid
     */
    fluidHeight: Boolean,
    /**
     * Set card to fluid in half
     */
    fluidHalfHeight: Boolean,
    /**
     * Set overlay head
     */
    headOverlay: Boolean,
    /**
     * Set extra class for main card
     */
    cardClass: String,
    /**
     * Set extra class for card head
     */
    headClass: String,
    /**
     * Set extra class for card body
     */
    bodyClass: String,
    /**
     * Set card body to fit
     */
    bodyFit: Boolean,
    /**
     * Set card body to fluid
     */
    bodyFluid: Boolean,
    /**
     * Code examples
     */
    example: Boolean,
  },
  setup() {
    const classes = () => {
      const cls = {
        "example example-compact": this.example,
        "height-fluid": this.fluidHeight,
        "height-fluid-half": this.fluidHalfHeight,
        "head-overlay": this.headOverlay,
      };

      cls[this.headSizeClass] = this.headSizeClass;

      // append extra classes
      if (this.cardClass) {
        cls[this.cardClass] = true;
      }

      return cls;
    };
    const hasTitleSlot = () => {
      return !!this.$slots["title"];
    };
    const hasFootSlot = () => {
      return !!this.$slots["foot"];
    };
    const headSizeClass = () => {
      if (this.headSize) {
        return `head-${this.headSize}`;
      }
      return false;
    };

    return {
      classes,
      hasTitleSlot,
      hasFootSlot,
      headSizeClass,
    };
  },
});
</script>
