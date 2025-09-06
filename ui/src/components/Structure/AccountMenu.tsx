import { faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button, Menu, Text } from "@mantine/core";
import { useAuth } from "../../auth/AuthProvider";
import { useNavigate } from "react-router-dom";

export default function AccountMenu() {
    const { logout } = useAuth();
    const navigate = useNavigate();
    return (
        <Menu transitionProps={{ transition: 'fade-down', duration: 200}} withinPortal={false}>
            <Menu.Target>
                <Button variant="subtle">
                    <FontAwesomeIcon color="white" icon={faUser} style={{marginRight:"1rem"}} />
                    <Text>My Account</Text>
                </Button>
            </Menu.Target>

            <Menu.Dropdown>
                <Menu.Item onClick={() => navigate("/me")}>My Profile</Menu.Item>
                <Menu.Item onClick={() => logout()}>Log out</Menu.Item>
            </Menu.Dropdown>
        </Menu>
    )
}