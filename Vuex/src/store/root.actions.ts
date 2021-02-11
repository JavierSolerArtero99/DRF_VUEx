import { RootState, SetSnackbar, SetCurrentUser, SetAuth } from "./root.models";
import { DefineActionTree, DefineTypes } from "./store.helpers";
import { rootMutationsTypes } from "./root.mutations";

import ApiService from "../common/api.service";

export interface RootActions {
  showSnackbar: SetSnackbar;
  setAuth: SetAuth;
  purgeAuth: void;
}

const actions: DefineActionTree<RootActions, RootState> = {
  showSnackbar({ commit }, { payload }) {
    commit(rootMutationsTypes.setSnackbar({ ...payload, isActive: true }));

    setTimeout(() => {
      commit(rootMutationsTypes.setSnackbar({ ...payload, isActive: false }));
    }, 3000);
  },

  /* AUTHENTICATION */

  // Login
  setAuth({ commit }, { payload }) {
    console.log("PAYLOAD");
    console.log(payload);

    let user: SetCurrentUser = {
      id: 1,
      username: payload.username,
      password: payload.password,
      email: "jasoka@gmail.com",
      bio: "mi bio",
      image: "none"
    };

    ApiService.post("users/login", {user})
      .then(({ data }) => {
        console.log("===SUCCESS===");
        console.log(data);
      })
      .catch(err => {
        console.log("===ERROR===");
        console.log(err.response);
      });

    commit(
      rootMutationsTypes.setCurrentUser({
        ...payload,
        ...user
      })
    );
  },

  purgeAuth({ commit }) {
    commit(rootMutationsTypes.purgeCurrentUser());
  }
};

export const rootActionsTypes: DefineTypes<RootActions> = {
  showSnackbar: payload => ({ type: "showSnackbar", payload }),
  setAuth: payload => ({ type: "setAuth", payload }),
  purgeAuth: payload => ({ type: "purgeAuth", payload })
};

export default actions;
