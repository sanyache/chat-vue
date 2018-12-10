<template>
    <div>
        <input v-model='login' type='text' placeholder='Логін' />
        <input v-model='password' type='password' placeholder='Пароль'/>
        <button @click='setLogin'>Вхід</button>

    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: 'Login',
        data(){
            return {
                login: '',
                password: '',
            }
        },
        methods: {
           setLogin(){
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/token/create/',
                type: "POST",
                data:{
                    username: this.login,
                    password: this.password
                },
                success: (response) => {
                    alert('Дякуємо, що ви з нами !')
                    sessionStorage.setItem('auth_token', response.data.attributes.auth_token)
                    console.log(response.data.attributes.auth_token)
                },
                error: (response) => {
                    if (response.status === 400)
                        alert('Невірний логін чи пароль')
                },
            })
           }
        },
    }
</script>

<style>

<style>
