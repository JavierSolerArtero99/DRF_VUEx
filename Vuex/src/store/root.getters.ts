import { DefineGetterTree } from "./store.helpers";
import { RootState } from "./root.models";

export interface RootGetters {
  snackbar: RootState["snackbar"];
  currentUser: RootState["currentUser"];
  errors: RootState["errors"];
}

const getters: DefineGetterTree<RootGetters, RootState> = {
  snackbar: state => state.snackbar,
  currentUser: state => state.currentUser,
  errors: state => state.errors
};

export default getters;
