<template>
  <!--begin::Menu wrapper-->
  <div
    id="kt_aside_menu_wrapper"
    ref="scrollElRef"
    class="hover-scroll-overlay-y my-5 my-lg-6"
    data-kt-scroll="true"
    data-kt-scroll-activate="{default: false, lg: true}"
    data-kt-scroll-dependencies="#kt_aside_logo, #kt_aside_footer"
    data-kt-scroll-height="auto"
    data-kt-scroll-offset="0"
    data-kt-scroll-wrappers="#kt_aside_menu"
  >
    <!--begin::Menu-->
    <div
      id="kt_header_menu"
      class="menu menu-rounded menu-column menu-sub-indention menu-active-bg menu-title-gray-800 menu-state-title-primary menu-state-icon-primary menu-state-bullet-primary menu-arrow-gray-500 px-3 fw-semibold"
      data-kt-menu="true"
    >
      <template v-for="(item, i) in MainMenuConfig" :key="i">
        <div v-if="item.heading" class="menu-item">
          <div class="menu-content pt-8 pb-2">
            <span class="menu-section text-muted text-uppercase fs-8 ls-1">
              {{ translate(item.heading) }}
            </span>
          </div>
        </div>
        <template v-for="(menuItem, j) in item.pages" :key="j">
          <template v-if="menuItem.heading">
            <div class="menu-item">
              <router-link
                v-if="menuItem.route"
                class="menu-link"
                active-class="active"
                :to="menuItem.route"
              >
                <span
                  v-if="menuItem.keenthemesIcon || menuItem.bootstrapIcon"
                  class="menu-icon"
                >
                  <i
                    v-if="asideMenuIcons === 'bootstrap'"
                    :class="menuItem.bootstrapIcon"
                    class="bi fs-3"
                  ></i>
                  <KTIcon
                    v-else-if="asideMenuIcons === 'keenthemes'"
                    :icon-name="menuItem.keenthemesIcon"
                    class="fs-2"
                  />
                </span>
                <span class="menu-title">{{
                  translate(menuItem.heading)
                }}</span>
              </router-link>
            </div>
          </template>
          <div
            v-if="menuItem.sectionTitle && menuItem.route"
            :class="{ show: hasActiveChildren(menuItem.route) }"
            class="menu-item menu-accordion"
            data-kt-menu-sub="accordion"
            data-kt-menu-trigger="click"
          >
            <span class="menu-link">
              <span
                v-if="menuItem.keenthemesIcon || menuItem.bootstrapIcon"
                class="menu-icon"
              >
                <i
                  v-if="asideMenuIcons === 'bootstrap'"
                  :class="menuItem.bootstrapIcon"
                  class="bi fs-3"
                ></i>
                <KTIcon
                  v-else-if="asideMenuIcons === 'keenthemes'"
                  :icon-name="menuItem.keenthemesIcon"
                  class="fs-2"
                />
              </span>
              <span class="menu-title">{{
                translate(menuItem.sectionTitle)
              }}</span>
              <span class="menu-arrow"></span>
            </span>
            <div
              :class="{ show: hasActiveChildren(menuItem.route) }"
              class="menu-sub menu-sub-accordion"
            >
              <template v-for="(item2, k) in menuItem.sub" :key="k">
                <div v-if="item2.heading" class="menu-item">
                  <router-link
                    v-if="item2.route"
                    class="menu-link"
                    active-class="active"
                    :to="item2.route"
                  >
                    <span class="menu-bullet">
                      <span class="bullet bullet-dot"></span>
                    </span>
                    <span class="menu-title">{{
                      translate(item2.heading)
                    }}</span>
                  </router-link>
                </div>
                <div
                  v-if="item2.sectionTitle && item2.route"
                  :class="{ show: hasActiveChildren(item2.route) }"
                  class="menu-item menu-accordion"
                  data-kt-menu-sub="accordion"
                  data-kt-menu-trigger="click"
                >
                  <span class="menu-link">
                    <span class="menu-bullet">
                      <span class="bullet bullet-dot"></span>
                    </span>
                    <span class="menu-title">{{
                      translate(item2.sectionTitle)
                    }}</span>
                    <span class="menu-arrow"></span>
                  </span>
                  <div
                    v-if="item2.route"
                    :class="{ show: hasActiveChildren(item2.route) }"
                    class="menu-sub menu-sub-accordion"
                  >
                    <template v-for="(item3, k) in item2.sub" :key="k">
                      <div v-if="item3.heading" class="menu-item">
                        <router-link
                          v-if="item3.route"
                          class="menu-link"
                          active-class="active"
                          :to="item3.route"
                        >
                          <span class="menu-bullet">
                            <span class="bullet bullet-dot"></span>
                          </span>
                          <span class="menu-title">{{
                            translate(item3.heading)
                          }}</span>
                        </router-link>
                      </div>
                    </template>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </template>
      </template>
      <div class="menu-item">
        <div class="menu-content">
          <div class="separator mx-1 my-4"></div>
        </div>
      </div>
      <div class="menu-item">
        <a
          class="menu-link"
          href="https://preview.keenthemes.com/metronic8/vue/docs/#/changelog"
        >
          <span class="menu-icon">
            <i
              v-if="asideMenuIcons === 'bootstrap'"
              class="bi bi-card-text fs-3"
            ></i>
            <KTIcon
              v-else-if="asideMenuIcons === 'keenthemes'"
              icon-name="document"
              class="fs-2"
            />
          </span>
          <span class="menu-title"
            >{{ translate("changelog") }} v{{ version }}</span
          >
        </a>
      </div>
    </div>
    <!--end::Menu-->
  </div>
  <!--end::Menu wrapper-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted, ref } from "vue";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";
import { version } from "@/core/helpers/documentation";
import { asideMenuIcons } from "@/core/helpers/config";
import MainMenuConfig from "@/core/config/MainMenuConfig";

export default defineComponent({
  name: "kt-menu",
  components: {},
  setup() {
    const { t, te } = useI18n();
    const route = useRoute();
    const scrollElRef = ref<null | HTMLElement>(null);

    onMounted(() => {
      if (scrollElRef.value) {
        scrollElRef.value.scrollTop = 0;
      }
    });

    const translate = (text: string) => {
      if (te(text)) {
        return t(text);
      } else {
        return text;
      }
    };

    const hasActiveChildren = (match: string) => {
      return route.path.indexOf(match) !== -1;
    };

    return {
      hasActiveChildren,
      MainMenuConfig,
      asideMenuIcons,
      version,
      translate,
      getAssetPath,
    };
  },
});
</script>
