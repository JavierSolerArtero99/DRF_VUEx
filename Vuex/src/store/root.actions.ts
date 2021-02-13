import { RootState, SetCurrentUser, SetAuth, Product } from "./root.models";
import { DefineActionTree, DefineTypes } from "./store.helpers";
import { rootMutationsTypes } from "./root.mutations";

import ApiService from "../common/api.service";

export interface RootActions {
  setAuth: SetAuth;
  purgeAuth: void;
}

const actions: DefineActionTree<RootActions, RootState> = {
  /* AUTHENTICATION */

  // Login
  setAuth({ commit }, { payload }) {
    ApiService.post("users/login", { payload })
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
  },
};

export const rootActionsTypes: DefineTypes<RootActions> = {
  setAuth: payload => ({ type: "setAuth", payload }),
  purgeAuth: payload => ({ type: "purgeAuth", payload })
};

export default actions;
