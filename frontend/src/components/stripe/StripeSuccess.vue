<script setup lang="ts"></script>

<template>
  <div class="d-flex flex-column flex-center flex-column-fluid">
    <!--begin::Content-->
    <div class="d-flex flex-column flex-center text-center p-10">
      <!--begin::Wrapper-->
      <div class="card card-flush w-md-650px py-5">
        <div class="card-body py-15 py-lg-20">
          <!--          &lt;!&ndash;begin::Logo&ndash;&gt;-->
          <!--          <div class="mb-7">-->
          <!--            <a href="#" class="">-->
          <!--              <img alt="Logo" src="/media/logos/default.svg" class="h-40px" />-->
          <!--            </a>-->
          <!--          </div>-->
          <!--          &lt;!&ndash;end::Logo&ndash;&gt;-->

          <!--begin::Title-->
          <h1 class="fw-bolder text-gray-900 mb-5">Purchase Successful</h1>
          <!--end::Title-->

          <!--begin::Text-->
          <div class="fw-semibold fs-6 text-gray-500 mb-7">
            Congrats, Your purchase is confirmed, enjoy unlimited resume scans
            and job matcher, optimizing your job search for success!
          </div>
          <!--end::Text-->

          <!--begin::Illustration-->
          <div class="mb-0">
            <img
              src="/media/auth/welcome.png"
              class="mw-100 mh-300px theme-light-show"
              alt=""
            />
            <img
              src="/media/auth/welcome-dark.png"
              class="mw-100 mh-300px theme-dark-show"
              alt=""
            />
          </div>
          <!--end::Illustration-->

          <!--begin::Link-->
          <div class="mb-0">
            <a href="/dashboard" class="btn btn-sm btn-primary"
              >Go To Dashboard</a
            >
          </div>
          <!--end::Link-->
        </div>
      </div>
      <!--end::Wrapper-->
    </div>
    <!--end::Content-->
  </div>
</template>

<style scoped></style>
