<template>
  <div class="header">
    <span class="logo"><router-link to="/">Javier Soler &#178;</router-link></span>

    <div class="container--links">
      <router-link to="/">Home</router-link>
      <router-link to="/app/products">Products</router-link>
      <router-link to="/app/about">About</router-link>
    </div>

    <div class="container--buttons">
      <button class="button  button-login"><router-link to="/login">Login</router-link></button>
      <button class="button  button-register"><router-link to="/register">Register</router-link></button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import store from "../../store";

export default Vue.extend({
  name: "Header",
  computed: {
  }
});
</script>

<style scoped>
.header {
  width: 100%;
  height: 6vh;

  position: relative;
  top: 0;

  background-color: #222222;
  /* background:linear-gradient(90deg, #ee0979 0%,#ff6a00 100% ); */
  
  color: white;
  font-size: 2vh;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

a {
  color: white !important;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
  text-decoration-color: white;
}

.logo {
  height: 100%;
  vertical-align: center;
  text-align: center;

  padding: 1vh;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

  background-color: #5136ff;

  display: flex;
  align-items: center;
  justify-content: center;
}

.container--buttons {
  height: 100%;

  display: flex;
  align-items: center;
  justify-content: center;
}

.container--links {
  height: 100%;

  display: flex;
  align-items: center;
  justify-content: space-around;
}

.container--links a {
  margin-left: 1vh;
  margin-right: 1vh;
}

.button {
  width: 15vh;
  height: 100%;

  padding: 1vh;
}

.button:focus {outline:0;}

.button-login {
  background-color: #ffad37;
}

.button-register {
  background-color: #5136ff;
}

</style>
