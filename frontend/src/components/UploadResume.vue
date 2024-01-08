<template>
  <div
    class="modal fade"
    id="upload_resume_modal"
    tabindex="-1"
    aria-hidden="false"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-900px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Modal header-->
        <div class="modal-header">
          <!--begin::Modal title-->
          <h2>Upload Resume</h2>
          <!--end::Modal title-->

          <!--begin::Close-->
          <div
            class="btn btn-sm btn-icon btn-active-color-primary"
            data-bs-dismiss="modal"
          >
            <KTIcon icon-name="cross" icon-class="fs-1" />
          </div>
          <!--end::Close-->
        </div>
        <!--end::Modal header-->

        <!--begin::Modal body-->
        <div class="modal-body py-lg-10 px-lg-10">
          <div class="d-flex justify-content-center">
            <!-- is uploading -->
            <div v-if="isUploading" class="col-6 w-50 text-center">
              <div
                class="spinner-border"
                role="status"
                style="width: 4rem; height: 4rem"
              >
                <span class="visually-hidden">Loading...</span>
              </div>
              <h1 class="fw-boldest mt-5">{{ uploadProgress }}%</h1>
              <p class="text-center fs-6 fw-boldest">
                {{ uploadMessage }}
              </p>
            </div>

            <!--begin::Dropzone-->
            <div v-else class="w-75 d-flex flex-column">
              <!-- Errors -->
              <Notice
                v-if="errMsg"
                classes="rounded-3"
                color="danger"
                title="Consistency Violation!"
                :body="errMsg"
              ></Notice>

              <!--              <div class="dropzone my-10" id="dropzone_file_section">-->
              <!--                <div class="dz-message needsclick">-->
              <!--                  <i class="ki-duotone ki-file-up fs-3x text-primary"-->
              <!--                  ><span class="path1"></span><span class="path2"></span-->
              <!--                  ></i>-->

              <!--                  <div class="ms-4">-->
              <!--                    <h3 class="fs-5 fw-bold text-gray-900 mb-1">-->
              <!--                      Drop your here or click to upload.-->
              <!--                    </h3>-->
              <!--                    <span class="fs-7 fw-semibold text-gray-400"-->
              <!--                    >PDF only</span-->
              <!--                    >-->
              <!--                  </div>-->
              <!--                </div>-->
              <!--              </div>-->

              <div class="my-10 dropzone">
                <label for="fileInput" class="dz-message needsclick">
                  <i class="ki-duotone ki-file-up fs-3x text-primary">
                    <span class="path1"></span><span class="path2"></span>
                  </i>

                  <div class="ms-4">
                    <h3 class="fs-5 fw-bold text-gray-900 mb-1">
                      Drop your file here or click to upload.
                    </h3>
                    <span class="fs-7 fw-semibold text-gray-400">PDF only</span>
                  </div>

                  <!-- Add a file input element -->
                  <input
                    type="file"
                    id="fileInput"
                    ref="fileInput"
                    style="display: none"
                    @change="handleFileUpload"
                  />
                </label>
                <div v-if="resumeFile" class="text-body fs-6">
                  {{ resumeFile.name }}
                </div>
              </div>

              <!--              <div class="text-center text-muted text-uppercase fw-bold mb-5">-->
              <!--                or-->
              <!--              </div>-->
              <!--              <div>-->
              <!--                <h3 class="my-5 fs-4 fw-boldest">-->
              <!--                  Enter any public file, webpage, or document URL-->
              <!--                </h3>-->
              <!--                <div class="my-3">-->
              <!--                  This URL should be accessible by someone not in your-->
              <!--                  organization and must end with a file extension-->
              <!--                </div>-->
              <!--                <input-->
              <!--                    class="form-control form-control-lg form-control-solid"-->
              <!--                    name="document"-->
              <!--                    placeholder="https://site.com/recording/example.mp4"-->
              <!--                    v-model="docURL"-->
              <!--                    type="text"-->
              <!--                />-->
              <!--              </div>-->
            </div>
          </div>

          <div
            class="card-footer d-flex align-items-end justify-content-between"
          >
            <div></div>
            <div>
              <button
                :disabled="!isValid || uploadLimitReached"
                @click="uploadFile"
                class="btn btn-primary"
              >
                Upload
              </button>
            </div>
          </div>
        </div>

        <!--end::Modal body-->
      </div>
      <!--end::Modal content-->
    </div>
    <!--end::Modal dialog-->
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { storeToRefs } from "pinia";
import { useRoute, useRouter } from "vue-router";
import { useLogger } from "vue-logger-plugin";
import Notice from "@/components/Notice.vue";
import { post } from "@/core/services/ApiService2";
import { hideModal } from "@/core/helpers/dom";
import Swal from "sweetalert2";
import { useAuthStore } from "@/stores/auth";
import supabase from "@/core/services/supabase";

const authStore = useAuthStore();
const { user } = storeToRefs(authStore);

const logger = useLogger();
const route = useRoute();
const router = useRouter();

const isUploading = ref(false);
const uploadProgress = ref(0);
const errMsg = ref<string>("");
const uploadMessage = ref("Do not close your browser tab");
const isValid = ref(false);

function clearStates() {
  isUploading.value = false;
  uploadProgress.value = 0;
}

function setError(msg: string) {
  errMsg.value = msg;
}

const uploadLimitReached = computed(() => {
  return user.value.limits?.reached === true;
});

const fileInput = ref<any>(null);
const resumeFile = ref<File | null>(null);

function NotifyUser() {
  Swal.fire({
    title: "Great, but Its not over yet!",
    text: "We're processing this document, but we'll let you know via mail about the status of this operation",
    icon: "success",
    allowOutsideClick: false,
    allowEscapeKey: false,
    buttonsStyling: false,
    confirmButtonText: "Ok, got it!",
    heightAuto: false,
    customClass: {
      confirmButton: "btn btn-primary",
    },
  }).then(() => {
    window.location.replace("/dashboard");
  });
}

const handleFileUpload = () => {
  const file = fileInput.value?.files?.[0];
  if (file) {
    isValid.value = true;
    resumeFile.value = file;
  }
};

async function uploadFile() {
  try {
    setError("");
    const BUCKET_NAME = "ai-resume";
    isUploading.value = true;
    logger.debug("starting upload:...");

    const uploadPath = `${user.value.id}/${resumeFile.value!.name}`;
    const { data, error } = await supabase.storage
      .from(BUCKET_NAME)
      .upload(uploadPath, resumeFile.value as File, {
        cacheControl: "3600",
        upsert: true,
      });

    if (error) {
      throw new Error(error.message);
    }

    if (data) {
      uploadProgress.value = 50;
      let { data: fileData } = supabase.storage
        .from(BUCKET_NAME)
        .getPublicUrl(data.path);

      const createResumeParams = {
        src: fileData.publicUrl,
        name: resumeFile.value!.name,
      };

      await post("/resume", createResumeParams);
      uploadProgress.value = 100;
      clearStates();
      NotifyUser();
      hideModal("#upload_resume_modal" as unknown as HTMLElement);
    }
  } catch (error: any) {
    setError(error?.message || "Sorry, an error occurred, try again?");
    uploadProgress.value = 0;
    isUploading.value = false;
  }
}
</script>

<style lang="scss">
.dropzone {
  background: transparent;
}

.dropzone .dz-preview .dz-remove {
  width: 30px;
  height: 30px;
}
</style>
