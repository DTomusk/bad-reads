import { Group, Text } from "@mantine/core";

interface EmojiScoreProps {
    love_score: number;
    shit_score: number;
}

export default function EmojiScore({ love_score, shit_score }: EmojiScoreProps) {
    return (
        <Group gap="xs">
            <Text>💖 {love_score}</Text>
            <Text>💩 {shit_score}</Text>
        </Group>
    )
}