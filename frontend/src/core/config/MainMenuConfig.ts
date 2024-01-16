import type { User } from "@/stores/auth";

export interface MenuItem {
  heading?: string;
  sectionTitle?: string;
  route?: string;
  pages?: Array<MenuItem>;
  keenthemesIcon?: string;
  bootstrapIcon?: string;
  sub?: Array<MenuItem>;
}

const MainMenuConfig = (user: User): Array<MenuItem> => {
  const pages = [
    {
      heading: "dashboard",
      route: "/dashboard",
    },
  ];
  if (!user?.stripe_customer_id) {
    pages.push({
      heading: "Upgrade",
      route: "/upgrade",
    });
  }
  return [
    {
      pages: pages,
    },
  ];
};

export default MainMenuConfig;
