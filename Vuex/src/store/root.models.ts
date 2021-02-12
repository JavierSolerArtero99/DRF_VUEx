/** Root State */
export interface RootState {
  loading: boolean;
  currentUser: User;
  snackbar: Snackbar;
  errors: String;
}

interface User {
  id: number;
  username: string;
  password: string;
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
export type SetCurrentUser = Pick<
  User,
  "id" | "username" | "password" | "email" | "bio" | "image" | "isAuthed"
>;
export type SetAuth = {
  username: string;
  email: string;
  password: string;
  changeScreen: any;
  showErrors: any;
};

export const initialRootState: RootState = {
  loading: false,
  currentUser: {
    id: 0,
    username: "",
    password: "",
    email: "",
    image: "",
    bio: "",
    isAuthed: false
  },
  errors: "",
  snackbar: {
    message: "",
    isActive: false,
    type: undefined
  }
};
