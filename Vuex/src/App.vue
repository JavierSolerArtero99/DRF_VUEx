<template>
  <div style="height: 100%">
    <router-view style="height: 100%" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import store, { storeTypes } from "./store";
import { RootState } from "./store/root.models";
import { Loader, Header, Footer } from "./components";

export default Vue.extend({
  name: "App",
  components: { Loader , Header, Footer },
  created() {
    this.reloadProducts();
  },
  methods: {
    reloadProducts() {
    }
  },
});
</script>

<style scoped>
#app{
  width: 100%;
  height: 100%;
  min-height: 100%;

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
