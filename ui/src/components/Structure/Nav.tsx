import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faHome } from "@fortawesome/free-solid-svg-icons/faHome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink, TextInput, Group, Flex } from "@mantine/core";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/AuthProvider";

export default function Nav() {
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter' && searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery("");
    }
  };

  return (
    <Group justify="space-between" align="center" style={{ width: "100%" }}>
      <TextInput
        placeholder="Search for bad books"
        leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
        value={searchQuery}
        onChange={(event) => setSearchQuery(event.currentTarget.value)}
        onKeyDown={handleKeyPress}
        style={{ width: "300px" }}
      />
      <Flex>
        <NavLink onClick={() => navigate("/")}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Home"
          leftSection={<FontAwesomeIcon icon={faHome} />}
          active={true}
          autoContrast
        />
        {!isAuthenticated && <NavLink onClick={() => navigate("/login", { state: { from: location.pathname }})}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Login"
          leftSection={<FontAwesomeIcon icon={faUser} />}
          active={true}
          autoContrast
        />}
        {isAuthenticated && <NavLink onClick={() => navigate("/account")}
          color="white"
          style={{ padding: "0.5rem" }}
          variant="subtle"
          label="Account"
          leftSection={<FontAwesomeIcon icon={faUser} />}
          active={true}
          autoContrast
        />}
      </Flex>
    </Group>
  );
}
