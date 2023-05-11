<template>
  <div>
    <h3>ArticleList</h3>

    <ArticleListItem v-for="article in articles"
    :key="article.id" 
    :article-item="article" />

  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
export default {
  components:{
    ArticleListItem,
  },
  computed:{
    articles(){
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>