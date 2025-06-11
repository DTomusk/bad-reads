import { Stack, Image, Card, Title, Text } from "@mantine/core";
import { useNavigate } from "react-router-dom";

export default function BookCardSmall({
    title,
    picture_url,
    id,
}: {
    title: string;
    picture_url: string;
    id: string;
}) {
    const navigate = useNavigate();
    
    return (
        <Card 
            shadow="sm" 
            radius="md" 
            withBorder 
            h="100%" 
            onClick={() => navigate(`/book/${id}`)}
            style={{ cursor: 'pointer' }}
            bg="dark.0"
            styles={{
                root: {
                    transition: 'background-color 0.2s ease',
                    '&:hover': {
                        backgroundColor: 'var(--mantine-color-dark-9)',
                    }
                }
            }}
            p="0"
            m="0"
        >
            <Stack h="100%" justify="space-between" gap="xs">
                {picture_url ? <Image 
                    src={picture_url} 
                    alt={title} 
                    width="100%" 
                    fit="contain" 
                    c="white"
                /> : <Title 
                    order={5} 
                    size="sm" 
                    c="white"
                    m="sm"
                >
                    {title}
                </Title>}

                <Stack gap="xs" align="center">
                    <Text c="white" size="xl">💖💖</Text>
                    <Text c="white" size="xl">💩💩💩💩💩</Text>
                    <Text c="white" size="sm" mb="sm">(9999)</Text>
                </Stack>
            </Stack>
        </Card> 
    )
}