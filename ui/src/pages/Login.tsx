import { Anchor, Button, Center, PasswordInput, Stack, TextInput, Title, Group } from "@mantine/core"
import { useForm } from "@mantine/form";
import { useLogin } from "../hooks/useLogin";
import { useAuth } from "../auth/AuthProvider";
import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import AlertBanner from "../components/Shared/AlertBanner";

export default function Login() {
    const location = useLocation();
    const navigate = useNavigate();
    const from = location.state?.from || "/";

    const { mutate: login, isPending } = useLogin();
    const { isAuthenticated, login: loginAuth } = useAuth();
    const [showAlert, setShowAlert] = useState(false);
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
    }, [isAuthenticated, navigate, from]);

    const handleSubmit = (values: typeof form.values) => {
        
        login({
            username: values.email,
            password: values.password,
        },
        {
            onSuccess: (data) => {
                loginAuth(data.access_token);
                navigate(from, { replace: true });
            },
            onError: () => {
                setShowAlert(true);
            },
        });
    };

    return (
        <Center>
            <form onSubmit={form.onSubmit(handleSubmit)}>
                <Stack>
                    <Title ta="center" order={1} mb="sm" mt="xl">💅Welcome back💅</Title>
                    {showAlert && <AlertBanner title="Login failed" message="Invalid email or password" type="error" />}
                    <TextInput 
                        required 
                        label="Email" 
                        placeholder="Email"
                        {...form.getInputProps('email')}
                        radius="md"
                        size="lg"
                        onFocus={() => setShowAlert(false)}
                    />
                    <PasswordInput 
                        required 
                        label="Password" 
                        placeholder="Password" 
                        {...form.getInputProps('password')}
                        radius="md"
                        size="lg"
                        onFocus={() => setShowAlert(false)}
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