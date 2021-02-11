
/** Root State */
export interface RootState {
  loading: boolean;
  currentUser: User;
  snackbar: Snackbar;
}

interface User {
  id: number;
  username: string;
  email: string;
  image: string;
  bio: string;
  isAuthed: boolean;
}

interface Snackbar {
  message: string;
  isActive: boolean;
  type?: "success" | "info" | "error";
}

export type SetSnackbar = Pick<Snackbar, "message" | "type">;
export type SetCurrentUser = Pick<User, "id" | "username" | "email" | "bio" | "image" | "isAuthed">;
export type SetAuth = { username: string, password: string };

export const initialRootState: RootState = {
  loading: false,
  currentUser: {
    id: 0,
    username: "",
    email: "",
    image: "",
    bio: "",
    isAuthed: false
  },
  snackbar: {
    message: "",
    isActive: false,
    type: undefined,
  },
};
