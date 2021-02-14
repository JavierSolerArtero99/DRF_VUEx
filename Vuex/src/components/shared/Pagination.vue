<template>
  <div class="pagination">
    <button class="button-focus">Previous</button>
    <div class="pages">
      <button
        class="page"
        v-for="page in data.totalPages"
        v-bind:key="page"
        v-bind:class="page === offset ? 'page--current' : 'page--stand'"
      >
        {{ page }}
      </button>
    </div>
    <button class="button-focus">Next</button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store, { storeTypes, Product } from "../../store";
import { Route } from "vue-router";

@Component({
  name: "pagination",
})
export default class Pagination extends Vue {
  @Prop({ required: true, type: Number }) readonly limit: number;
  @Prop({ required: true, type: Number }) readonly offset: number;
  @Prop({ required: true, type: Number }) readonly total: number;

  constructor() {
    super();
  }

  data = {
    totalPages: 0
  }

  mounted() {
    this.data.totalPages = Math.ceil(this.total / this.limit);
  }
}
</script>

<style scoped>
.pagination {
  width: 79%;
  height: 10%;

  overflow: hidden;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0;
}

.button-focus {
  height: 100%;
  width: 10%;

  color: white;

  background-color: #ffad37;
}

.pages {
  width: 80%;
  height: 100%;

  display: flex;
  justify-content: space-evenly;
  align-items: center;

  color: white;
}

.page {
  height: 100%;
  width: 100%;

  margin: .2rem;
}

.page--stand {
  border: 2px solid #ffad37;
}

.page--stand:hover {
  border: 2px solid #ffad37;
  background-color: #ffad37;
}

.page--current {
  background-color: #5136ff;
}

button:focus {
  outline: none;
}
</style>