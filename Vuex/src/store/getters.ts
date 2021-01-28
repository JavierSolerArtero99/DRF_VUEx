import { GetterTree } from 'vuex'
import { State, User } from './state'
 
export type Getters = {
  getCurrentUser(state: State): () => User | undefined;
}
 
export const getters: GetterTree<State, State> & Getters = {
  getCurrentUser: (state) => () => {
    return state.currentUser;
  }
}