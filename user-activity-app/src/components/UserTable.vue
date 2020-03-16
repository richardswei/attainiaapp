<template>
  <div>
    <md-toolbar md-elevation="0">
      <h1 class="md-title">User Monitor - {{status}}</h1>
      <div class="md-toolbar-section-end">
        <md-switch class="highlight-switch" v-model="boolean">Active Users Highlighted</md-switch>
      </div>
    </md-toolbar>
    <table>
      <thead>
        <tr class="md-table-row">
          <th scope="col">ID</th>
          <th scope="col">Username</th>
          <th scope="col">Login Count</th>
          <th scope="col">Project Count</th>
          <th scope="col">Last Login</th>
        </tr >
      </thead>
      <tbody>
        <tr class="md-table-row" 
          v-for="(element, index) in rowData" :key="index"
          v-bind:class="{
            'highlighted-green': element.login_count>0 && boolean && status=='active',
            'highlighted-red': element.login_count<=0 && boolean && status=='dormant'
          }" >
          <td class="md-table-cell">{{ element.id }}</td>
          <td class="md-table-cell">{{ element.username }}</td>
          <td class="md-table-cell">{{ element.login_count }}</td>
          <td class="md-table-cell">{{ element.project_count }}</td>
          <td class="md-table-cell">{{ element.last_login }}</td>
        </tr >
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'TableCard',
    // props: {
    //   activeHighlight: Boolean
    // },
    props: {
      'status':String,
    },
    data: () => ({
      boolean: false,
      rowData: []
    }),
    created () {
      // fetch the data when the view is created and the data is
      // already being observed
      this.fetchData()
    },
    methods: {
      fetchData() {
        fetch("http://localhost:8000/api/v1/users/")
          .then(res => res.json())
          .then(json => {
            const parsedJson = json.map((account) => {
              account.last_login = (new Date(account.last_login)).toLocaleString();
              return account
            }) 
            this.rowData = parsedJson
          })
      }
    }
  }
</script>

<style>
  .highlighted-red {
    background: rgba(219, 29, 54,0.7)
  }
  .highlighted-green {
    background: rgba(60,240,60,0.7)
  }
  table {  
    width: 100%;
    color: #333;
    font-family: Helvetica, Arial, sans-serif;

    border-collapse: 
    collapse; border-spacing: 0; 
  }
  td, th {  
    border: 1px solid transparent; /* No more visible border */
    height: 30px; 
    transition: all 0.3s;  /* Simple transition for hover effect */
  }
  th {  
    background: #DFDFDF;  /* Darken header a bit */
    font-weight: bold;
  }
  td {  
    text-align: center;
  }

</style>