import { faHome, faUser } from "@fortawesome/free-solid-svg-icons";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink, TextInput, Group, Flex, Title } from "@mantine/core";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/AuthProvider";
import { useMediaQuery } from "@mantine/hooks";
import BadReadLogo from "../BadReadLogo";

export default function Nav() {
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const isCompact = useMediaQuery("(max-width: 560px)");

  const navigationData = [
    { label: "Home", icon: <FontAwesomeIcon icon={faHome} />, link: "/" },
    {
      label: isAuthenticated ? "Account" : "Login",
      icon: <FontAwesomeIcon icon={faUser} />,
      link: isAuthenticated ? "/account" : "/login",
    },
  ];

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter" && searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery("");
    }
  };

  const links = navigationData.map((item) => (
    <div
      key={item.label}
      style={{
        display: "flex",
        flexDirection: "row",
        padding: "0.5rem",
      }}
    >
      <NavLink
        onClick={() => navigate(item.link)}
        color="white"
        style={{ padding: "0.5rem" }}
        variant="subtle"
        label={item.label}
        leftSection={item.icon}
        active={true}
        autoContrast
      />
    </div>
  ));

  return (
    <Group
      gap={0}
      justify="space-between"
      align="center"
      style={{ width: "100%" }}
    >
      {isCompact ? (
        <>
          <Group>
            <div onClick={() => navigate("/")} style={{ cursor: "pointer" }}>
              <BadReadLogo />
              {/* <h style={{ color: "white" }}>Bad Reads</h1> */}
            </div>
            <Group>{links}</Group>
          </Group>
          <TextInput
            placeholder="Search for bad books"
            leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
            value={searchQuery}
            onChange={(event) => setSearchQuery(event.currentTarget.value)}
            onKeyDown={handleKeyPress}
            style={{ margin: "0.75rem auto" }}
          />
        </>
      ) : (
        <>
          <TextInput
            placeholder="Search for bad books"
            leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
            value={searchQuery}
            onChange={(event) => setSearchQuery(event.currentTarget.value)}
            onKeyDown={handleKeyPress}
            style={{ width: "300px" }}
          />{" "}
          <Group>{links}</Group>
        </>
      )}
    </Group>
  );
}
