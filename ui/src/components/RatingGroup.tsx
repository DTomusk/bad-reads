import { Rating, Text, Stack } from "@mantine/core";
import { faPoo, faHeart } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";
import { useState } from "react";

interface RatingGroupProps {
  changeFunction: (value: number) => void;
  icon?: "heart" | "poo";
  value: number;
  getRatingText: (value: number) => string;
  filledColor?: string;
}

const setIconColour = (color?: string) => ({
  color: color,
});

export default function RatingGroup({
  changeFunction,
  icon = "poo",
  value,
  getRatingText,
  filledColor = "var(--mantine-color-highlight-0)"
}: RatingGroupProps) {
  const [hoverValue, setHoverValue] = useState<number | null>(null);
  const [selectedValue, setSelectedValue] = useState<number>(value);
  const iconMap: Record<string, IconDefinition> = {
    heart: faHeart,
    poo: faPoo
  };

  const selectedIcon = iconMap[icon];

  const handleChange = (newValue: number) => {
    setSelectedValue(newValue);
    changeFunction(newValue);
  };

  const handleHover = (newValue: number | null) => {
    setHoverValue(newValue === -1 ? null : newValue);
  };

  return (
    <Stack align="center" gap="xs">
      <Rating
        fractions={2}
        size="xl"
        value={value}
        onChange={handleChange}
        onHover={handleHover}
        emptySymbol={
          <FontAwesomeIcon
            icon={selectedIcon}
            size="4x"
            style={setIconColour("gray")}
          />
        }
        fullSymbol={
          <FontAwesomeIcon
            icon={selectedIcon}
            size="4x"
            style={setIconColour(filledColor)}
          />
        }
      />
      <Text size="sm" c="dimmed">
        {getRatingText(hoverValue ?? selectedValue)}
      </Text>
    </Stack>
  );
}
