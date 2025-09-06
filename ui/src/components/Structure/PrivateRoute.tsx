import { useNavigate } from "react-router-dom";
import { useAuth } from "../../auth/AuthProvider";
import { PropsWithChildren, useEffect } from "react";

export default function PrivateRoute({ children }: PropsWithChildren) {
  const { isAuthenticated, isLoading } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      navigate("/");
    }
  }, [isLoading, isAuthenticated, navigate]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return null;
  }

  return <>{children}</>;
}