import { useMediaQuery } from "@mantine/hooks";

export function useBreakpoints() {
    const isExtraSmall = useMediaQuery("(max-width: 36em)"); 
    const isSmall = useMediaQuery("(max-width: 48em)");
    const isMedium = useMediaQuery("(max-width: 62em)");
    const isLarge = useMediaQuery("(max-width: 75em)");
    const isExtraLarge = useMediaQuery("(max-width: 90em)");

    return { isExtraSmall, isSmall, isMedium, isLarge, isExtraLarge };
}