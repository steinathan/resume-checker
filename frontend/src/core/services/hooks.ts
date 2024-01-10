import axios from "@/core/services/ApiService2";
import Swal from "sweetalert2";

export async function fixResume(
  resumeId: string,
  scanId: string | null = null
) {
  const yes = confirm(
    "We'll attempt to add these missing skills to your resume, continue?"
  );
  if (yes) {
    const url = `/resume/${resumeId}/fix?scan_id=${scanId}`;
    await axios({
      url: url,
      method: "GET",
      responseType: "blob",
    }).then(async (response) => {
      await Swal.fire({
        title: "Your Resume is ready!",
        text: "Kindly download your Resume as an editable DOCX but keep in mind that this is just an evaluation copy and you must carefully review the resume after downloading",
        icon: "success",
        buttonsStyling: false,
        confirmButtonText: "Ok, got it!",
        allowEscapeKey: false,
        allowOutsideClick: false,
        heightAuto: false,
        customClass: {
          confirmButton: "btn fw-semobold btn-light-primary",
        },
      });

      // @ts-ignore
      const url = window.URL.createObjectURL(new Blob([response]));
      const a = document.createElement("a");
      a.href = url;
      a.download = "revamped_resume.docx";
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    });
  }
}
