<template>
  <div>
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from "vue";

import Component from "vue-class-component";
import Header from "../shared/Header.vue";
import Footer from "../shared/Footer.vue";

import ApiService from "../../common/api.service";
import { store, storeTypes } from "../../store";
import { destroyToken, getToken } from "../../common/jwt.service";

@Component({
  name: "home",
  components: {
    Header,
    Footer,
  },
})
export default class Home extends Vue {
  constructor() {
    super();
  }

  mounted() {
    if (getToken()) {
      store.dispatch(storeTypes.root.actions!.homeLogin({})).then(() => {});
    } else {
      console.log("There is NOOOOO TOKEN");
    }
  }
}
</script>

<style scoped>
</style>