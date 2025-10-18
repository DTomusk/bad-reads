export interface ErrorResponse {
  detail: string;
  errors?: Record<string, string>;
}