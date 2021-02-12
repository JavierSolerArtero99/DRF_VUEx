/** Root State */
export interface RootState {
  loading: boolean;
  currentUser: User;
  snackbar: Snackbar;
  errors: String
}

interface User {
  id: number;
  username: string;
  password: string;
  email: string;
  image: string;
  bio: string;
}

interface Snackbar {
  message: string;
  isActive: boolean;
  type?: "success" | "info" | "error";
}

export type SetSnackbar = Pick<Snackbar, "message" | "type">;
export type SetCurrentUser = Pick<
  User,
  "id" | "username" | "password" | "email" | "bio" | "image"
>;
export type SetAuth = { username: string; email: string; password: string; };

export const initialRootState: RootState = {
  loading: false,
  currentUser: {
    id: 0,
    username: "",
    password: "",
    email: "",
    image: "",
    bio: ""
  },
  errors: "",
  snackbar: {
    message: "",
    isActive: false,
    type: undefined
  }
};
