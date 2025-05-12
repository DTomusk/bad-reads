import { Card, Image, Text, Badge, Button, Group, Stack } from "@mantine/core";
import { useNavigate } from "react-router-dom";

interface IBookCard {
  title: string;
  author: string;
  picture?: string;
  description: string;
  uuid: string;
}

export default function BookCard({
  title,
  author,
  picture = "",
  description,
  uuid,
}: IBookCard) {
  const navigate = useNavigate();
  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Card.Section>
        <Image src={picture} height={160} alt="Norway" />
      </Card.Section>

      <Group justify="space-between" mt="md" mb="xs">
        <Text fw={500}>{title}</Text>
        <Badge color="orange">{author}</Badge>
      </Group>

      <Text size="sm" c="dimmed">
        {description}
      </Text>

      <Stack>
        <Button
          color="blue"
          fullWidth
          mt="md"
          radius="md"
          onClick={() => navigate(uuid)}
        >
          Rate
        </Button>
      </Stack>
    </Card>
  );
}
