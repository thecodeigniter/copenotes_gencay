from django.shortcuts import render, HttpResponse
from .forms import UserForm, MessageForm, ConfigurationForm
from django.views import View
from .models import User, Message, Configuration
from django.shortcuts import redirect
from .serializers import (UserSerializer, MessageSerializer)
from rest_framework import viewsets
from .constants import email_text

try:
    if (not Configuration.objects.exists()):
        c = Configuration()
        c.save()


    if (Configuration.objects.first().is_first_addition):
        for text in email_text:
            m = Message(text = text)
            m.save()
except:
    print("First Migrations...")
 
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class UserFormView(View):
    def __init__(self):
        self.template_name = "registration/general_form.html"
        self.custom_style = "text-align: center;max-width:300px; top:40%;"
        self.FormType = UserForm
        self.header_text = "New Customer Registration"
        self.form_text = "New Customer Registration"
        self.context = {}
        self.context['custom_style'] = self.custom_style
        self.context['form_creation']= self.FormType()
        self.context['form_header']= self.header_text
        self.context['form_text']= self.header_text
        self.context['delete_url'] = "/delete/user/"
        
        

    def get(self, request):
        
        self.context["success_message"] = ""
        
        return render(request, self.template_name , self.context)
    
    def post(self, request):
        
        details = self.FormType(request.POST)
        if details.is_valid(): 
            self.context["success_message"] = "User has been addedd successfully!"
            post = details.save()
            post.save() 
        else:
            self.context["success_message"] = "User has not been added."
        return render(request, self.template_name , self.context)

class MessageFormView(View):  
    def __init__(self):
        self.template_name = "registration/general_form.html"
        self.custom_style = "text-align: center;max-width:400px; top:40%;"
        self.FormType = MessageForm
        self.header_text = "Write New Message"
        self.form_text = "Write New Message"
        self.context = {}
        self.context['custom_style'] = self.custom_style
        self.context['form_creation']= self.FormType()
        self.context['form_header']= self.header_text
        self.context['form_text']= self.header_text
        self.context['delete_url'] = "/delete/message/"
        
        

    def get(self, request):
        self.context["success_message"] = ""
        return render(request, self.template_name , self.context)
    def post(self, request):
        details = self.FormType(request.POST)
        try:
            if details.is_valid(): 
                self.context["success_message"] = "Message has been added successfully!"
                post = details.save()
                post.save() 
            else:
                self.context["success_message"] = "Message has not been added."
        except:
            self.context["success_message"] = 'You cannot add more than '+\
            str(Configuration.objects.first().message_count_threhsold)+' messages.'
        return render(request, self.template_name , self.context)
    

class ConfigurationFormView(View):
    def __init__(self):
        self.template_name = "home.html"
        self.custom_style = "text-align: center;max-width:300px; top:40%;"
        self.FormType = ConfigurationForm
        self.header_text = ""
        self.form_text = ""
        self.context = {}
        self.context['custom_style'] = self.custom_style
        self.context['form_creation']= self.FormType()
        self.context['form_header']= self.header_text
        self.context['form_text']= self.header_text
        
        

    def get(self, request):
        
        self.context["success_message"] = ""
        
        return render(request, self.template_name , self.context)
    
    def post(self, request):
        
        details = self.FormType(request.POST)
        if details.is_valid(): 
            self.context["success_message"] = "Configurations has been saved"
            post = details.save()
            post.save() 
        else:
            self.context["success_message"] = "Configuration has not been saved"
        return render(request, self.template_name , self.context)


class HomeView(View):
    def __init__(self):
        self.template_name = "home.html" 
        self.context = {}
      

    def get(self, request):
        self.context["users"]  =User.objects.filter(is_staff=False)
        self.context["messages"]  = Message.objects.all()
        self.context['message_delete_url'] = "/delete/message/"
        self.context['user_delete_url'] = "/delete/user/"
        return render(request, self.template_name , self.context)
        
    def post(self, request):
        return HttpResponse("Does not implement", status_code = 500)

def delete_entry(request, model_name, entry_id):
    if (model_name == "user"):
        model_type = User
    elif (model_name == "message"):
        model_type = Message
    else:
        return redirect('/')
    model_type.objects.get(id = entry_id).delete()
    return  redirect('/')
def index(self):
    return HttpResponse("ok")