<template>
  <div style="backGround">
    SOL is an SB;
    <test a='1' b='2'>41235235423</test>
  </div>
</template>

<script>
import test from './test'

export default {
  name: 'HelloWorld',
  components: {
    test
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
