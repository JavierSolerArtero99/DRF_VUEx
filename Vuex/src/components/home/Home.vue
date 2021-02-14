<template>
  <div>
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from "vue";

import Header from "../shared/Header.vue";
import Footer from "../shared/Footer.vue";

import ApiService from "../../common/api.service";
import { store } from "../../store";
import { destroyToken, getToken } from "../../common/jwt.service";

export default Vue.extend({
  name: "Home",
  components: {
    Header,
    Footer,
  },
  computed: {},
  mounted() {
    if (getToken()) {
      console.log("There is TOKEN");
      console.log(getToken());  
      ApiService.setHeader()    
      ApiService.get("user").then(data => {
        console.log("THERE IS USER");
        console.log(data);
      }).catch(err => {
        console.log("ERROR");
        console.log(err);
      })
    } else {
      console.log("There is NOOOOO TOKEN");
    }
  },
});
</script>

<style scoped>
</style>