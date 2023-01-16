
from django.urls import path, include
from .views import (index, UserFormView, MessageFormView,
                     HomeView, delete_entry, index, 
                        UserView, MessageView)
from django.views.generic.base import TemplateView # new
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserView, 'user')
router.register(r'message', MessageView, 'message')

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('api/', include(router.urls), name = "apiframework"),
    path('form/user', UserFormView.as_view(), name='user form'), 
    path('form/message', MessageFormView.as_view(), name='message form'), 
    path('delete/<str:model_name>/<int:entry_id>/',
     delete_entry , name='Delete Entry'), 
    path('index/', index, name  = "Index")
]