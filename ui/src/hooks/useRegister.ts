import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { apiClient } from "../api/apiClient";

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

export const useRegister = (): UseMutationResult<RegisterResponse, Error, RegisterCredentials> => {
    return useMutation({
        mutationFn: async (credentials: RegisterCredentials) => {
            const response = await apiClient.post("/users/register", credentials);
            return response.data;
        },
    });
};
