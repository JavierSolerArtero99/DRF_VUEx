<template>
  <div class="login">
    <form class="login__form">
      <input type="text" name="username" placeholder="Username">
      <!-- <input type="email" name="email" placeholder="Email"> -->
      <input type="password" name="password" placeholder="Password">

      <button class="login__button">Login</button>

      <router-link to="/register">You don't have an account?</router-link>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Login",
  components: {
  },
  computed: {
  },
  mounted() {
  },
});
</script>

<style scoped>
.login {
  height: 100%;
  width: 100%;

  display: flex;
  align-items: center;
  justify-content: center;

  background-image: url('https://images.unsplash.com/photo-1565638459249-c85cbb2faaa8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
  background-size: cover;
}

.login__form {
  height: 60%;
  width: 60%;

  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

  background-color: #00000090;
  border-radius: 3vh;
}

.login__button {
  height: 2rem;
  width: 7rem;

  background-color: white;
  color: black;
  border-radius: 3vh;

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>