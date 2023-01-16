from django import forms
  
# import GeeksModel from models.py
from .models import User, Message, Configuration
  
# create a ModelForm
class UserForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', )
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = "__all__"