import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    articles:[]
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      axios
      .get('http://127.0.0.1:8000/api/v1/index/')
      .then((res) =>{
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err)=> {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
