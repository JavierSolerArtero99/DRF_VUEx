<template>
  <div class="not-found">
    <h2>Error 404</h2>
    <span>The page you were looking for is no longer here</span>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import store from "../../store";

export default Vue.extend({
  name: "NotFound",
  computed: {
  },
  mounted() {
    console.log("Hey");
  },
});
</script>

<style scoped>
.not-found {
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
