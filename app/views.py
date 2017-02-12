from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
class HomeView(TemplateView):
    template_name = 'app/home.html'



def logout_view(request):
    logout(request)
    return redirect('app:home')

class login_view(View):
    def get(self,request):
        return render(request,'app/home.html')
    def post(self,request):
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                # albums = Album.objects.filter(user=request.user)
                return render(request,'app/login.html')
            else:       #inactive user
                #using the messages framework
                messages.success(request,'Your account has been disabled')
                return redirect('app:home',)

        #form not valid- using the message framework
        messages.success(request,'Error. Please try again. Are you trying to create a new account?')
        return redirect('app:home',)
