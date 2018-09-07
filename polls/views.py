from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
import datetime
from polls.forms import LoginForm




class StaticView(TemplateView):


    datee = datetime.datetime.now().date()
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat''sun']
    #template_name = "temp.html"


class AboutUs(View):
	def get(self, request, *args, **kwargs):
		context = {'name': 'Gryffindor'}
		return render(request, "temp.html", context=context)

def Display(request):
    return render(request,'hello.html',{})


def Detail(request):
    text = "<h1>welcome to my app number %s!</h1>" % id
    return render(request,'detail.html',{})
    #return redirect("Datee")

def Datee(request):
    datee= datetime.datetime.now().date()
    days=['mon', 'tue', 'wed','thu','fri','sat''sun']
    return render(request,'datee.html',{'datee':datee, 'days':days})
    #return redirect("Detail", x=1)


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():

            username = MyLoginForm.cleaned_data['xyz']

    else:
        MyLoginForm = LoginForm()

    return render(request, 'loggedin.html', {"username": username})

class Displayy(TemplateView):
    template_name = "login.html"