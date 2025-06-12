import { Center } from "@mantine/core";
import { useLogin } from "../hooks/useLogin";
import { useNavigate } from "react-router-dom";
import AuthForm from "../components/AuthForm";

export default function Login() {
  const navigate = useNavigate();
  const { mutate: login, isPending } = useLogin();

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
  ];

  const handleSubmit = (values: Record<string, string>) => {
    login(
      {
        username: values.email,
        password: values.password,
      },
      {
        onSuccess: (data) => {
          // Store the token in localStorage
          localStorage.setItem("token", data.access_token);
          // Redirect to home page
          navigate("/");
        },
        onError: (error) => {
          // TODO: Show error message to user
          console.error("Login failed:", error);
        },
      }
    );
  };

  return (
    <Center>
      <AuthForm
        fields={fields}
        submitLabel="Login"
        alternateLabel="Don't have an account? Register"
        alternatePath="/register"
        onSubmit={handleSubmit}
        isPending={isPending}
      />
    </Center>
  );
}
