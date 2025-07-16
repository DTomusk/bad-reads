import {
  Text,
  Stack,
  Image,
  Flex,
  Box,
} from "@mantine/core";
import { TBook } from "../types/book";
import { useNavigate } from "react-router-dom";
import "../styles.css";

export default function BookCard({
  title,
  authors,
  picture_url = "",
  id,
}: TBook) {
  const navigate = useNavigate();

  return (
    <>
      <Flex
        gap="md"
        p="lg"
        h="10rem"
      >
        <Box>
          <Image 
            src={picture_url} 
            height="100%"
            alt={`${title} image`} 
            fit="contain"
            onClick={() => navigate(`/book/${id}`)}
            style={{ cursor: "pointer" }}
          />
        </Box>

        <Stack h="100%" style={{ flex: 1 }}>
          <Text 
            fw={500} 
            size="lg" 
            onClick={() => navigate(`/book/${id}`)} 
            className="hover-underline"
            lineClamp={2}
            >{title}</Text>
          <Text>{authors.join(", ")}</Text>
        </Stack>
      </Flex>
    </>
  );
}
