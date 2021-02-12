<template>
  <div class="products">
    <div class="container">
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
      <ProductPreview />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

import ProductPreview from "../products/ProductPreview.vue";

@Component({
  name: "products",
  components: {
    ProductPreview
  }
})
export default class Products extends Vue {
  data = {
  };

  constructor() {
    super();
  }

  mounted() {}
}
</script>

<style scoped>
.products {
  height: 90%;
  width: 100%;

  padding: 0;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container {
  height: 100%;
  width: 100%;

  display: inline-grid;
  grid-template-columns: repeat( 4, minmax(230px, 1fr));;
  grid-gap: 3px;
  justify-items: center;
  align-items: center;

  overflow: hidden;

  padding: 0;
}


</style>