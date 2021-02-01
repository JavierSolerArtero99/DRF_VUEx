<template>
  <div>
    <Header />
    <router-view/>
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from "vue";

import Header from "../shared/Header.vue"
import Footer from "../shared/Footer.vue"

export default Vue.extend({
  name: "Home",
  components: {
    Header,
    Footer
  },
  computed: {
  },
  mounted() {
  },
});
</script>

<style scoped>
</style>