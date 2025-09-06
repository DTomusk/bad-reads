import { Alert, Text } from "@mantine/core";
import { useState } from "react";

interface AlertBannerProps {
  title: string;
  message: string;
  type: "error" | "success" | "warning" | "info";
}

export default function AlertBanner({ title, message, type }: AlertBannerProps) {

    const [show, setShow] = useState(true);

    if (!show) {
        return null;
    }

    return (
    <Alert 
    withCloseButton 
    closeButtonLabel="Dismiss" 
    variant="filled"
    onClose={() => setShow(false)}
    color={type === "error" ? "red" : type === "success" ? "green" : type === "warning" ? "yellow" : "blue"}>
      <Text fw={700}>{title}</Text>
      <Text>{message}</Text>
    </Alert>
  );
}