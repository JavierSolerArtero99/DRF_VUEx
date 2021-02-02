import { DefineGetterTree } from "../../store.helpers";
import { RootState } from "../../root.models";
import { UserState, CartProductsGetter, CheckoutStatus } from "./cart.models";

export interface UserGetters {
  checkoutStatus: CheckoutStatus;
  cartProducts: CartProductsGetter[];
  cartTotalPrice: number;
}

const getters: DefineGetterTree<UserState, UserState, RootState> = {
  checkoutStatus: state => state.checkoutStatus,

  cartProducts: (state, getters, rootState) =>
    state.added.map(({ id, quantity }) => {
      const product = rootState.products!.all.find(p => p.id === id)!;
      return {
        title: product.title,
        price: product.price,
        quantity,
      };
    }),

  cartTotalPrice: (state, getters) =>
    getters.cartProducts.reduce(
      (total, product) => total + product.price! * product.quantity,
      0,
    ),
};

export default getters;
