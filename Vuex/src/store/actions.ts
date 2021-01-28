import { ActionContext, ActionTree } from 'vuex'
import { Mutations, MutationType } from './mutations'
import { State } from './state'
 
export enum ActionTypes {
  GetCurrentUser = 'GET_CURRENT_USER',
}

type ActionAugments = Omit<ActionContext<State, State>, 'commit'> & {
  commit<K extends keyof Mutations>(
    key: K,
    payload: Parameters<Mutations[K]>[1]
  ): ReturnType<Mutations[K]>;
}

export type Actions = {
  [ActionTypes.GetCurrentUser](context: ActionAugments): void;
}

export const actions: ActionTree<State, State> & Actions = {
  async [ActionTypes.GetCurrentUser]({ commit }) {
    commit(MutationType.SetUser,
      {
        id: 1,
        name: 'Create a new programming language',
        email: "The programing language should have full typescript support ",
        username: "Emmanuel John",
      }
    )
  },
}