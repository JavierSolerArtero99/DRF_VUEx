import { initialRootState, RootState } from "./root.models";
import { DefineMutationTree, DefineTypes } from "./store.helpers";

export interface RootMutations {
  setLoading: RootState["loading"];
  setCurrentUser: RootState["currentUser"];
  purgeCurrentUser: void;
}

const mutations: DefineMutationTree<RootMutations, RootState> = {
  setLoading(state, { payload }) {
    state.loading = payload;
  },
  setCurrentUser(state, { payload }) {
    state.currentUser = {
      id: payload.id,
      username: payload.username,
      password: "",
      email: payload.email,
      image: payload.image,
      bio: payload.bio,
      isAuthed: true
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
      isAuthed: false
    }
  },
};

export const rootMutationsTypes: DefineTypes<RootMutations> = {
  setLoading: payload => ({ type: "setLoading", payload }),
  setCurrentUser: payload => ({ type: "setCurrentUser", payload }),
  purgeCurrentUser: payload => ({ type: "purgeCurrentUser", payload })
};

export default mutations;
