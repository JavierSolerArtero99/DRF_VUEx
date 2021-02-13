<template>
  <div class="comment">
    <div class="container">
      eso
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store, { storeTypes, Product } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "comments",
})
export default class Comments extends Vue {

  @Prop({required: true, type: Object as () => Product}) readonly product: Product;

  constructor() {
    super();
  }

  data = {
    currentUser: store.getters.currentUser,
  };

  mounted() {
  }
}
</script>

<style scoped>
.comments {
  height: 90%;
  width: 100%;

  overflow: hidden;

  padding: 0;
}

.container {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;

  color: white;

  padding: 0;
}

button:focus {
  outline: none;
}
</style>