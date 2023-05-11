<template>
  <div>
    <h1>Index</h1>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name:'IndexView',
  components:{
    ArticleList
  },
  methods:{
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  },
  created(){
    this.getArticles()
  }

}
</script>

<style>

</style>