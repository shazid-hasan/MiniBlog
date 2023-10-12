from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{"posts":posts})

def about(request):
    return render (request,'blog/about.html')

def contact(request):
    return render (request,'blog/contact.html')

def dashboard(request):
    return render (request,'blog/dashboard.html')

def user_logout(request):
    return HttpResponseRedirect('/')
    # return render (request,'blog/logout.html')    

def user_login(request):
    form = LoginForm()
    return render (request,'blog/login.html',{'form':form})


def user_signup(request):
    form =  SignUpForm()
    return render (request,'blog/signup.html', {'form':form})