<template>
  <div class="comments">
    <div class="container">
      <CommentComponent v-for="comment in data.comments" v-bind:key="comment.id" :comment="comment" />
    </div>
    <div class="comments-box">
      <textarea name="" id="" cols="1" rows="3" placeholder="Text your comment"></textarea>
      <button></button>
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

  addComment() {
    
  }
}
</script>

<style scoped>
.comments {
  height: 70%;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;

  overflow: hidden;

  padding: 0;
}

.container {
  height: 80%;
  width: 100%;

  overflow-x: hidden;
  overflow-y: scroll;
}

.comments-box {
  width: 40%;
  height: 17%;

  padding: 0.3rem;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comments-box textarea {
  width: 70%;
  height: 70%;

  padding: 0.3rem;
  
  resize: none;

  color: white;
  border: 3px solid #ffad37;
}

.comments-box button {
  width: 27%;
  height: 70%;

  background-image: url('https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/send.png?raw=true');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center center;
  background-origin: content-box;

  border: 3px solid #5136ff;
}

.comments-box button:hover {
  background-color: #5136ff;
  background-image: url('https://github.com/JavierSolerArtero99/DRF_VUEx/blob/master/Vuex/images/sendgrey.png?raw=true');
}

button:focus, textarea:focus {
  outline: none;
}
</style>