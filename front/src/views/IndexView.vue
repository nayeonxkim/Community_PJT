<template>
  <div>
    <h1>Index</h1>
    <p>{{articles}}</p>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name:'IndexView',
  computed:{
      ...mapState(['articles']),
  }

}
</script>

<style>

</style>