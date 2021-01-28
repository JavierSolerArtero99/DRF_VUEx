export type User = {
  id: number;
  name: string;
  email: string;
  username: string;
};
export type State = {
  loading: boolean;
  currentUser: User;
};
export const state: State = {
  loading: false,
  currentUser: {
      id: 0,
      name: '',
      email: '',
      username: ''
  },
};