<template>
  <div class="modal fade" id="scan_job_modal" tabindex="-1" aria-hidden="false">
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-900px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Modal header-->
        <div class="modal-header">
          <!--begin::Modal title-->
          <h2>Scan a job</h2>
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
            <div v-if="isProcessing" class="col-6 w-50 text-center">
              <div
                class="spinner-border"
                role="status"
                style="width: 4rem; height: 4rem"
              >
                <span class="visually-hidden">Loading...</span>
              </div>
              <!--              <h1 class="fw-boldest mt-5">{{ uploadProgress }}%</h1>-->
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

              <div class="mt-5">
                <h3 class="fs-4 fw-boldest">Enter any public job URL</h3>
                <div class="my-3">
                  This URL should be accessible by someone not authenticated
                  with a credential
                </div>
                <input
                  class="form-control form-control-lg form-control-solid"
                  name="document"
                  placeholder="https://boards.greenhouse.io/remotecom/jobs/xxxxxxxxxxxx"
                  type="text"
                  v-model="jobURL"
                />
              </div>
              <div class="text-center text-muted text-uppercase fw-bold my-5">
                or
              </div>
              <!-- job description-->
              <div>
                <h3 class="fs-4 fw-boldest">Enter job description</h3>
                <textarea
                  class="form-control form-control-lg form-control-solid"
                  name="document"
                  rows="3"
                  v-model="jobDescription"
                  placeholder="Remote is solving global remote organizations’ biggest challenge: employing anyone anywhere compliantly. We make it possible for businesses big and small to employ a global team by handling global payroll, benefits, taxes, and compliance. Check out remote.com/how-it-works to learn more or if you’re interested in adding to the mission, scroll down to apply now.

Please take a look at remote.com/handbook to learn more about our culture and what it is like to work here. Not only do we encourage folks from all ethnic groups, genders, sexuality, age and abilities to apply, but we prioritize a sense of belonging. You can check out independent reviews by other candidates on Glassdoor or look up the results of our candidate surveys to see how others feel about working and interviewing here.

All of our positions are fully remote. You do not have to relocate to join us!

The position
This is an exciting time to join Remote and make a personal difference in the global employment space as a Senior Product Designer, joining our Design team.

Design is at the forefront of everything we do. A Senior Product Designer's job is to envision how people experience our products and bring that vision to life with a deep knowledge of working within a diverse team (design, engineering, and product management)—taking responsibility for the entire design process from initial research, ideation, conceptualization, and design, to testing and validation.

What this job can offer you
Take ownership of strategic design and user-experience decisions, and pioneer new functions and features that solve our user’s problems.
Join a close knit group inside Remote, serving a critical part of the product for our customers.
Work in a user-centered way, to discover, define, rapidly test and iterate your designs.
Work in cross-collaborative teams with product and engineering to implement new features and iteration - learning rapidly from seeing your work in the real world.
Join a supportive design practice where you will help further increase the design team’s level of ux maturity.
What you bring
An advanced level of product design experience. You effectively translate user needs and business goals into design solutions.
Preference will be given to candidates who have experience designing complex solutions for complete digital environments, fintech or HR tech experience is a big plus for this position.
An impressive portfolio showcasing a clear understanding of simplicity, typography, interaction design and UI design, displaying a deep understanding of the product design process
Proven experience of advocacy for the customer and applying UX methodologies including user research and insights to your design.
Strong understanding and appreciation of the practice of design iteration - you will always be experimenting, evaluating and learning. You approach problems from multiple perspectives to get the best solution.
A systematic approach to creating and maintaining our design system - exceptional communication skills to explain the rationales behind decisions clearly and concisely
Practicals
You'll report to: Product Design Director
Team: Design
Location: Global
Start date: As soon as possible
Remote Compensation Philosophy"
                  type="text"
                />
              </div>

              <!--CV-->
              <div class="mt-10">
                <h3 class="fs-4 fw-boldest">Select a CV</h3>
                <select
                  class="form-select form-select-solid select2-hidden-accessible"
                  v-model="selectedCV"
                >
                  <option
                    v-for="resume in resumes"
                    :key="resume.id"
                    :value="resume.id"
                  >
                    {{ resume.name }} -
                    {{
                      moment(resume.created_at).format(
                        "MMMM Do YYYY, h:mm:ss a"
                      )
                    }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div
            v-if="!isProcessing"
            class="mt-5 card-footer d-flex align-items-end justify-content-between"
          >
            <div></div>
            <div>
              <button
                :disabled="!isValid"
                @click="processScan"
                class="btn btn-primary"
              >
                Scan & Analyze
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
import { useRouter } from "vue-router";
import { useLogger } from "vue-logger-plugin";
import Notice from "@/components/Notice.vue";
import { post } from "@/core/services/ApiService2";
import { hideModal } from "@/core/helpers/dom";
import { useResumeStore } from "@/stores/resume";
import moment from "moment/moment";
import type { JobScan } from "../../types";

const logger = useLogger();
const router = useRouter();

const isProcessing = ref(false);
const uploadProgress = ref(0);
const errMsg = ref<string>("");
const uploadMessage = ref(
  "Analyzing the job, please do not close your browser tab"
);

const jobDescription = ref("");
const jobURL = ref("");
const selectedCV = ref("");

const isValid = computed(() => {
  return (
    Boolean(selectedCV.value) && Boolean(jobURL.value || jobDescription.value)
  );
});

function clearStates() {
  isProcessing.value = false;
  uploadProgress.value = 0;
  setError("");
}

function setError(msg: string) {
  errMsg.value = msg;
}

const resumeStore = useResumeStore();
const { resumes } = storeToRefs(resumeStore);

async function processScan() {
  try {
    clearStates();
    logger.debug("starting to process job...");
    isProcessing.value = true;

    const params = {
      job_url: jobURL.value,
      job_description: jobDescription.value,
      resume_id: selectedCV.value,
    };
    const data = await post<JobScan>("/job/scan", params);
    clearStates();
    hideModal("#scan_job_modal" as unknown as HTMLElement);
    gotoJobRoute(data.id);
  } catch (e) {
    isProcessing.value = false;
    setError(e.message || "Sorry, something bad happened, try again?");
  }
}

function gotoJobRoute(id: string) {
  router.push({
    name: "single-scan",
    params: {
      scan_id: id,
    },
  });
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
