from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import User

# Create your views here.
class HomePageView(TemplateView):
    template_name = "user_info/home.html"


class UserPageView(ListView):
    template_name = "user_info/user.html"
    model = User
    fields = ["name", "surname", "email"]