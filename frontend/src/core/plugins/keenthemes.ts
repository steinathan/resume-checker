import {
  DrawerComponent,
  MenuComponent,
  ScrollComponent,
  StickyComponent,
  SwapperComponent,
  ToggleComponent,
} from "@/assets/ts/components";
import { ThemeModeComponent } from "@/assets/ts/layout";
import type { App } from "vue";
import KTIcon from "@/core/helpers/kt-icon/KTIcon.vue";

/**
 * @description Initialize KeenThemes custom components
 */
const initializeComponents = () => {
  ThemeModeComponent.init();
  setTimeout(() => {
    ToggleComponent.bootstrap();
    StickyComponent.bootstrap();
    MenuComponent.bootstrap();
    ScrollComponent.bootstrap();
    DrawerComponent.bootstrap();
    SwapperComponent.bootstrap();
  }, 0);
};

/**
 * @description Reinitialize KeenThemes custom components
 */
const reinitializeComponents = () => {
  ThemeModeComponent.init();
  setTimeout(() => {
    ToggleComponent.reinitialization();
    StickyComponent.reInitialization();
    MenuComponent.reinitialization();
    reinitializeScrollComponent().then(() => {
      ScrollComponent.updateAll();
    });
    DrawerComponent.reinitialization();
    SwapperComponent.reinitialization();
  }, 0);
};

const reinitializeScrollComponent = async () => {
  await ScrollComponent.reinitialization();
};

/**
 * Initialize KTIcon global component instance
 * @param app vue instance
 */
function initKtIcon(app: App<Element>) {
  app.component("KTIcon", KTIcon);
}

export {
  initializeComponents,
  reinitializeComponents,
  reinitializeScrollComponent,
  initKtIcon,
};
