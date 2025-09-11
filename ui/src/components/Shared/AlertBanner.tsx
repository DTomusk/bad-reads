import { Alert, List, Text } from "@mantine/core";
import { useState } from "react";

interface AlertBannerProps {
  title: string;
  message: string[] | string;
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
      {Array.isArray(message) ? (
        <List spacing="xs" size="sm" withPadding>
          {message.map((msg, i) => (
            <List.Item key={i}>{msg}</List.Item>
          ))}
        </List>
      ) : (
        <Text size="sm">{message}</Text>
      )}
    </Alert>
  );
}