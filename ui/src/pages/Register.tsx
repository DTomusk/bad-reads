import { useForm } from "@mantine/form";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthProvider";
import { Anchor, Button, Center, Group, PasswordInput, Stack, TextInput, Title } from "@mantine/core";
import AlertBanner from "../components/Shared/AlertBanner";
import { useRegister } from "../hooks/useRegister";

export default function Register() {
    const location = useLocation();
    const navigate = useNavigate();
    const from = location.state?.from || "/";

    const { mutate: register, isPending } = useRegister();
    const { isAuthenticated } = useAuth();

    const [showSuccessAlert, setShowSuccessAlert] = useState(false);

    const [showErrorAlert, setShowErrorAlert] = useState(false);
    const [errorMessage, setErrorMessage] = useState("");

    const form = useForm({
        initialValues: {
            email: "",
            password: "",
            confirm_password: ""
        },

        validate: {
            email: (value) => /^\S+@\S+$/.test(value) ? null : "Invalid email",
            password: (value) => value.length <= 6 ? "Password should include at least 6 characters" : null,
            // confirmPassword: (value) => 
        },
    });

    useEffect(() => {
        if (isAuthenticated) {
            navigate(from, { replace: true });
        }
    }, [isAuthenticated, navigate, from]);

    const handleSubmit = (values: typeof form.values) => {
        register({
            email: values.email,
            password: values.password,
            confirm_password: values.confirm_password
        },
        {
            onSuccess: () => {
                setShowSuccessAlert(true);
            },
            onError: (error) => {
                setErrorMessage(error.response?.data?.detail || "Something went wrong signing you up")
                setShowErrorAlert(true);
            }
        })
    }

    return (
        <Center>
            <form onSubmit={form.onSubmit(handleSubmit)}>
                <Stack>
                    <Title ta="center" order={1} mb="xl" mt="xl">✨Register✨</Title>
                    {showSuccessAlert && <AlertBanner title="Registered successfully" type="success" message="Welcome to the coolest club in town"></AlertBanner>}
                    {showErrorAlert && <AlertBanner title="Registration failed" message={errorMessage} type="error" />}
                    <TextInput 
                        required 
                        label="Email" 
                        placeholder="Email"
                        {...form.getInputProps('email')}
                        radius="md"
                        size="lg"
                        onFocus={() => setShowErrorAlert(false)}
                    />
                    <PasswordInput 
                        required 
                        label="Password" 
                        placeholder="Password" 
                        {...form.getInputProps('password')}
                        radius="md"
                        size="lg"
                        onFocus={() => setShowErrorAlert(false)}
                    />
                    <PasswordInput 
                        required 
                        label="Confirm Password" 
                        placeholder="Confirm Password" 
                        {...form.getInputProps('confirm_password')}
                        radius="md"
                        size="lg"
                        onFocus={() => setShowErrorAlert(false)}
                    />  
                </Stack>
                <Group justify="space-between" mt="xl">
                    <Anchor
                        component="button"
                        type="button"
                        onClick={() => navigate("/login")}
                        size="md"
                    >
                    Already signed up? Login here
                    </Anchor>
                    <Button 
                        type="submit" 
                        radius="xl" 
                        size="lg" 
                        loading={isPending}
                    >
                    Register
                    </Button>
                </Group>
            </form>
        </Center>
    )
}