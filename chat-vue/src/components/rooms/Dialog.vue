<template>
    <mu-col span="8" xl='8'>
        <AddUsers :room="id"></AddUsers>
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs"
                    direction="column"
                    justify-content="start"
                    align-items="end"
                    :key="dialog.id" >
                <p><strong>{{ dialog.user.username }}</strong></p>
                <p>{{ dialog.text }}</p>
                <span>{{ dialog.date }}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field multi-line :rows="3" :rows-max="6" 
                    placeholder='Введіть текст' v-model="form.textarea"></mu-text-field>
                <mu-button class="btn-send" round color="success" @click="sendMes">Відправити</mu-button>    
            </mu-row>
        </mu-container>    
    </mu-col>
</template>


<script>
import $ from 'jquery'
import AddUsers from "./AddUsers"    
export default {
    name: 'Dialog',
    props: {
        id: '',
    },
    components: {
        AddUsers
    },
    data() {
        return {
            dialogs: '',
            form: {
                textarea: '',
            }
        }
    },
    created() {
        $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
        this.loadDialog()
        // setInterval(() => {
        //     this.loadDialog()
        // }, 5000)
        
    },
    methods: {
        loadDialog(){
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                type: "GET",
                data: {
                    room: this.id
                },
                success: (response) => {
                    this.dialogs = response.data.data
                    console.log(response.data.data)
                },
                error:(response) => {
                    console.log(this.id)
                }

                
            })
        },
        sendMes(){
            $.ajax({
                url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                type: "POST",
                data: {
                    room: this.id,
                    text: this.form.textarea
                },
                success: (response) => {
                    this.loadDialog()
                },
                error:(response) => {
                    alert(response.statusText)
                }

                
            })    
        }
    }
}
</script>

<style scoped>
    .dialog {
        border: 1px solid #000;
        margin: 5px 0 0 0;
    }
    .btn-send {
        margin: 60px 0 0 20px;
    }
    
</style>
