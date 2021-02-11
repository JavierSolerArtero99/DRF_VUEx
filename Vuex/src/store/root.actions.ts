import { RootState, SetSnackbar, SetCurrentUser, SetAuth } from "./root.models";
import { DefineActionTree, DefineTypes } from "./store.helpers";
import { rootMutationsTypes } from "./root.mutations";

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

  setAuth({ commit }, { payload }) {
    console.log(payload);
    
    let user: SetCurrentUser = {
      id: 1,
      username: payload.username,
      email: "jasoka@gmail.com",
      bio: "mi bio",
      image: "none",
      isAuthed: true
    };

    commit(rootMutationsTypes.setCurrentUser({ ...payload, ...user}));
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
