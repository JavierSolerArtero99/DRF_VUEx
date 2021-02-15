import {
  RootState,
  SetCurrentUser,
  SetAuth,
  Product,
  HomeLogin
} from "./root.models";
import { DefineActionTree, DefineTypes } from "./store.helpers";
import { rootMutationsTypes } from "./root.mutations";

import ApiService from "../common/api.service";
import { destroyToken, saveToken } from "../common/jwt.service";

export interface RootActions {
  setAuth: SetAuth;
  homeLogin: HomeLogin;
  purgeAuth: void;
}

const actions: DefineActionTree<RootActions, RootState> = {
  /* AUTHENTICATION */

  // Authenticaiton
  setAuth({ commit }, { payload }) {
    if (payload.isLogin) {
      // Login
      ApiService.post("users/login", { user: payload })
        .then(({ data }) => {
          saveToken(data.user.token);
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
    } else {
      // Register
      ApiService.post("users/", { user: payload })
        .then(({ data }) => {
          saveToken(data.user.token);
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
    }
  },

  // Home auto login with token
  homeLogin({ commit }, { payload }) {
    ApiService.setHeader();
    ApiService.get("user")
      .then(({ data }) => {
        saveToken(data.user.token);
        commit(rootMutationsTypes.setCurrentUser(data.user));
      })
      .catch(err => {
        console.log("ERROR EN ACTION");
        console.log(err);
      });
  },

  // logout user
  purgeAuth({ commit }) {
    destroyToken();
    commit(rootMutationsTypes.purgeCurrentUser());
  }
};

export const rootActionsTypes: DefineTypes<RootActions> = {
  setAuth: payload => ({ type: "setAuth", payload }),
  purgeAuth: payload => ({ type: "purgeAuth", payload }),
  homeLogin: payload => ({ type: "homeLogin", payload })
};

export default actions;
