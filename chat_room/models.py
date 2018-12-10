from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Room(models.Model):

    creater = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name='учасники', related_name='invited_user')
    date = models.DateTimeField('Дата створення', auto_now_add=True)

    class Meta:
        verbose_name = 'Кімната чату'
        verbose_name_plural = 'Кімнати чату'

class Chat(models.Model):

    room = models.ForeignKey(Room, verbose_name='Кімната чату', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    text = models.TextField('Меседж', max_length=500)
    date = models.DateTimeField('Дата відправки', auto_now_add=True)


    class Meta:

        verbose_name = 'Меседж'
        verbose_name_plural = 'Меседжи'

