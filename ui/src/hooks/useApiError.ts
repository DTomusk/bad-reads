import { useState } from "react";

export function useApiErrorHandler() {
  const [showErrorAlert, setShowErrorAlert] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | string[]>("");

  const handleError = (error: any) => {
    const apiError = error?.response?.data;
    console.error("API Error:", apiError);

    if (apiError?.errors && typeof apiError.errors === "object") {
      setErrorMessage(Object.values(apiError.errors));
    } else if (apiError?.detail) {
      setErrorMessage(apiError.detail);
    } else {
      setErrorMessage("Something went wrong. Please try again.");
    }

    setShowErrorAlert(true);
  };

  const clearError = () => {
    setShowErrorAlert(false);
    setErrorMessage("");
  };

  return {
    showErrorAlert,
    errorMessage,
    handleError,
    clearError,
  };
}
