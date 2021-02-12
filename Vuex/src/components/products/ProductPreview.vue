<template>
  <div
    @click="
      () => {
        $router.push({
          name: 'details',
          params: { id: data.product.id },
        });
      }"
    class="productPreview"
  >
    <div class="image-container">
      <img v-bind:src="data.product.image" alt="image" />
    </div>
    <div class="info-container">
      <span class="title">{{ data.product.title }}</span>
      <span class="subtitle">{{ data.product.subtitle }}</span>
      <span class="price">{{ data.product.price }} €</span>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "productPreview",
})
export default class ProductPreview extends Vue {
  data = {
    product: {
      id: 1,
      title: "Shirt",
      subtitle: "Running shirt",
      price: 19.99,
      image:
        "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/shirt.png?raw=true",
    },
  };

  constructor() {
    super();
  }

  mounted() {}
}
</script>

<style scoped>
.productPreview {
  height: 290px;
  width: 230px;

  overflow: hidden;

  padding: 0;

  display: grid;
  grid-template-rows: 70% 30%;
}

.image-container {
  padding: 1rem;

  display: flex;
  justify-content: center;
  align-items: center;

  border-left: 3px solid #5136ff;
  border-right: 3px solid #5136ff;
  border-top: 3px solid #5136ff;

  overflow: hidden;
}

.image-container img {
  max-width: 100%;
  max-height: 100%;
}

.info-container {
  color: white;
  background-color: #5136ff;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.image-container:hover {
  height: 290px;
  border-bottom: 3px solid #5136ff;
  cursor: pointer;
}

.image-container:hover img {
  max-width: 110%;
  max-height: 110%;
}

.image-container:hover ~ .info-container {
  display: none;
}

.title {
  width: 100%;

  padding-left: 1rem;

  font-weight: bold;
  font-size: 1.4rem;
}

.subtitle {
  width: 100%;

  padding-left: 1rem;

  font-weight: lighter;
  font-size: 0.8rem;
}

.price {
  width: 100%;
  padding-right: 1rem;
  text-align: right;

  font-weight: bold;
  font-size: 1.4rem;
}

.container {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 0;

  background-color: crimson;
}
</style>