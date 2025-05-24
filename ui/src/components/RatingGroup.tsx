import { Rating } from "@mantine/core";

import { faPoo } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const setIconColour = (color?: string) => ({
  color: color,
});

export default function RatingGroup({
  changeFunction,
}: {
  changeFunction: () => void;
}) {
  return (
    <Rating
      fractions={4}
      size={"lg"}
      onChange={changeFunction}
      emptySymbol={
        <FontAwesomeIcon
          icon={faPoo}
          size="5x"
          style={setIconColour("#803900")}
        />
      }
      fullSymbol={
        <FontAwesomeIcon
          icon={faPoo}
          size="5x"
          style={setIconColour("ffb01b")}
        />
      }
    />
  );
}
