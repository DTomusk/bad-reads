import { Center } from "@mantine/core";
import { useRegister } from "../hooks/useRegister";
import { useNavigate } from "react-router-dom";
import AuthForm from "./AuthForm";
import { useAuth } from "../auth/AuthProvider";
import { useEffect } from "react";

export default function Register() {
  const navigate = useNavigate();
  const { mutate: register, isPending } = useRegister();
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    if (isAuthenticated) {
      navigate("/");
    }
  }, [isAuthenticated, navigate]);

  const fields = [
    {
      name: "email",
      label: "Email",
      placeholder: "bad@bad-reads.com",
      type: "text" as const,
      validation: (val: string) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
    },
    {
      name: "password",
      label: "Password",
      placeholder: "Your password",
      type: "password" as const,
      validation: (val: string) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
    },
    {
      name: "confirm_password",
      label: "Confirm Password",
      placeholder: "Confirm your password",
      type: "password" as const,
      validation: (val: string, values?: Record<string, string>) =>
        val !== values?.password ? "Passwords did not match" : null,
    },
  ];

  const handleSubmit = (values: Record<string, string>) => {
    register(
      {
        email: values.email,
        password: values.password,
        confirm_password: values.confirm_password,
      },
      {
        onSuccess: (data) => {
          // TODO: Show success message to user, maybe a banner
          console.log("Registration successful:", data);
          navigate("/login");
        },
        onError: (error) => {
          // TODO: Show error message to user
          console.error("Registration failed:", error);
        },
      }
    );
  };

  return (
    <Center>
      <AuthForm
        title="✨Register✨"
        fields={fields}
        submitLabel="Register"
        alternateLabel="Already have an account? Login"
        alternatePath="/login"
        onSubmit={handleSubmit}
        isPending={isPending}
      />
    </Center>
  );
} 