import { Group, Button } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthProvider";

interface BookActionsProps {
  bookId: string;
  onRateClick: () => void;
}

export default function BookActions({ bookId, onRateClick }: BookActionsProps) {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  return (
    <Group justify="flex-start" mt="auto">
      <Button
        color="blue"
        radius="md"
        onClick={() => navigate(`/book/${bookId}`)}
      >
        More
      </Button>
      <Button
        color="orange"
        radius="md"
        onClick={onRateClick}
        disabled={!isAuthenticated}
      >
        Rate
      </Button>
    </Group>
  );
} 