<template>
       <mu-container>
           <mu-appbar style="width: 100%;" color="primary">
               
                    Чат на Vue.js
               
                <mu-button flat slot="right" v-if="!auth" @click='goLogin'>Вхід</mu-button>
                <mu-button flat slot="right" v-else @click="logout">Вихід</mu-button>

            </mu-appbar>

            <mu-row>
                <Room v-if="auth" @openDialog="openDialog"></Room>
                <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
            </mu-row>
       </mu-container>
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
