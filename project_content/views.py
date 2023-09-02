from django.views.generic import ListView,FormView
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User

class HomeView(ListView):
    template_name = "project_content/home.html"
    context_object_name = 'mydata'
    model = Locations
    #form_class = EmailForm
    success_url = "/"


