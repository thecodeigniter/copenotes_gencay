from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .utils import generate

# Create your models here.


class Configuration(models.Model):
    is_first_addition = models.BooleanField(default = True)
    message_time_in_sec_threshold = models.IntegerField(default = 60, 
     validators=[MinValueValidator(1)])
    message_count_threhsold = models.IntegerField(default = 10, 
    validators=[MinValueValidator(1)])
   


    def save(self, *args, **kwargs):
        if not self.pk and Configuration.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Configuration instance')
        return super(Configuration, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.message_time_in_sec_threshold)+\
        " | "+str(self.message_count_threhsold)


class Message(models.Model):
    text = models.TextField()
    def save(self, *args, **kwargs):
        try:
            Configuration.object.first()
        except:
            if Message.objects.count() == Configuration.objects.first().message_count_threhsold:
                raise ValidationError('You cannot add more than '+\
                str(Configuration.objects.first().message_count_threhsold)+' messages.')
        return super(Message, self).save(*args, **kwargs)
    def __str__(self):
        return self.text[0:20]+"..."


class User(AbstractUser, models.Model):
    first_name = models.CharField(max_length  = 50)
    last_name = models.CharField(max_length  = 50)
    email = models.EmailField(unique = True)
    message = models.ManyToManyField("Message", related_name = "message", blank = True)
    username = models.CharField(max_length = 50, unique = True,
     default ="user_"+generate())
    try:
        count = models.IntegerField(default = Configuration.objects.first().message_count_threhsold)
    except:
        count = models.IntegerField(default = 10)
    def __str__(self):
        return self.email






    



