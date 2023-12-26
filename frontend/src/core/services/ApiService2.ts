import Axios, { AxiosError } from "axios";
import type { AxiosResponse } from "axios";
import JwtService from "@/core/services/JwtService";

export const baseUrl = import.meta.env.VITE_APP_API_URL as string;
const axios = Axios.create({
  baseURL: baseUrl,
});

axios.interceptors.request.use((config) => {
  const token = JwtService.getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${JwtService.getToken()}`;
  }
  return config;
});

axios.interceptors.response.use(
  (response: AxiosResponse) => {
    return response.data as any;
  },
  (error: AxiosError) => {
    let rejectionMessage = "Something went wrong";

    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx + "/v1"
      const data = error.response.data as any;
      const { code, message } = data;
      if (message) {
        rejectionMessage = error.message;
      }

      if (code === "TokenExpiredError") {
        console.warn("logging out user: %s", message);
        JwtService.destroyToken();
        window.location.href = "/sign-in";
      }
      console.error("[KT] ApiService Response Error:", error.response.data);
    } else if (error.request) {
      // The request was made, but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser
      console.error("[KT] ApiService Request Error:", error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error("[KT] ApiService Error:", error.message);
      throw new Error(`[KT] ApiService ${error}`);
    }

    return Promise.reject(rejectionMessage);
  }
);

/**
 * POST request
 * @param url
 * @param data
 */
export function post<T = Record<string, any>>(url, data): Promise<T> {
  return axios.post(url, data);
}

export function get<T = Record<string, any>>(
  url,
  query: Record<string, any>
): Promise<T> {
  return axios.get(url, {
    params: query,
  });
}

export default axios;
