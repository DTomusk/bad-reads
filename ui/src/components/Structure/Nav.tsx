import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faHome } from "@fortawesome/free-solid-svg-icons/faHome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink, TextInput, Group, Flex } from "@mantine/core";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/AuthProvider";
import BadReadLogo from "../BadReadLogo";

export default function Nav() {
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();
  const { isAuthenticated, logout } = useAuth();

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter' && searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery("");
    }
  };

  return (
    <Flex justify="space-between" align="center" gap="lg" w="100%">
      <Group onClick={() => navigate("/")} style={{ cursor: 'pointer' }}>
        <BadReadLogo />
        <h1 style={{ color: "white" }}>Bad Reads</h1>
      </Group>
      <Group>
        <TextInput
          placeholder="Search for bad books"
          leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
          value={searchQuery}
          onChange={(event) => setSearchQuery(event.currentTarget.value)}
          onKeyDown={handleKeyPress}
          style={{ width: "300px" }}
        />
      
        <NavLink onClick={() => navigate("/")}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Home"
          leftSection={<FontAwesomeIcon icon={faHome} />}
          active={true}
          autoContrast
          w="auto"
        />
        {!isAuthenticated && <NavLink onClick={() => navigate("/login", { state: { from: location.pathname }})}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Login"
          leftSection={<FontAwesomeIcon icon={faUser} />}
          active={true}
          autoContrast
          w="auto"
        />}
        {isAuthenticated && <NavLink onClick={() => logout()}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Log out"
          leftSection={<FontAwesomeIcon icon={faUser} />}
          active={true}
          autoContrast
          w="auto"
        />}
      </Group>
    </Flex>
  );
}
