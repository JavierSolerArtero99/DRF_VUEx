<template>
  <div class="login">
    <div class="container">
      <img src="https://i.ibb.co/sqdfW3W/vuex.png" alt="logo" />
      <form @submit="checkForm" class="login__form">
        <div class="input__container">
          <div>
            <label for="username">Username</label>
            <input
              @click="cleanErrors"
              class="login__input"
              id="username"
              v-model="data.username"
              type="text"
              name="username"
              required
            />
          </div>
          <div>
            <label for="email">Email</label>
            <input
              class="login__input"
              id="email"
              v-model="data.email"
              type="text"
              name="username"
              required
            />
          </div>
          <div>
            <label for="password">Password</label>
            <input
              class="login__input"
              id="password"
              v-model="data.password"
              type="password"
              name="password"
              required
            />
          </div>
        </div>

        <div v-if="errors.length > 0" class="container-error">
          <b>Please, check this errors:</b>
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <button type="submit" class="login__button">
          {{ this.mode ? "Login" : "Register" }}
        </button>
      </form>
    </div>

    <button class="router-link" @click="changeMode">
      {{
        this.mode ? "You don't have an account?" : "Do you have an account yet?"
      }}
    </button>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import ApiService from "../../common/api.service";
import store, { SetAuth, storeTypes } from "../../store";

@Component({
  name: "login",
})
export default class Login extends Vue {
  data = {
    username: "",
    email: "",
    password: "",
  };

  errors: string[] = [];
  mode: boolean = true;
  logged: boolean = false;

  constructor() {
    super();

    this.errors = [];
  }

  /* HANDLERS */

  /**
   * Cambia el metodo para hacer login / registro
   */
  changeMode(): void {
    this.mode = !this.mode;
  }

  /**
   * Control de errores en el formulario de usuario
   */
  checkForm(e) {
    // login
    if (this.mode) {
      let user = {
        username: this.data.username,
        email: this.data.email,
        password: this.data.password,
      } as SetAuth;
      this.handleAuth(user);
    }

    // Register
    if (
      this.data.username.length >= 3 &&
      this.data.username.length <= 15 &&
      this.data.password.length >= 8 &&
      this.data.password.length <= 30
    ) {
      // do a register
      let user = {
        username: this.data.username,
        email: this.data.email,
        password: this.data.password,
      } as SetAuth;
      this.handleAuth(user);
    }

    if (this.data.username.length < 3 || this.data.username.length > 15)
      this.errors.push("Username must be at least 3 characters.");
    if (this.data.password.length < 8 || this.data.password.length > 30)
      this.errors.push("Password must be at least 8 characters.");

    e.preventDefault();
  }

  /**
   * Cleaning errors when introduce new credentials
   */
  cleanErrors(e) {
    this.errors = [];
  }

  /* AUTHENTICATION */

  /**
   * Handle the user auth petition
   */
  handleAuth(user: SetAuth) {
    store.dispatch(
      storeTypes.root.actions!.setAuth({
        username: user.username,
        email: user.email,
        password: user.password,
        isLogin: this.mode,
        changeScreen: () => {
          this.$router.push({ path: "/" });
        },
        showErrors: this.showErrors,
      })
    );
  }

  /* EXCEPTIONS */

  /**
   * Show errors in toastr
   *
   */
  showErrors(errorsToShow: string) {
    this.errors.push(errorsToShow);
  }
}
</script>

<style scoped>
.login {
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

.login__form {
  width: 100%;
  height: 100%;

  display: grid;
  grid-template-rows: 90% 10%;
}

.login__input {
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

.login__input:focus {
  border-bottom: 2px #5136ff solid;
}

.login__input::placeholder {
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