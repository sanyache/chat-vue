<template>
       <div>
            <h1>Чат на Vue.js</h1>
            <button v-if="!auth" @click='goLogin'>Вхід</button>
            <button v-else @click="logout">Вихід</button>
            <Room v-if="auth" @openDialog="openDialog"></Room>
            <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
       </div>
</template>

<script>
    import Room from '@/components/rooms/Room'
    import Dialog from '@/components/rooms/Dialog'
    export default {
        name: 'Home',
        components: {
            Room,
            Dialog
        },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false
                }
            }
        },
        computed: {
            auth(){
                if (sessionStorage.getItem('auth_token'))
                    return true
            }
        },
        methods: {
            goLogin(){
               this.$router.push({name: 'login'})
            },
            logout(){
                sessionStorage.removeItem('auth_token')
                window.location = '/'
            },
            openDialog(id){
                this.dialog.id = id
                this.dialog.show = true
            }
        },
    }
</script>

<style>

</style>
