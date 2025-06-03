import { apiClient } from "./apiClient";

export const fetcher = async <T>(url: string): Promise<T> => {
    const response = await apiClient.get<T>(url);
    return response.data;
}

export const fetcherWithParams = async <T>(url: string, params: any): Promise<T> => {
    const response = await apiClient.get(url, { params });
    return response.data;
}
