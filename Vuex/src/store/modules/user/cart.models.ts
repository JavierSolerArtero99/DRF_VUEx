/** User State */
export interface UserState {
  added: AddedItem[];
  checkoutStatus: CheckoutStatus;
}

/** Type to extend the RootState interface */
export type ExtendedUserState = { user?: UserState };

export interface AddedItem {
  id: number;
  quantity: number;
}

export interface CartItem extends AddedItem {
  title: string;
  price: number;
}

export type CartProductsGetter = Omit<CartItem, "id">;

export type CheckoutStatus = "successful" | "failed" | null;

export const initialCartState: UserState = {
  added: [],
  checkoutStatus: null,
};
