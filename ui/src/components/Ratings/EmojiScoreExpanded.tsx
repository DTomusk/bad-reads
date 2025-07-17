import { Text, Stack } from "@mantine/core";

interface EmojiScoreExpandedProps {
    love_score: number;
    shit_score: number;
}

export default function EmojiScoreExpanded({ love_score, shit_score }: EmojiScoreExpandedProps) {
    const createEmojiString = (score: number, emoji: string) => {
        const filledCount = Math.ceil(score);
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
        <Stack gap="xs">
            <Text>{createEmojiString(love_score, "💖")} {love_score}</Text>
            <Text>{createEmojiString(shit_score, "💩")} {shit_score}</Text>
        </Stack>
    )
}