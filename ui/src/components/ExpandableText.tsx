import { useState } from 'react';
import { Text, Button, Box } from '@mantine/core';

interface ExpandableTextProps {
  text: string;
  maxChars?: number;
}

export function ExpandableText({ text, maxChars = 500 }: ExpandableTextProps) {
  const [expanded, setExpanded] = useState(false);

  const isLong = text.length > maxChars;
  const displayText = expanded || !isLong ? text : `${text.slice(0, maxChars)}...`;

  return (
    <Box>
      <Text>{displayText}</Text>
      {isLong && (
        <Button variant="outline" size="xs" onClick={() => setExpanded((prev) => !prev)}>
          {expanded ? 'Show less' : 'Read more'}
        </Button>
      )}
    </Box>
  );
}
