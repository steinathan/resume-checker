<template>
  <Notice
    v-if="!coverLetter"
    classes="rounded-3 my-5"
    color="warning"
    title="No cover letter was generated"
    body="Cover letter wasn't generated because the resume didnt reach a minimum score threshold for the job"
  ></Notice>

  <div class="card" v-else>
    <div class="card-body">
      <div class="card-title mb-5 d-flex justify-content-between">
        <div class="m-0">
          <h4 class="card-title fw-bolder text-hover-primary fs-2">
            Cover Letter
          </h4>
          <p class="fw-semibold fs-4 text-gray-600 mb-2">
            Here is an auto generated cover letter that you can utilize when
            applying for this position.
          </p>
        </div>
      </div>
      <div>
        <textarea
          class="form-control form-control-lg form-control-solid"
          name="document"
          rows="20"
          v-model="text"
          type="text"
        />
      </div>
      <div class="card-footer justify-content-end d-flex">
        <button
          class="btn btn-light-primary copy-btn"
          title="copy to clipboard"
        >
          <i class="fas fa-copy fs-1"></i> Copy
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { useResumeStore } from "@/stores/resume";
import { onMounted, ref } from "vue";
import Clipboard from "clipboard";
import Notice from "@/components/Notice.vue";

const resumeStore = useResumeStore();

const { coverLetter } = storeToRefs(resumeStore);

const text = ref<string>("");

onMounted(() => {
  text.value = coverLetter.value?.text;
});
function copyToClipboardWithNewlines(text) {
  // Use the Clipboard API to write text to the clipboard
  navigator.clipboard
    .writeText(text)
    .then(() => {
      console.log("Text copied to clipboard successfully");
    })
    .catch((err) => {
      console.error("Unable to copy text to clipboard", err);
    });
}
const platformDependentNewline = navigator.platform
  .toLowerCase()
  .startsWith("win")
  ? "\r\n"
  : "\n";
const textToCopyWithPlatformNewlines = text.value.replace(
  /\n/g,
  platformDependentNewline
);

function copyToClipboard() {
  copyToClipboardWithNewlines(textToCopyWithPlatformNewlines);
}
</script>
