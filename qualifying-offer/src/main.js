import Vue from 'vue'
import Vuex from "vuex";
import './plugins/axios'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.use(Buefy)
Vue.use(Vuex);

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {
    payArray: [],
    dataLoading: false
  },
  mutations: {
    setPayArray(state, arr) {
      state.payArray = arr;
    },
    setDataLoading(state, loading) {
      state.dataLoading = loading;
    }
  }
});

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
