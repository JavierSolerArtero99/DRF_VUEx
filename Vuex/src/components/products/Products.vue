<template>
  <div class="products">
    <div class="container">
      ASKSKKaaada
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "products",
})
export default class Products extends Vue {
  data = {};

  constructor() {
    super();
  }

  mounted() {}
}
</script>

<style scoped>
.products {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 0;

  color: white;
  font-size: 1.3rem;
}