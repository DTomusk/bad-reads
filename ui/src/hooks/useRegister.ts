import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { apiClient } from "../api/apiClient";
import { AxiosError } from "axios";

interface RegisterCredentials {
    password: string;
    confirm_password: string;
    email: string;
}

// TODO: think about what to return
interface RegisterResponse {
    id: string;
    email: string;
}

// TODO: centralise error responses
interface RegisterError {
    detail: string;
}

export const useRegister = (): UseMutationResult<RegisterResponse, AxiosError<RegisterError>, RegisterCredentials> => {
    return useMutation({
        mutationFn: async (credentials: RegisterCredentials) => {
            const response = await apiClient.post("/users/register", credentials);
            return response.data;
        },
    });
};
