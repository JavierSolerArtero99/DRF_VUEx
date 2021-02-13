<template>
  <div class="comments">
    <div class="container">
      <CommentComponent v-for="comment in data.comments" v-bind:key="comment.id" :comment="comment" />
      <div class="comment-box">
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store, { storeTypes, Product, Comment } from "../../store";
import { Route } from "vue-router";

import CommentComponent from "../comments/Comment.vue";

@Component({
  name: "comments",
  components: {
    CommentComponent
  }
})
export default class Comments extends Vue {

  @Prop({ required: true, type: Number }) readonly productId: number;

  constructor() {
    super();
  }

  data = {
    currentUser: store.getters.currentUser,
    comments: [] as Comment[],
  };

  mounted() {
    console.log(this.productId);

    this.data.comments = [
      {
        id: 1,
        body: "This is a comment of a product",
        author: {
          id: 0,
          username: "jasoka",
          email: "jasoka@gmail.com",
          password: "",
          image: "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true",
          bio: "",
          isAuthed: true,
        },
        product: {
          id: parseInt(this.$route.params.id),
          title: "Shirt",
          subtitle: "Running shirt",
          price: 19.99,
          description: "An amazing shirt to go running every day and get fit",
          image:
            "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/shirt.png?raw=true",
          author: {
            id: 0,
            username: "jasoka",
            email: "jasoka@gmail.com",
            password: "",
            image: "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true",
            bio: "",
            isAuthed: true,
          },
        },
      },
      {
        id: 2,
        body: "This is another comment of a product",
        author: {
          id: 1,
          username: "carlos",
          email: "carlos@gmail.com",
          password: "",
          image: "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true",
          bio: "",
          isAuthed: false,
        },
        product: {
          id: parseInt(this.$route.params.id),
          title: "Shirt",
          subtitle: "Running shirt",
          price: 19.99,
          description: "An amazing shirt to go running every day and get fit",
          image:
            "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/shirt.png?raw=true",
          author: {
            id: 0,
            username: "jasoka",
            email: "jasoka@gmail.com",
            password: "",
            image: "https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/avatar.png?raw=true",
            bio: "",
            isAuthed: true,
          },
        },
      },
    ];
  }
}
</script>

<style scoped>
.comments {
  height: 70%;
  width: 100%;

  overflow: hidden;

  padding: 0;
}

.container {
  height: 100%;
  width: 100%;

  overflow-x: hidden;
  overflow-y: scroll;
}

button:focus {
  outline: none;
}
</style>