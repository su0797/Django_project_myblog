from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import JoinForm, LoginForm

# Create your views here.


### RegisterForm
class Join(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = JoinForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_join.html', context)
    
    def post(self, request):
        form = JoinForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')
        

###Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form':form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '이메일이 없습니다.')

        context = {
            'form': form
        }
        return render(request, 'user/user_login.html', context)


###Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('user:login')