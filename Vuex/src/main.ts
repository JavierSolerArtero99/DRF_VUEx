import Vue from "vue";
import VueRouter from 'vue-router';
import App from "./App.vue";
import store from "./store";
import { vuetify } from "./core/plugins";
import { currency } from "./core/filters";
import { Header, NotFound, Products, Home, Login } from "./components";

Vue.use(VueRouter);

Vue.filter("currency", currency);

Vue.config.productionTip = false;

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes: [
    { path: '/', component: App, redirect: '/app' },
    { path: '/app', component: Home, 
      children: [
        { path: 'products', component: Products },
        { path: 'about', component: Products },
      ]
    },
    { path: '/login', component: Login },
    { path: '/register', component: Home },
    // { path: '/app/*', component: NotFound }
  ]
});

console.log(router)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount("#app");
