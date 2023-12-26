<template>
  <!--begin::Layout Builder Notice-->
  <div class="card mb-10">
    <div class="card-body d-flex align-items-center py-8">
      <!--begin::Icon-->
      <div
        class="d-flex h-50px w-50px h-lg-80px w-lg-80px flex-shrink-0 flex-center position-relative align-self-start align-self-lg-center mt-3 mt-lg-0"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          class="text-primary h-75px w-75px h-lg-100px w-lg-100px position-absolute opacity-5"
        >
          <path
            fill="currentColor"
            d="M10.2,21.23,4.91,18.17a3.58,3.58,0,0,1-1.8-3.11V8.94a3.58,3.58,0,0,1,1.8-3.11L10.2,2.77a3.62,3.62,0,0,1,3.6,0l5.29,3.06a3.58,3.58,0,0,1,1.8,3.11v6.12a3.58,3.58,0,0,1-1.8,3.11L13.8,21.23A3.62,3.62,0,0,1,10.2,21.23Z"
          ></path>
        </svg>
        <KTIcon
          icon-name="wrench"
          icon-class="fs-2x fs-lg-3x text-primary position-absolute"
        />
      </div>
      <!--end::Icon-->

      <!--begin::Description-->
      <div class="ms-6">
        <p class="list-unstyled text-gray-600 fw-semobold fs-6 p-0 m-0">
          The layout builder is to assist your set and configure your preferred
          project layout specifications and preview it in real time and export
          the HTML template with its includable partials of this demo. The
          downloaded version does not include the assets folder since the layout
          builder's main purpose is to help to generate the final HTML code
          without hassle.
        </p>
      </div>
      <!--end::Description-->
    </div>
  </div>
  <!--end::Layout Builder Notice-->

  <div class="card mb-10">
    <!--begin::Header-->
    <div class="card-header card-header-stretch">
      <ul
        class="nav nav-stretch nav-line-tabs fw-semobold border-0"
        role="tablist"
        id="kt_layout_builder_tabs"
        ref="kt_layout_builder_tabs"
      >
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 0 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="0"
            role="tab"
          >
            Main
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 1 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="1"
            role="tab"
          >
            Header
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 2 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="2"
            role="tab"
          >
            Subheader
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 3 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="3"
            role="tab"
          >
            Aside
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 4 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="4"
            role="tab"
          >
            Content
          </a>
        </li>
        <li class="nav-item">
          <a
            class="nav-link cursor-pointer"
            :class="{ active: tabIndex === 5 }"
            data-bs-toggle="tab"
            @click="setActiveTab($event)"
            data-tab-index="5"
            role="tab"
          >
            Footer
          </a>
        </li>
      </ul>
    </div>
    <!--end::Header-->

    <!--begin::Form-->
    <form class="form" id="kt_layout_builder_form" @submit="submit($event)">
      <!--begin::Body-->
      <div class="card-body">
        <div class="tab-content pt-3" id="kt_tabs">
          <div
            class="tab-pane"
            :class="{ active: tabIndex === 0 }"
            id="kt_builder_main"
          >
            <!--begin::Form group-->
            <div class="form-group d-flex flex-stack">
              <!--begin::Heading-->
              <div class="d-flex flex-column">
                <h4 class="fw-bold text-dark">Keenicons Style</h4>
                <div>
                  <span class="fs-7 fw-semibold text-muted"
                    >Select global UI icons style.</span
                  >{{ " " }}
                  <a
                    class="fw-semibold"
                    href="https://preview.keenthemes.com/html/metronic/docs/icons/keenicons"
                    target="_blank"
                    >Learn more</a
                  >
                </div>
              </div>
              <!--end::Heading-->
              <!--begin::Options-->
              <div
                class="d-flex flex-stack gap-3 mw-lg-600px"
                data-kt-buttons="true"
                data-kt-buttons-target=".form-check-image,.form-check-input"
                data-kt-initialized="1"
              >
                <!--begin::Option-->
                <label
                  :class="config.general.iconsType === 'duotone' && 'active'"
                  class="form-check-image form-check-success w-100 parent-active parent-hover"
                >
                  <!--begin::Image-->
                  <div
                    class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                  >
                    <KTIcon
                      icon-type="duotone"
                      icon-name="picture"
                      icon-class="fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                    />
                    <span
                      class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      >Duotone</span
                    >
                  </div>
                  <!--end::Image-->
                  <!--begin::Check-->
                  <div
                    style="
                      visibility: hidden;
                      height: 0;
                      width: 0;
                      overflow: hidden;
                    "
                  >
                    <input
                      v-model="config.general.iconsType"
                      class="form-check-input"
                      type="radio"
                      value="duotone"
                      :checked="config.general.iconsType === 'duotone'"
                    />
                  </div>
                  <!--end::Check-->
                </label>
                <!--end::Option-->
                <!--begin::Option-->
                <label
                  :class="config.general.iconsType === 'outline' && 'active'"
                  class="form-check-image form-check-success w-100 parent-active parent-hover"
                >
                  <!--begin::Image-->
                  <div
                    class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                  >
                    <i
                      class="ki-outline ki-picture fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                    ></i>
                    <span
                      class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      >Outline</span
                    >
                  </div>
                  <!--end::Image-->
                  <!--begin::Check-->
                  <div
                    style="
                      visibility: hidden;
                      height: 0;
                      width: 0;
                      overflow: hidden;
                    "
                  >
                    <input
                      v-model="config.general.iconsType"
                      class="form-check-input"
                      type="radio"
                      value="outline"
                      name="outline"
                      :checked="config.general.iconsType === 'outline'"
                    />
                  </div>
                  <!--end::Check-->
                </label>
                <!--end::Option-->
                <!--begin::Option-->
                <label
                  :class="config.general.iconsType === 'solid' && 'active'"
                  class="form-check-image form-check-success w-100 parent-active parent-hover"
                >
                  <!--begin::Image-->
                  <div
                    class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                  >
                    <i
                      class="ki-solid ki-picture fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                    ></i>
                    <span
                      class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      >Solid</span
                    >
                  </div>
                  <!--end::Image-->
                  <!--begin::Check-->
                  <div
                    style="
                      visibility: hidden;
                      height: 0;
                      width: 0;
                      overflow: hidden;
                    "
                  >
                    <input
                      v-model="config.general.iconsType"
                      class="form-check-input"
                      type="radio"
                      value="solid"
                      name="solid"
                      :checked="config.general.iconsType === 'solid'"
                    />
                  </div>
                  <!--end::Check-->
                </label>
                <!--end::Option-->
              </div>
              <!--end::Options-->
            </div>
            <!--end::Form group-->
            <!--begin::Separator-->
            <div class="separator separator-dashed my-6"></div>
            <!--end::Separator-->
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Illustration Set:</label
              >
              <div class="col-lg-8 pe-10">
                <div class="row g-9 mb-3">
                  <div class="col-6">
                    <label
                      class="btn btn-outline btn-outline-dashed btn-outline-default d-flex flex-column text-start p-6"
                      for="sketchy-1"
                    >
                      <span class="d-flex mb-2">
                        <span
                          class="form-check form-check-custom form-check-solid form-check-sm me-5"
                        >
                          <input
                            class="form-check-input"
                            type="radio"
                            v-model="config.illustrations.set"
                            value="sketchy-1"
                            name="illustrations-set"
                            id="sketchy-1"
                          />
                        </span>
                        <span class="fs-4 fw-bold">Sketchy</span>
                      </span>
                      <span
                        :style="{
                          backgroundImage: `url(${getAssetPath(
                            '/media/illustrations/sketchy-1/1.png'
                          )})`,
                        }"
                        class="d-block h-200px w-100 bgi-no-repeat bgi-size-contain bgi-position-center"
                      ></span>
                    </label>
                  </div>
                  <div class="col-6">
                    <label
                      class="btn btn-outline btn-outline-dashed btn-outline-default d-flex flex-column text-start p-6"
                      for="sigma-1"
                    >
                      <span class="d-flex mb-2">
                        <span
                          class="form-check form-check-custom form-check-solid form-check-sm me-5"
                        >
                          <input
                            class="form-check-input"
                            type="radio"
                            v-model="config.illustrations.set"
                            value="sigma-1"
                            name="illustrations-set"
                            id="sigma-1"
                          />
                        </span>
                        <span class="fs-4 fw-bold">Sigma</span>
                      </span>
                      <span
                        :style="{
                          backgroundImage: `url(${getAssetPath(
                            '/media/illustrations/sigma-1/1.png'
                          )})`,
                        }"
                        class="d-block h-200px w-100 bgi-no-repeat bgi-size-contain bgi-position-center"
                      ></span>
                    </label>
                  </div>
                  <div class="col-6">
                    <label
                      class="btn btn-outline btn-outline-dashed btn-outline-default d-flex flex-column text-start p-6"
                      for="dozzy-1"
                    >
                      <span class="d-flex mb-2">
                        <span
                          class="form-check form-check-custom form-check-solid form-check-sm me-5"
                        >
                          <input
                            class="form-check-input"
                            type="radio"
                            v-model="config.illustrations.set"
                            value="dozzy-1"
                            name="illustrations-set"
                            id="dozzy-1"
                          />
                        </span>
                        <span class="fs-4 fw-bold">Dozzy</span>
                      </span>
                      <span
                        :style="{
                          backgroundImage: `url(${getAssetPath(
                            '/media/illustrations/dozzy-1/1.png'
                          )})`,
                        }"
                        class="d-block h-200px w-100 bgi-no-repeat bgi-size-contain bgi-position-center"
                      ></span>
                    </label>
                  </div>
                  <div class="col-6">
                    <label
                      class="btn btn-outline btn-outline-dashed btn-outline-default d-flex flex-column text-start p-6"
                      for="unitedpalms-1"
                    >
                      <span class="d-flex mb-2">
                        <span
                          class="form-check form-check-custom form-check-solid form-check-sm me-5"
                        >
                          <input
                            class="form-check-input"
                            type="radio"
                            v-model="config.illustrations.set"
                            value="unitedpalms-1"
                            name="illustrations-set"
                            id="unitedpalms-1"
                          />
                        </span>
                        <span class="fs-4 fw-bold">United Palms</span>
                      </span>
                      <span
                        :style="{
                          backgroundImage: `url(${getAssetPath(
                            '/media/illustrations/unitedpalms-1/1.png'
                          )})`,
                        }"
                        class="d-block h-200px w-100 bgi-no-repeat bgi-size-contain bgi-position-center"
                      ></span>
                    </label>
                  </div>
                </div>
                <div class="form-text text-muted">
                  Select one of our in-house designed illustration set and apply
                  globally for all apps and pages
                </div>
              </div>
            </div>
          </div>

          <div
            class="tab-pane"
            :class="{ active: tabIndex === 1 }"
            id="kt_builder_header"
          >
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Fixed Header:</label
              >
              <div class="col-lg-9 col-xl-4">
                <input type="hidden" v-model="config.header.fixed.desktop" />
                <input
                  type="hidden"
                  v-model="config.header.fixed.tabletAndMobile"
                />

                <label
                  class="form-check form-check-custom form-check-solid form-switch mb-5"
                >
                  <input
                    class="form-check-input"
                    type="checkbox"
                    v-model="config.header.fixed.desktop"
                  />
                  <span class="form-check-label text-muted">Desktop</span>
                </label>

                <label
                  class="form-check form-check-custom form-check-solid form-switch mb-5"
                >
                  <input
                    class="form-check-input"
                    type="checkbox"
                    v-model="config.header.fixed.tabletAndMobile"
                  />
                  <span class="form-check-label text-muted"
                    >Tablet & Mobile</span
                  >
                </label>

                <div class="form-text text-muted">Enable fixed header</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Menu Icon:</label
              >
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.header.menuIcon"
                >
                  <option value="keenthemes">Keenthemes Font Icons</option>
                  <option value="bootstrap">Bootstrap Font Icons</option>
                </select>
                <div class="form-text text-muted">Select menu icon type.</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end">Width:</label>
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.header.width"
                >
                  <option value="fluid">Fluid</option>
                  <option value="fixed">Fixed</option>
                </select>
                <div class="form-text text-muted">
                  Select header width type.
                </div>
              </div>
            </div>
          </div>

          <div
            class="tab-pane"
            :class="{ active: tabIndex === 2 }"
            id="kt_builder_subheader"
          >
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Display:</label
              >
              <div class="col-lg-9 col-xl-4">
                <input type="hidden" v-model="config.toolbar.display" />
                <div
                  class="form-check form-check-custom form-check-solid form-switch mb-2"
                >
                  <input
                    class="form-check-input"
                    type="checkbox"
                    v-model="config.toolbar.display"
                    value="true"
                  />
                </div>
                <div class="form-text text-muted">Display Subheader</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end">Width:</label>
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.toolbar.width"
                >
                  <option value="fluid">Fluid</option>
                  <option value="fixed">Fixed</option>
                </select>
                <div class="form-text text-muted">
                  Select layout width type.
                </div>
              </div>
            </div>
          </div>

          <div
            class="tab-pane"
            :class="{ active: tabIndex === 3 }"
            id="kt_builder_aside"
          >
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end">Theme:</label>
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.aside.theme"
                >
                  <option value="dark">Dark</option>
                  <option value="light">Light</option>
                </select>
                <div class="form-text text-muted">Set aside theme</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Menu Icon:</label
              >
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.aside.menuIcon"
                >
                  <option value="keenthemes">Keenthemes Font Icons</option>
                  <option value="bootstrap">Bootstrap Font Icons</option>
                </select>
                <div class="form-text text-muted">Select menu icon type.</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Display:</label
              >
              <div class="col-lg-9 col-xl-4">
                <span class="switch switch-icon">
                  <input type="hidden" v-model="config.aside.display" />
                  <div
                    class="form-check form-check-custom form-check-solid form-switch mb-2"
                  >
                    <input
                      class="form-check-input"
                      type="checkbox"
                      v-model="config.aside.display"
                    />
                  </div>
                </span>
                <div class="form-text text-muted">Display Aside</div>
              </div>
            </div>
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end"
                >Minimized:</label
              >
              <div class="col-lg-9 col-xl-4">
                <span class="switch switch-icon">
                  <input type="hidden" v-model="config.aside.minimized" />
                  <div
                    class="form-check form-check-custom form-check-solid form-switch mb-2"
                  >
                    <input
                      class="form-check-input"
                      type="checkbox"
                      v-model="config.aside.minimized"
                    />
                  </div>
                </span>
                <div class="form-text text-muted">
                  Minimize secondary panel by default
                </div>
              </div>
            </div>
          </div>

          <div
            class="tab-pane"
            :class="{ active: tabIndex === 4 }"
            id="kt_builder_content"
          >
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end">Width:</label>
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.content.width"
                >
                  <option value="fluid">Fluid</option>
                  <option value="fixed">Fixed</option>
                </select>
                <div class="form-text text-muted">
                  Select layout width type.
                </div>
              </div>
            </div>
          </div>

          <div
            class="tab-pane"
            :class="{ active: tabIndex === 5 }"
            id="kt_builder_footer"
          >
            <div class="row mb-10">
              <label class="col-lg-3 col-form-label text-lg-end">Width:</label>
              <div class="col-lg-9 col-xl-4">
                <select
                  class="form-select form-select-solid"
                  v-model="config.footer.width"
                >
                  <option value="fluid">Fluid</option>
                  <option value="fixed">Fixed</option>
                </select>
                <div class="form-text text-muted">
                  Select layout width type.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--end::Body-->

      <!--begin::Footer-->
      <div class="card-footer py-6">
        <div class="row">
          <div class="col-lg-3"></div>
          <div class="col-lg-9">
            <input
              type="hidden"
              id="kt_layout_builder_tab"
              name="layout-builder[tab]"
            />
            <input
              type="hidden"
              id="kt_layout_builder_action"
              name="layout-builder[action]"
            />

            <button
              type="submit"
              id="kt_layout_builder_preview"
              class="btn btn-primary me-2"
            >
              <span class="indicator-label"> Preview </span>
              <span class="indicator-progress">
                Please wait...
                <span
                  class="spinner-border spinner-border-sm align-middle ms-2"
                ></span>
              </span>
            </button>

            <button
              @click="reset($event)"
              type="button"
              id="kt_layout_builder_reset"
              class="btn btn-active-light btn-color-muted fw-semobold"
            >
              Reset
            </button>
          </div>
        </div>
      </div>
      <!--end::Footer-->
    </form>
    <!--end::Form-->
  </div>

  <!--begin::Card-->
  <div class="card">
    <!--begin::Card Body-->
    <div class="card-body p-10 p-lg-15">
      <!--begin::Heading-->
      <h1 class="anchor fw-bold mb-5" id="overview">Generated config</h1>
      <!--end::Heading-->
      <div class="py-5">
        This config is used as a <b>{{ themeName }}</b> layout config, you can
        update default values inside file
        <code>metronic/vue/theme/src/core/config/DefaultLayoutConfig.ts</code>
      </div>
      <CodeHighlighter lang="json">{{ config }}</CodeHighlighter>
    </div>
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted, ref } from "vue";
import { config } from "@/core/helpers/config";
import CodeHighlighter from "@/components/highlighters/CodeHighlighter.vue";
import { themeName } from "@/core/helpers/documentation";
import { LS_CONFIG_NAME_KEY } from "@/stores/config";

const LS_BUILDER_TAB_NAME =
  "layoutBuilderTabIndex_" + import.meta.env.VITE_APP_DEMO;

export default defineComponent({
  name: "layout-builder",
  components: {
    CodeHighlighter,
  },
  setup() {
    const tabIndex = ref(0);

    onMounted(() => {
      // set the tab from previous
      tabIndex.value = parseInt(
        localStorage.getItem(LS_BUILDER_TAB_NAME) || "0"
      );
    });

    /**
     * Reset config
     * @param event
     */
    const reset = (event: any) => {
      event.preventDefault();
      // remove existing saved config
      localStorage.removeItem(LS_CONFIG_NAME_KEY);
      window.location.reload();
    };

    /**
     * Set active tab when the tab get clicked
     * @param event
     */
    const setActiveTab = (event: any) => {
      tabIndex.value = parseInt(event.target.getAttribute("data-tab-index"));
      // keep active tab
      localStorage.setItem(LS_BUILDER_TAB_NAME, tabIndex.value.toString());
    };

    /**
     * Submit form
     * @param event
     */
    const submit = (event: any) => {
      event.preventDefault();
      // save new config to localStorage
      localStorage.setItem(LS_CONFIG_NAME_KEY, JSON.stringify(config.value));
      window.location.reload();
    };

    return {
      tabIndex,
      config,
      reset,
      setActiveTab,
      submit,
      themeName,
      getAssetPath,
    };
  },
});
</script>
