import { initialRootState, RootState } from "./root.models";
import { DefineMutationTree, DefineTypes } from "./store.helpers";

export interface RootMutations {
  setLoading: RootState["loading"];
  setSnackbar: RootState["snackbar"];
  setCurrentUser: RootState["currentUser"];
  setErrors: RootState["errors"];
  purgeCurrentUser: void;
}

const mutations: DefineMutationTree<RootMutations, RootState> = {
  setLoading(state, { payload }) {
    state.loading = payload;
  },
  setSnackbar(state, { payload }) {
    state.snackbar = {
      message: payload.message,
      type: payload.type || "success",
      isActive: payload.isActive
    };
  },
  setErrors(state, { payload }) {
    state.errors = payload
  },
  setCurrentUser(state, { payload }) {
    state.currentUser = {
      id: payload.id,
      username: payload.username,
      password: payload.password,
      email: payload.email,
      image: payload.image,
      bio: payload.bio
    };
  },
  purgeCurrentUser(state) {
    state.currentUser = {
      id: 0,
      username: "",
      email: "",
      image: "",
      bio: ""
    };
  }
};

export const rootMutationsTypes: DefineTypes<RootMutations> = {
  setLoading: payload => ({ type: "setLoading", payload }),
  setSnackbar: payload => ({ type: "setSnackbar", payload }),
  setCurrentUser: payload => ({ type: "setCurrentUser", payload }),
  setErrors: payload => ({ type: "setErrors", payload }),
  purgeCurrentUser: payload => ({ type: "purgeCurrentUser", payload })
};

export default mutations;
