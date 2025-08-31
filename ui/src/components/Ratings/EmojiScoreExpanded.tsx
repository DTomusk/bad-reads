import { Text, Stack, Group } from "@mantine/core";

interface EmojiScoreExpandedProps {
    love_score: number;
    shit_score: number;
    number_of_ratings: number;
    size?: "small" | "medium" | "large";
    align?: "left" | "center" | "right";
}

export default function EmojiScoreExpanded({ love_score, shit_score, number_of_ratings, size = "medium", align = "center" }: EmojiScoreExpandedProps) {
    const createEmojiString = (score: number, emoji: string) => {
        const filledCount = Math.round(score);
        const filledEmojis = emoji.repeat(filledCount);
        const emptyCount = 5 - filledCount;
        const emptyEmojis = emoji.repeat(emptyCount);
        
        return (
            <>
                <span>{filledEmojis}</span>
                <span style={{ opacity: 0.5 }}>{emptyEmojis}</span>
            </>
        );
    };

    return (
        <Stack gap="md" align={align}>
            <Group>
                <Text size={size === "small" ? "16px" : size === "medium" ? "20px" : "24px"}>{createEmojiString(love_score, "💖")}</Text>
                <Text size="16px">{love_score.toFixed(1)}</Text>
            </Group>
            <Group>
                <Text size={size === "small" ? "16px" : size === "medium" ? "20px" : "24px"}>{createEmojiString(shit_score, "💩")}</Text>
                <Text size="16px">{shit_score.toFixed(1)}</Text>
            </Group>
            {number_of_ratings > 0 && <Text size="16px" fw="bold" mx="xs">{number_of_ratings > 1 ? `${number_of_ratings} ratings` : `${number_of_ratings} rating`}</Text>}
            {number_of_ratings === 0 && <Text size="16px" fw="bold" mx="xs">No ratings yet</Text>}
        </Stack>
    )
}