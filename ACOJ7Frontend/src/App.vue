<template>
  <div id="app" class="backGround">
    <router-view/>
  </div>
  <!-- !-->
</template>

<script>
export default {
  name: 'App'
}
//
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.backGround{
  background-color: #00fcff;
  padding: 0px;
  height: 100vh;
  width: 100vw;
  position: fixed;
  top: 0;
  left: 0;
}

/**/
</style>
