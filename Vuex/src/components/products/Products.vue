<template>
  <div class="products">
    <span>Products</span>
    <router-link to="/">Return home</router-link>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Products",
  computed: {
  },
  mounted() {
      console.log('products mounted')
  },
});
</script>

<style scoped>
</style>