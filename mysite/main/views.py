from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Profile



class IndexView(TemplateView):
    template_name = "index.html"

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password , first_name=first_name, last_name=last_name)
                user.save()
                
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user = user_model, id_user = user_model.id , first_name = user_model.first_name, last_name = user_model.last_name)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')