<template>
  <div class="footer">
    <span>Javier Soler Artero & Cantó ©</span>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.footer {
  width: 100%;
  height: 8vh;

  position: absolute;
  bottom: 0;

  background-color: #000000;
  background:linear-gradient(90deg, #ee0979 0%,#ff6a00 100% );
  
  color: white;
  font-size: 2vh;

  display: flex;
  align-items: center;
  justify-content: center;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
