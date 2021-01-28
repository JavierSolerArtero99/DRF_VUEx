<template>
  <div class="header">
    <h1>e-shop</h1>
    <span>{{ currentUser }}</span>
  </div>
  <div>
    <button @click="login('Jasoka')">Login</button>
    <button @click="logout()">Logout</button>
  </div>    
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'Header',
  props: {
  },

  computed:{
    ...mapState(['currentUser'])
  },

  methods: {
    login: (username) => {
      this.$store.commit('USER_LOGIN', username);
    }, 
    logout: () => {
      this.$store.commit('USER_LOGOUT');
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.header {
  width: 100%;
  height: 8vh;

  position: sticky;
  top: 0;

  background:linear-gradient(90deg, #ee0979 0%,#ff6a00 100%);
  font-size: 2vh;

  color: white;

  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
