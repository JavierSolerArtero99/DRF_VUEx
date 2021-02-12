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

export default Vue.extend({
  name: "Home",
  components: {
    Header,
    Footer,
  },
  computed: {},
  mounted() {
    ApiService.get(`products`)
      .then(({ data }) => {
        console.log("===SUCCESS===");
        console.log(data);
      })
      .catch((err) => {
        console.log("===ERROR===");
        console.log(err);
      });
  },
});
</script>

<style scoped>
</style>