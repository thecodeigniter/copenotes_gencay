from django.contrib import admin
from .models import Configuration, User, Message

# Register your models here.

admin.site.register(User)
admin.site.register(Configuration)
admin.site.register(Message)

