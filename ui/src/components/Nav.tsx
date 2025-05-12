import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faHome } from "@fortawesome/free-solid-svg-icons/faHome";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink } from "@mantine/core";
import { use } from "react";
import { useNavigate } from "react-router-dom";

const navigationData = [
  { label: "Home", icon: <FontAwesomeIcon icon={faHome} />, link: "/" },
  { label: "Login", icon: <FontAwesomeIcon icon={faUser} />, link: "/login" },
];

export default function Nav() {
  // const navigate = useNavigate()
  const links = navigationData.map((item) => (
    <div style={{ display: "flex", flexDirection: "row", padding: "0.5rem" }}>
      <NavLink
        // color="rgb(250, 121, 0)"
        color="orange"
        style={{ padding: "0.5rem" }}
        variant="subtle"
        href={item.link}
        key={item.label}
        label={item.label}
        leftSection={item.icon}
        active={true}
        autoContrast
      />
    </div>
  ));

  return <>{links} </>;
}
