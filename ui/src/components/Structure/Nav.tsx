import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink, TextInput, Group, Flex, Title } from "@mantine/core";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/AuthProvider";
import BadReadLogo from "../BadReadLogo";
import AccountMenu from "./AccountMenu";
import { useBreakpoints } from "../../hooks/useBreakpoints";

export default function Nav() {
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const { isExtraLarge } = useBreakpoints();

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter' && searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery("");
    }
  };

  return (
    <Flex justify="space-between" align="center" gap="lg" w={isExtraLarge ? "100%" : "70%"} h="100%" wrap="nowrap">
      <Group onClick={() => navigate("/")} style={{ cursor: 'pointer' }}>
        <BadReadLogo />
        <Title visibleFrom="xs" style={{ color: "white" }}>Bad Reads</Title>
      </Group>
      <Group>
        <TextInput
          placeholder="Search for bad books"
          leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
          value={searchQuery}
          onChange={(event) => setSearchQuery(event.currentTarget.value)}
          onKeyDown={handleKeyPress}
          style={{ maxWidth: "300px" }}
        />
        {!isAuthenticated && <NavLink visibleFrom="sm" onClick={() => navigate("/login", { state: { from: location.pathname }})}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Login"
          leftSection={<FontAwesomeIcon icon={faUser} />}
          active={true}
          autoContrast
          w="auto"
        />}
        {isAuthenticated && <AccountMenu />}
      </Group>
    </Flex>
  );
}
