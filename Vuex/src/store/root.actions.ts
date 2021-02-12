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
    let user = {
      username: payload.username,
      email: payload.email,
      password: payload.password,
      bio: "mi bio",
      image: "none",
      isAuthed: true
    };

    ApiService.post("users/login", { user })
      .then(({ data }) => {
        commit(rootMutationsTypes.setCurrentUser(data.user));
        payload.changeScreen();
      })
      .catch(err => {
        let errors = "";
        for (var i in err.response.data.user) {
          errors += `${i}: ${err.response.data.user[i]}`;
        }
        payload.showErrors(errors);
      });
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
