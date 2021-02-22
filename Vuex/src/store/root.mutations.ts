import { initialRootState, RootState } from "./root.models";
import { DefineMutationTree, DefineTypes } from "./store.helpers";

export interface RootMutations {
  toggleLoading: RootState["isLoading"];
  setCurrentUser: RootState["currentUser"];
  purgeCurrentUser: void;
}

const mutations: DefineMutationTree<RootMutations, RootState> = {
  toggleLoading(state, { payload }) {
    state.isLoading = payload;
  },
  setCurrentUser(state, { payload }) {
    state.currentUser = {
      id: payload.id,
      username: payload.username,
      password: "",
      email: payload.email,
      image: payload.image,
      bio: payload.bio,
      isAuthed: true,
      isAdmin: false
    }
  },
  purgeCurrentUser(state) {
    state.currentUser = {
      id: 0,
      username: "",
      password: "",
      email: "",
      image: "",
      bio: "",
      isAuthed: false,
      isAdmin: false
    }
  },
};

export const rootMutationsTypes: DefineTypes<RootMutations> = {
  toggleLoading: payload => ({ type: "toggleLoading", payload }),
  setCurrentUser: payload => ({ type: "setCurrentUser", payload }),
  purgeCurrentUser: payload => ({ type: "purgeCurrentUser", payload })
};

export default mutations;
