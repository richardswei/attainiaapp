<template>
  <div>
    <a href="/"><img class="mini-logo" alt="Vue logo" src="./assets/logo-red.png"></a>
    <div>
      <md-button class="md-raised md-disabled" href="/active">
        Highlight Active Users
      </md-button>
      <md-button class="md-raised md-accent" href="/dormant">
        Highlight Dormant Users
      </md-button>
    </div>
    <UserTable 
      status="dormant"
    />
  </div>
</template>

<script>
  import UserTable from './components/UserTable.vue'

  export default {
    name: 'Dormant',
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