<template>
  <div class="profile">
    <div class="container">
      <img src="https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true" alt="logo" />
      <span>Javier Soler Cantó</span>

      <cite>Lorem ipsum dolor sit amet consectete perferendis libero optio eiustam saepe quas?</cite>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "profile",
})
export default class Profile extends Vue {
  data = {
  };

  constructor() {
    super();
  }

  mounted() {
    console.log("Mounted profile Component");
  }
}
</script>

<style scoped>
.profile {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  background-size: cover;

  background-color: #222222;
}

.container {
  height: 70%;
  width: 30%;

  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 0;

  color: white;
  font-size: 1.3rem;
}

img {
  width: 150px;
  height: 150px;
}

cite {
  font-size: 1rem;
  text-align: center;
}

</style>
