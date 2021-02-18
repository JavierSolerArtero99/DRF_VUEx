<template>
  <div class="container">
    <form @submit="handleNewProduct" class="create__form">
      <div class="input__container">
        <div>
          <label for="name">Name</label>
          <input
            @click="cleanErrors"
            class="create__input"
            id="name"
            v-model="data.title"
            type="text"
            name="name"
            required
          />
        </div>
        <div>
          <label for="description">Description</label>
          <textarea
            @click="cleanErrors"
            class="create__textarea"
            id="description"
            v-model="data.description"
            type="text"
            name="description"
            required
          />
        </div>
        <div>
          <label for="image">Image</label>
          <input
            @click="cleanErrors"
            class="create__input"
            id="image"
            v-model="data.image"
            type="text"
            name="image"
            required
          />
        </div>
        <div>
          <label for="price">Price</label>
          <input
            @click="cleanErrors"
            class="create__input"
            id="price"
            v-model="data.price"
            type="number"
            name="price"
            required
          />
        </div>
      </div>

      <div v-if="errors.length > 0" class="container-error">
        <b>Please, check this errors:</b>
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>
      <button @click="handleNewProduct" class="login__button">
        Create Product
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

import Component from "vue-class-component";
import ApiService from "../../common/api.service";

@Component({
  name: "createProduct",
  components: {},
})
export default class CreateProduct extends Vue {
  constructor() {
    super();
  }

  data = {
    title: "",
    description: "",
    image: "",
    price: 0,
  };

  errors: string[] = [];

  mounted() {}

  handleNewProduct(e) {
    let product = {
      product: {
        slug: this.data.title,
        title: this.data.title,
        description: this.data.description,
        image: this.data.image,
        price: this.data.price,
      },
    };

    ApiService.post("products", product)
      .then((data) => {
        console.log(data);
      })
      .catch((err) => {
        // console.log(err.response.data);

        if (!err.response.data.includes("duplicate key value")) {
          for (var i in err.response.data) {
            this.errors.push(`${i}: ${err.response.data[i][0]}`);
          }
        } else {
          this.errors.push(`There is a product with name: ${this.data.title}`);
        }
      });

    e.preventDefault();
  }

  cleanErrors(e) {
    this.errors = [];
  }
}
</script>

<style scoped>
.container {
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
  height: 70%;
  width: 30%;

  display: flex;
  flex-direction: column;
  align-items: center;

  padding: 0;
}

.input__container {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.router-link {
  margin-top: 2rem;
  color: white;
}

h1 {
  background: #5136ff;
  text-align: center;
  color: white;
}

img {
  width: 100px;
  height: 100px;
}

label {
  color: white;
  padding-left: 1rem;
}

.container-error {
  height: fit-content;
  width: 250px;

  margin: 1.5rem;
  padding: 1rem;

  position: absolute;
  top: 0;
  right: 0;

  border-radius: 0.3rem;

  line-height: 2rem;

  background-color: #c23834;
  color: white;
}

.container-error p {
  line-height: 1.5rem;
}

.container-error img {
  width: 30px;
  height: 30px;
}

.create__form {
  width: 100%;
  height: 100%;

  display: grid;
  grid-template-rows: 90% 10%;
}

.create__input {
  height: 3rem;
  width: 100%;

  color: white;

  border-bottom: 2px #ffad37 solid;

  padding-left: 1.5rem;
  padding-right: 1rem;

  font-size: 1.2rem;

  display: flex;
  align-items: center;
  justify-content: center;
}

.create__input:focus {
  border-bottom: 2px #5136ff solid;
}

.create__input::placeholder {
  color: white;
}

.create__textarea {
  height: 7rem;
  width: 100%;

  color: white;

  border-bottom: 2px #ffad37 solid;

  padding-left: 1.5rem;
  padding-right: 1rem;

  font-size: 1.2rem;

  display: flex;
  align-items: center;
  justify-content: center;
}

.create__textarea:focus {
  border-bottom: 2px #5136ff solid;
}

.create__textarea::placeholder {
  color: white;
}

button:focus,
input:focus {
  outline: 0;
}

.login__button {
  background-color: #ffad37;
  color: white;

  font-weight: bold;

  display: flex;
  align-items: center;
  justify-content: center;
}

.login__button:hover {
  background-color: #5136ff;
}
</style>