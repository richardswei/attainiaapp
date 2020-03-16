<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo-red.png">
    <h2 class="md-display-3">User Monitor</h2>
    <div>
      <md-button class="md-raised md-primary" href="/active">
        Highlight Active Users
      </md-button>
      <md-button class="md-raised md-accent" href="/dormant">
        Highlight Dormant Users
      </md-button>
    </div>
  </div>
</template>

<script>
  // import HelloWorld from './components/HelloWorld.vue'

  export default {
    name: 'App',
    components: {
      // HelloWorld
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
