/** Root State */
export interface RootState {
  loading: boolean;
  currentUser: User;
  snackbar: Snackbar;
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
export type SetAuth = { username: string; password: string };

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
  snackbar: {
    message: "",
    isActive: false,
    type: undefined
  }
};
