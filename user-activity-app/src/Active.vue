<template>
  <div>
    <a href="/"><img class="mini-logo" alt="Vue logo" src="./assets/logo-red.png"></a>
    <div>
      <md-button class="md-raised md-primary" href="/active">
        Highlight Active Users
      </md-button>
      <md-button class="md-raised md-disabled" href="/dormant">
        Highlight Dormant Users
      </md-button>
    </div>
    <UserTable 
      status="active"
    />
  </div>
</template>

<script>
  import UserTable from './components/UserTable.vue'

  export default {
    name: 'App',
    components: {
      UserTable
    }
  }
</script>

<style>
  .mini-logo {
    max-width: 15rem
  }
</style>