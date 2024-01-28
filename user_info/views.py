from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import User


# Create your views here.
class HomePageView(TemplateView):
    template_name = "user_info/home.html"


## Using class
class UserPageView(ListView):
    template_name = "user_info/user.html"
    model = User
    fields = ["name", "surname", "email"]


## Using function
def user_page_view(request):
    user_list = User.objects.order_by("name")
    data_dict = {
        "user_list": user_list,
    }
    return render(request, "user_info/user.html", context=data_dict)
