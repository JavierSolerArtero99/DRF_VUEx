<template>
  <div class="header">
    <span class="logo"
      ><a target="_blank" href="https://github.com/JavierSolerArtero99/DRF_VUEx"
        >Javier Soler &#178;</a
      ></span
    >

    <div class="container--links">
      <router-link to="/">Home</router-link>
      <router-link to="/app/products">Products</router-link>
      <router-link to="/app/editor">Editor</router-link>
    </div>

    <div class="container--buttons">
      <button
        v-if="this.$store.getters.currentUser.isAuthed"
        @click="
          () => {
            $router.push({ path: '/app/profile' });
          }"
        class="button button-profile"
      >
        {{ this.$store.getters.currentUser.username }}
      </button>
      <button @click="handleAuth" class="button button-login">
        {{ this.$store.getters.currentUser.isAuthed ? "Logout" : "Login" }}
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import store, { storeTypes } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "appHeader",
})
export default class Header extends Vue {
  data = {
    currentUser: store.getters.currentUser,
  };

  handleAuth() {
    if (this.$store.getters.currentUser.isAuthed) {
      store
        .dispatch(storeTypes.root.actions!.purgeAuth())
        .then((res) => this.$router.push({ path: "/login" }));
    } else {
      this.$router.push({ path: "/login" });
    }
  }
}
</script>

<style scoped>
.header {
  width: 100%;
  height: 6vh;

  position: relative;
  top: 0;

  background-color: #222222;

  border-bottom: 2px #202020 solid;

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
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;

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
  width: 60%;

  display: flex;
  align-items: center;
  justify-content: space-evenly;
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

.button:focus {
  outline: 0;
}

.button-login {
  background-color: #ffad37;
}

.button-profile {
  background-color: #5136ff;
}
</style>
