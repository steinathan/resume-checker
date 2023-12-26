import { computed } from "vue";
import { useConfigStore } from "@/stores/config";
import { ThemeModeComponent } from "@/assets/ts/layout";

/**
 * Returns layout config
 * @returns {object}
 */
export const config = computed(() => {
  return useConfigStore().config;
});

/**
 * Returns theme mode
 * @returns {string}
 */
export const themeMode = computed(() => {
  if (useConfigStore().getLayoutConfig("general.mode") === "system") {
    return ThemeModeComponent.getSystemMode();
  }
  return useConfigStore().getLayoutConfig("general.mode");
});

/**
 * Returns the actual theme configuration mode
 * @returns {string}
 */
export const themeConfigValue = computed<"system" | "dark" | "light">(() => {
  return useConfigStore().getLayoutConfig("general.mode")
    ? (useConfigStore().getLayoutConfig("general.mode") as
        | "system"
        | "dark"
        | "light")
    : "system";
});

/**
 * Set the sidebar display
 * @returns {boolean}
 */
export const displaySidebar = computed(() => {
  return useConfigStore().getLayoutConfig("sidebar.display");
});

/**
 * Check if footer container is fluid
 * @returns {boolean}
 */
export const footerWidthFluid = computed(() => {
  return useConfigStore().getLayoutConfig("footer.width") === "fluid";
});

/**
 * Check if header container is fluid
 * @returns {boolean}
 */
export const headerWidthFluid = computed(() => {
  return useConfigStore().getLayoutConfig("header.width") === "fluid";
});

/**
 * Returns header left part type
 * @returns {string}
 */
export const headerLeft = computed(() => {
  return useConfigStore().getLayoutConfig("header.left");
});

/**
 * Returns header fixed on desktop
 * @returns {boolean}
 */
export const headerFixed = computed(() => {
  return useConfigStore().getLayoutConfig("header.fixed.desktop");
});

/**
 * Returns header fixed on tablet and mobile
 * @returns {boolean}
 */
export const headerFixedOnMobile = computed(() => {
  return useConfigStore().getLayoutConfig("header.fixed.tabletAndMobile");
});

/**
 * Set the aside display
 * @returns {boolean}
 */
export const asideDisplay = computed(() => {
  return useConfigStore().getLayoutConfig("aside.display");
});

/**
 * Check if toolbar width is fluid
 * @returns {boolean}
 */
export const toolbarWidthFluid = computed(() => {
  return useConfigStore().getLayoutConfig("toolbar.width") === "fluid";
});

/**
 * Set the toolbar display
 * @returns {boolean}
 */
export const toolbarDisplay = computed(() => {
  return useConfigStore().getLayoutConfig("toolbar.display");
});

/**
 * Page title display
 * @returns {boolean}
 */
export const pageTitleDisplay = computed(() => {
  return useConfigStore().getLayoutConfig("pageTitle.display");
});

/**
 * Page title breadcrumb display
 * @returns {boolean}
 */
export const pageTitleBreadcrumbDisplay = computed(() => {
  return useConfigStore().getLayoutConfig("pageTitle.breadcrumb");
});

/**
 * Page title direction display
 * @returns { "row" | "column" }
 */
export const pageTitleDirection = computed(() => {
  return useConfigStore().getLayoutConfig("pageTitle.direction");
});

/**
 * Check if the page loader is enabled
 * @returns {boolean}
 */
export const loaderEnabled = computed(() => {
  return useConfigStore().getLayoutConfig("loader.display");
});

/**
 * Check if container width is fluid
 * @returns {boolean}
 */
export const contentWidthFluid = computed(() => {
  return useConfigStore().getLayoutConfig("content.width") === "fluid";
});

/**
 * Page loader logo image
 * @returns {string}
 */
export const loaderLogo = computed(() => {
  return (
    import.meta.env.BASE_URL + useConfigStore().getLayoutConfig("loader.logo")
  );
});

/**
 * Check if the aside menu is enabled
 * @returns {boolean}
 */
export const asideEnabled = computed(() => {
  return !!useConfigStore().getLayoutConfig("aside.display");
});

/**
 * Set the aside theme
 * @returns {string}
 */
export const asideTheme = computed(() => {
  return useConfigStore().getLayoutConfig("aside.theme");
});

/**
 * Set the subheader display
 * @returns {boolean}
 */
export const subheaderDisplay = computed(() => {
  return useConfigStore().getLayoutConfig("toolbar.display");
});

/**
 * Set the aside menu icon type
 * @returns {string}
 */
export const asideMenuIcons = computed(() => {
  return useConfigStore().getLayoutConfig("aside.menuIcon");
});

/**
 * Light theme logo image
 * @returns {string}
 */
export const themeLightLogo = computed(() => {
  return useConfigStore().getLayoutConfig("main.logo.light");
});

/**
 * Dark theme logo image
 * @returns {string}
 */
export const themeDarkLogo = computed(() => {
  return useConfigStore().getLayoutConfig("main.logo.dark");
});

/**
 * Set the header menu icon type
 * @returns {string}
 */
export const headerMenuIcons = computed(() => {
  return useConfigStore().getLayoutConfig("header.menuIcon");
});

/**
 * Scrolltop display
 * @returns {boolean}
 */
export const scrolltopDispaly = computed(() => {
  return useConfigStore().getLayoutConfig("scrolltop.display");
});

/**
 * Illustrations set
 * @returns {string}
 */
export const illustrationsSet = computed(() => {
  return useConfigStore().getLayoutConfig("illustrations.set");
});
