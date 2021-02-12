<template>
  <div class="product">
    <div class="container">
      <div class="image-container">
        <img v-bind:src="data.product.image" alt="image" />
      </div>
      <div class="info-container">
        <span class="price">{{ data.product.price }} <span class="price-sufix">€</span></span>

        <h2 class="title">{{ data.product.title }}</h2>
        <span class="subtitle">{{ data.product.subtitle }}</span>

        <p class="description">{{ data.product.description }}</p>

        <div class="buttons-container">
          <button class="buy">
            <img src="https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/shopping-cartorange.png?raw=true" alt="cart">
            <span>Buy</span>
          </button>
          <button class="fav">Fav</button>
          <button class="share">Share</button>
        </div>
      </div>
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
      description:
        "An amazing shirt to make sport. An amazing shirt to make sport. An amazing shirt to make sport. An amazing shirt to make sport. An amazing shirt to make sport",
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
.product {
  height: 90%;
  width: 100%;

  overflow: hidden;

  padding: 0;
}

.container {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;

  color: white;

  padding: 0;
}

.info-container {
  width: 50%;
  height: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title {
  width: 100%;
  font-size: 3rem;
  font-weight: bold;

  color: #5136ff;
}

.subtitle {
  width: 100%;
  padding-left: 0.3rem;
}

.price {
  width: 100%;
  font-size: 2.2rem;
  font-weight: bold;
  color: #ffad37
}

.price-sufix {
  color: #ffad37
}

.description {
  width: 100%;

  margin-top: 2rem;
}

.buttons-container {
  width: 100%;
  height: 45px;

  margin-top: 4rem;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.buttons-container button {
  font-size: 1rem;
  font-weight: bold;
}

.buy {
  width: 40%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  background-color: #ffad37;
  /* border: 2px solid #ffad37 */
}

.buy img {
  max-height: 80%;
  max-width: 80%;
}

.buy span {
  color: white;
  margin-left: 1rem;
}

.fav {
  width: 25%;
  height: 100%;

  background-color: #5136ff;
}

.share {
  width: 25%;
  height: 100%;

  background-color: #ffad37;
}

.image-container {
  width: 50%;
  height: fit-content;

  display: flex;
  justify-content: center;
  align-items: center;

  overflow: hidden;
}

.image-container img {
  max-width: 50%;
  max-height: 50%;
}
</style>