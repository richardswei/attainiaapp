import Vue from 'vue'
import App from './App'
import Active from './Active'
import Dormant from './Dormant'
import { 
  MdButton, 
  MdSwitch, 
  MdCard, 
  MdToolbar 
} from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdButton)
Vue.use(MdSwitch)
Vue.use(MdCard)
Vue.use(MdToolbar)

import NotFound from './NotFound'
Vue.config.productionTip = false
// const Home = { template: '<p>home page</p>' }
const routes = {
  '/': App,
  '/active': Active,
  '/dormant': Dormant,
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})