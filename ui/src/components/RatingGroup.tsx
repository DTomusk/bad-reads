import { Rating } from "@mantine/core";
import { faPoo, faHeart } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

interface RatingGroupProps {
  changeFunction: (value: number) => void;
  icon?: "heart" | "poo";
}

const setIconColour = (color?: string) => ({
  color: color,
});

export default function RatingGroup({
  changeFunction,
  icon = "poo"
}: RatingGroupProps) {
  const iconMap: Record<string, IconDefinition> = {
    heart: faHeart,
    poo: faPoo
  };

  const selectedIcon = iconMap[icon];

  return (
    <Rating
      fractions={4}
      size="lg"
      onChange={changeFunction}
      emptySymbol={
        <FontAwesomeIcon
          icon={selectedIcon}
          size="5x"
          style={setIconColour("#803900")}
        />
      }
      fullSymbol={
        <FontAwesomeIcon
          icon={selectedIcon}
          size="5x"
          style={setIconColour("ffb01b")}
        />
      }
    />
  );
}
