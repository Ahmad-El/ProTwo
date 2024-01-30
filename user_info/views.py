from django.shortcuts import render
from .models import User
from user_info.forms import NewUser
from django.http import HttpResponseRedirect


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = "user_info/home.html"

# def index(request):
#     return render(request, 'user_info/home.html')
    


# ## Using class
# class UserPageView(ListView):
#     template_name = "user_info/user.html"
#     model = User
#     fields = ["name", "surname", "email"]


## Using function
def user_page_view(request):
    user_list = User.objects.order_by("name")
    data_dict = {
        "user_list": user_list,
    }
    return render(request, "user_info/user.html", context=data_dict)

def index(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('')
            # return index(request)
        else:
            print("ERROR FORM INVALID")
    
    return render(request, 'user_info/home.html', {"form": form})