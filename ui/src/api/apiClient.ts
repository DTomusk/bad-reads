import axios from "axios";
import { apiConfig } from "../config/apiConfig";

export const apiClient = axios.create({
    baseURL: apiConfig.apiUrl,
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 5000,
});

// Add a request interceptor
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// TODO: this is commented out because it messes with the login page
// Add a response interceptor to handle 401 errors
// apiClient.interceptors.response.use(
//     (response) => response,
//     (error) => {
//         if (error.response?.status === 401) {
//             // Clear token and redirect to login if unauthorized
//             localStorage.removeItem('token');
//             window.location.href = '/login';
//         }
//         return Promise.reject(error);
//     }
// );

