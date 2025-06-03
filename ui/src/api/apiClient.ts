import axios from "axios";
import { apiConfig } from "../config/apiConfig";

export const apiClient = axios.create({
    baseURL: apiConfig.apiUrl,
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 5000,
});

