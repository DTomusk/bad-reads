import { Anchor, Button, Center, PasswordInput, Stack, TextInput, Text, Title, Group } from "@mantine/core"
import { useForm } from "@mantine/form";
import { useLogin } from "../hooks/useLogin";
import { useAuth } from "../auth/AuthProvider";
import { useLocation, useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function Login() {
    const location = useLocation();
    const navigate = useNavigate();
    const from = location.state?.from || "/";

    const { mutate: login, isPending } = useLogin();
    const { isAuthenticated, login: loginAuth } = useAuth();
    const form = useForm({
        initialValues: {
            email: "",
            password: "",
        },

        validate: {
            email: (value) => /^\S+@\S+$/.test(value) ? null : "Invalid email",
            password: (value) => value.length <= 6 ? "Password should include at least 6 characters" : null,
        },
    });

    useEffect(() => {
        if (isAuthenticated) {
            navigate(from, { replace: true });
        }
    }, [isAuthenticated, navigate]);

    const handleSubmit = () => {
        login({
            username: form.values.email,
            password: form.values.password,
        },
        {
            onSuccess: (data) => {
                loginAuth(data.access_token);
                navigate(from, { replace: true });
            },
            onError: () => {
                console.error("Login failed");
            },
        });
    };

    return (
        <Center>
            <form onSubmit={form.onSubmit(handleSubmit)}>
                <Stack>
                    <Title ta="center" order={1} mb="xl" mt="xl">💅Welcome back💅</Title>
                    <TextInput 
                        required 
                        label="Email" 
                        placeholder="Email"
                        value={form.values.email}
                        onChange={(event) => form.setFieldValue("email", event.currentTarget.value)}
                        error={form.errors.email && 'Invalid email'}
                        radius="md"
                        size="lg"
                    />
                    <PasswordInput 
                        required 
                        label="Password" 
                        placeholder="Password" 
                        value={form.values.password}
                        onChange={(event) => form.setFieldValue("password", event.currentTarget.value)}
                        error={form.errors.password && 'Password should include at least 6 characters'}
                        radius="md"
                        size="lg"
                    />
                </Stack>

                <Group justify="space-between" mt="xl">
                    <Anchor
                        component="button"
                        type="button"
                        onClick={() => navigate("/register")}
                        size="md"
                    >
                    Don't have an account yet? Register
                    </Anchor>
                    <Button 
                        type="submit" 
                        radius="xl" 
                        size="lg" 
                        loading={isPending}
                    >
                    Login
                    </Button>
                </Group>
            </form>
        </Center>
    )
}