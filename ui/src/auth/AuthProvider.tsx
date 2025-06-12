import { createContext, useContext, useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';

interface JwtPayload {
  exp: number;
  iat: number;
  sub: string;
}

interface AuthContextValue {
  isAuthenticated: boolean;
  login: (token: string) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const checkToken = () => {
    const token = localStorage.getItem('token');
    if (!token) {
      setIsAuthenticated(false);
      return;
    }

    try {
      const { exp } = jwtDecode<JwtPayload>(token);
      if (Date.now() >= exp * 1000) {
        localStorage.removeItem('token');
        setIsAuthenticated(false);
      } else {
        setIsAuthenticated(true);
      }
    } catch (err) {
      console.error('Invalid token:', err);
      setIsAuthenticated(false);
    }
  };

  useEffect(() => {
    checkToken();
  }, []);

  const login = (token: string) => {
    localStorage.setItem('token', token);
    checkToken();
  };

  const logout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
