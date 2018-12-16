<template>
    <mu-col span='3' sm='3' class="rooms-list">
        <mu-button @click="addRoom">Створити кімнату</mu-button>
        <div v-for="room in rooms" :key="room.id">
            <h3 @click="openDialog(room.id)"> {{room.creater.username}} </h3>
            <small>{{room.date}}</small>
        </div>
    </mu-col>
</template>


<script>
import $ from 'jquery'
import Dialog from '@/components/rooms/Dialog'
export default {
    name: 'Room',
    components: {
        Dialog
    },
    data(){
        return {
            rooms: '',
            dialog: {
                id: '',
                show: false,
            },
        }
    },
    created(){
        $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
        this.loadRoom()
    },
    methods: {
        loadRoom() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                type: 'GET',
                success: (response) => {
                    this.rooms = response.data.data
                }
            });
        },
        openDialog(id){
            this.$emit('openDialog', id)                  
        },
        addRoom() {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                type: 'POST',
                data: {

                },
                success: (response) => {
                    this.loadRoom()
                },
                error: (response) => {
                    alert(response.statusText)
                }
            }); 
        }
    }
}
</script>

<style scoped>
    h3 {
        cursor: pointer;
    } 
    .rooms-list {
        box-shadow: 1px 4px 5px #848181;
        margin: 20px 90px 0px 0px;
    }
</style>
