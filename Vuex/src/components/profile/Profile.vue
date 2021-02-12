<template>
  <div class="profile">
    <div class="container">
      <div class="header">
        <img
          @click="
            () => {
              $router.push({ path: '/app/profile-edit' })
            }"

          class="picture"
          src="https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true"
          alt="profile picture"
        />
        <span class="username">Jasoka</span>
        <span class="email">jasoka@gmail.com</span>

        <cite
          >Lorem ipsum dolor sit amet consectete perferendis libero optio
          eiustam saepe quas</cite
        >
      </div>

      <div class="dashboard">
        <div class="dashboard-card">
          <img
            src="https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/fire.png?raw=true"
            alt="uploads"
          />
          <span>1</span>
        </div>
        <div class="dashboard-card">
          <img
            src="https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/upload.png?raw=true"
            alt="karma"
          />
          <span>1</span>
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
  name: "profile",
})
export default class Profile extends Vue {
  data = {};

  constructor() {
    super();
  }

  mounted() {}
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
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 0;

  color: white;
  font-size: 1.3rem;
}

.header {
  height: 40%;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.header cite {
  margin-top: 0.5rem;
}

.dashboard {
  width: 100%;
  height: 40%;

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;

  margin-top: 1rem;
}

.dashboard-card {
  width: 45%;
  height: 70%;

  display: flex;
  align-items: center;
  justify-content: center;
}

.dashboard-card img {
  width: 80px;
  height: 80px;
}

.dashboard-card span {
  font-size: 3rem;
  margin-left: 3rem;
}

.username {
  margin-top: 1rem;
}

.email {
  font-size: 0.8rem;
}

.picture {
  width: 150px;
  height: 150px;
}

.picture:hover {
  content: url("https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/edit.png?raw=true");
  cursor: pointer;

  width: 140px;
  height: 140px;

  margin: 1rem;

  transition: 1s all;
}

cite {
  font-size: 1rem;
  text-align: center;
}
</style>
