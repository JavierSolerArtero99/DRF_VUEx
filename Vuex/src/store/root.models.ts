/** Root State */
export interface RootState {
  loading: boolean;
  currentUser: User;
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

export type SetCurrentUser = Pick<
  User,
  "id" | "username" | "password" | "email" | "bio" | "image" | "isAuthed"
>;
export type SetAuth = {
  username: string;
  email: string;
  password: string;
  isLogin: boolean;
  changeScreen: any;
  showErrors: any;
};

export type HomeLogin = {
  
} 

export type Product = {
  id: number;
  title: string;
  subtitle: string;
  description: string;
  price: number
  image: string;
  author: User;
};

export type Comment = {
  id: number;
  body: string;
  author: User,
  product: Product;
}

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
};
