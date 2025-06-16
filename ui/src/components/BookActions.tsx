import { Group, Button, Flex } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthProvider";

interface BookActionsProps {
  bookId: string;
  showMore?: boolean;
  onRateClick: () => void;
}

export default function BookActions({ bookId, showMore = false, onRateClick }: BookActionsProps) {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  return (
    <Flex justify="flex-start" gap="md">
      {showMore && <Button
        color="blue"
        radius="md"
        onClick={() => navigate(`/book/${bookId}`)}
        w="100%"
      >
        More
      </Button>}
      <Button
        color="secondary.0"
        radius="md"
        onClick={onRateClick}
        disabled={!isAuthenticated}
        w="100%"
      >
        Rate
      </Button>
    </Flex>
  );
} 