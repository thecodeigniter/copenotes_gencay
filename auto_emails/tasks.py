# from optparse import Values
from genericpath import exists
from celery import shared_task
from .models import User, Message, Configuration
from django.core.mail import send_mail
import random
from copenotes_gencay import settings


def shuffle_email_message(queryset):
    shuffled_messages = []
    for message in queryset:
        shuffled_messages.append(message.text)
    random.shuffle(shuffled_messages)
    return shuffled_messages[0], Message.objects.get(text = shuffled_messages[0] )

@shared_task
def email_sender(bind=True):
    messages = Message.objects.all()
    for user in User.objects.all():
        try:    
            message_to_sent, message_object = shuffle_email_message(messages.difference(user.message.all()))
            send_mail("Motivatioanl Quote for "+user.first_name+" "+user.last_name,
                        "Dear "+user.first_name+" "+user.last_name+",\n\n"+message_to_sent+\
                        "\n\nRegards"
                ,settings.DEFAULT_FROM_EMAIL,[user.email],fail_silently=False)
            user.message.add(message_object)
            user.save()
        except:
            print("No messages are left for user", user.email)

            
    
        