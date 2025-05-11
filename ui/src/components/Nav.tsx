import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faHome } from "@fortawesome/free-solid-svg-icons/faHome";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { NavLink } from "@mantine/core";

const navigationData = [
  { label: "Home", icon: <FontAwesomeIcon icon={faHome} />, link: "/" },
  { label: "Login", icon: <FontAwesomeIcon icon={faUser} />, link: "/login" },
];

export default function Nav() {
  const links = navigationData.map((item) => (
    <NavLink
      color="red"
      variant="filled"
      href={item.link}
      key={item.label}
      label={item.label}
      leftSection={item.icon}
      active={true}
    />
  ));

  return <>{links} </>;
}
