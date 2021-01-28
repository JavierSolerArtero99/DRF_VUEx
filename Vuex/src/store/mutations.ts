import { MutationTree } from 'vuex';
import { State, User } from './state';
 
export enum MutationType {
  SetUser = 'LOGIN_USER',
  RemoveUser = 'LOGOUT_USER',
  CreateUser = 'CREATE_USER',
  UpdateUser = 'UPDATE_USER',
}

export type Mutations = {
   [MutationType.SetUser](state: State, user: User): void;
   [MutationType.RemoveUser](state: State, user: User): void;
   [MutationType.CreateUser](state: State, user: User): void;
   [MutationType.UpdateUser](state: State, user: User): void;
};

export const mutations: MutationTree<State> & Mutations = {
    [MutationType.SetUser](state, user) {
        state.currentUser = user
    },
    [MutationType.RemoveUser](state) {
        state.currentUser = {
            id: 0,
            name: '',
            email: '',
            username: ''
        }
    },
    [MutationType.CreateUser](state, user) {
        state.currentUser = user
    },
    [MutationType.UpdateUser](state, user) {
        state.currentUser = user
    },
};