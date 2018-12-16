from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializers, ChatSerializers, \
    ChatPostSerializers, UserSerializers

#


class Rooms(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(
                                    invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)


class Dialog(APIView):

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})

    def post(self, request):

        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)

class AddUsersRoom(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)

