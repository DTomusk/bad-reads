import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { apiClient } from "../api/apiClient";

interface LoginCredentials {
    username: string;
    password: string;
}

interface LoginResponse {
    access_token: string;
    token_type: string;
}

export const useLogin = (): UseMutationResult<LoginResponse, Error, LoginCredentials> => {
    return useMutation({
        mutationFn: async (credentials: LoginCredentials) => {
            const formData = new FormData();
            formData.append("username", credentials.username);
            formData.append("password", credentials.password);
            
            const response = await apiClient.post<LoginResponse>("/users/login", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            });
            return response.data;
        },
    });
}; 