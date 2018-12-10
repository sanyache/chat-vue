<template>
       <div>
            <h1>Чат на Vue.js</h1>
            <button @click='goLogin'>Вхід</button>

       </div>
</template>

<script>
    export default {
        name: 'Home',
        methods: {
            goLogin(){
               this.$router.push({name: 'login'})
            }
        },
    }
</script>

<style>

</style>
