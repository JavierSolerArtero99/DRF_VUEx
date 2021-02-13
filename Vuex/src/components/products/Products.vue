<template>
  <div class="products">
    <div class="container">
      <ProductPreview
        v-for="product in data.products"
        v-bind:key="product.id"
        :product="product"
      />
    </div>
    <Pagination :limit="10" :offset="1" :total="100" />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

import ProductPreview from "./ProductPreview.vue";
import Pagination from "../shared/Pagination.vue";

@Component({
  name: "products",
  components: {
    ProductPreview,
    Pagination,
  },
})
export default class Products extends Vue {
  data = {
    products: [],
  };

  constructor() {
    super();
  }

  mounted() {
    for (let i = 0; i < 10; i++) {
      this.data.products.push({
        id: i+1,
        title: "Shirt",
        subtitle: "Running shirt",
        price: 19.99,
        description: "An amazing shirt to go running every day and get fit",
        image:
          "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/shirt.png?raw=true",
      });
    }
  }
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
  height: 80%;
  width: 100%;

  display: inline-grid;
  grid-template-columns: repeat(5, minmax(190px, 1fr));
  justify-items: center;
  align-items: center;

  overflow: hidden;
  padding: 0;
}
</style>