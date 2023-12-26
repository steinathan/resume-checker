<template>
  <!--begin::Tables Widget 3-->
  <div :class="widgetClasses" class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Files</span>

        <span class="text-muted mt-1 fw-semobold fs-7"
          >Over 100 pending files</span
        >
      </h3>
      <div class="card-toolbar">
        <!--begin::Menu-->
        <button
          type="button"
          class="btn btn-sm btn-icon btn-color-primary btn-active-light-primary"
          data-kt-menu-trigger="click"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-flip="top-end"
        >
          <KTIcon icon-name="category" icon-class="fs-2" />
        </button>
        <Dropdown3></Dropdown3>
        <!--end::Menu-->
      </div>
    </div>
    <!--end::Header-->

    <!--begin::Body-->
    <div class="card-body py-3">
      <!--begin::Table container-->
      <div class="table-responsive">
        <!--begin::Table-->
        <table class="table align-middle gs-0 gy-3">
          <!--begin::Table head-->
          <thead>
            <tr>
              <th class="p-0 w-50px"></th>
              <th class="p-0 min-w-150px"></th>
              <th class="p-0 min-w-140px"></th>
              <th class="p-0 min-w-120px"></th>
              <th class="p-0 min-w-40px"></th>
            </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
            <template v-for="(item, index) in items" :key="index">
              <tr>
                <td>
                  <div class="symbol symbol-50px me-2">
                    <span
                      :class="`bg-light-${item.color}`"
                      class="symbol-label"
                    >
                      <KTIcon
                        :icon-name="item.icon"
                        :icon-class="`text-${item.color} fs-2x`"
                      />
                    </span>
                  </div>
                </td>
                <td>
                  <a
                    href="#"
                    class="text-dark fw-bold text-hover-primary mb-1 fs-6"
                  >
                    {{ item.title }}
                  </a>
                </td>
                <td class="text-end text-muted fw-semobold">
                  {{ item.technologies }}
                </td>
                <td class="text-end text-muted fw-semobold">
                  {{ item.users }}
                </td>
                <td class="text-end text-dark fw-bold fs-6 pe-0">
                  {{ item.size }}
                </td>
              </tr>
            </template>
          </tbody>
          <!--end::Table body-->
        </table>
        <!--end::Table-->
      </div>
      <!--end::Table container-->
    </div>
    <!--begin::Body-->
  </div>
  <!--end::Tables Widget 3-->
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import Dropdown3 from "@/components/dropdown/Dropdown3.vue";

export default defineComponent({
  name: "kt-widget-3",
  components: {
    Dropdown3,
  },
  props: {
    widgetClasses: String,
  },
  setup() {
    const items = [
      {
        icon: "basket",
        color: "success",
        title: "Top Authors",
        description: "Best Customers",
        technologies: "ReactJs, HTML",
        users: "4600 Users",
        size: "5.4MB",
      },
      {
        icon: "category",
        color: "danger",
        title: "Popular Authors",
        description: "Best Customers",
        technologies: "Python, MySQL",
        users: "7200 Users",
        size: "2.8MB",
      },
      {
        icon: "briefcase",
        color: "info",
        title: "New Users",
        description: "Communication/Group.svg",
        technologies: "Laravel, Metronic",
        users: "890 Users",
        size: "1.5MB",
      },
      {
        icon: "abstract-26",
        color: "warning",
        title: "Active Customers",
        description: "Best Customers",
        technologies: "AngularJS, C#",
        users: "4600 Users",
        size: "5.4MB",
      },
      {
        icon: "abstract-41",
        color: "primary",
        title: "Active Customers",
        description: "Best Customers",
        technologies: "ReactJS, Ruby",
        users: "354 Users",
        size: "500KB",
      },
    ];

    return {
      items,
      getAssetPath,
    };
  },
});
</script>
