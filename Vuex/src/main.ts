import Vue from "vue";
import VueRouter from 'vue-router';
import App from "./App.vue";
import store from "./store";
import { vuetify } from "./core/plugins";
import { currency } from "./core/filters";
import { Header, NotFound, Home, Login, Products, Profile, EditProfile, ProductDetails } from "./components";
import ApiService from "./common/api.service";

Vue.use(VueRouter);

Vue.filter("currency", currency);

Vue.config.productionTip = false;

ApiService.init();

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes: [
    { path: '/', component: App, redirect: '/app' },
    {
      path: '/app', component: Home,
      children: [
        { path: 'products', component: Products },
        { path: 'products/:id', name: 'details', component: ProductDetails },
        { path: 'about', component: Products },
        // {
        //   path: 'profile', component: Profile, beforeEnter: (to, from, next) => {
        //     if (store.getters.currentUser.isAuthed) {
        //       next();
        //     } else next({ path: '/' });
        //   }
        // },
        { path: 'profile', component: Profile },
        { path: 'profile-edit', component: EditProfile }
      ]
    },
    { path: '/login', component: Login },
    { path: '/app/*', component: NotFound }
  ]
});

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount("#app");
