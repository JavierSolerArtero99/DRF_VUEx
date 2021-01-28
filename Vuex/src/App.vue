<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <span>USER: {{ currentUser.name }}</span>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted } from 'vue';
import { useStore } from './store/index'
import { ActionTypes } from './store/actions'

export default defineComponent({
  name: 'App',
  components: {
  },
  setup() {
    const store = useStore();
    onMounted(() => store.dispatch(ActionTypes.GetCurrentUser));
    const currentUser = computed(() => store.getters.getCurrentUser);
    console.log(currentUser);
    return { currentUser };
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
