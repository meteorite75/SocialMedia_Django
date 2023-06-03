from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, FollowersCount
from posts.models import Post
from itertools import chain


@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    
    user_following_list = []
    feed = []
    
    user_following = FollowersCount.objects.filter(follower = request.user.username)
    
    for i in user_following:
        user_following_list.append(i.followed_user)
        
    for i in user_following_list:
        feed_list = Post.objects.filter(user = i)
        feed.append(feed_list)
    
    feed_list = list(chain(*feed))
    
    
    posts = Post.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feed_list})

@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
            
        if request.FILES.get('image'):
            image = request.FILES['image']
            bio = request.POST['bio']
            location = request.POST['location']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.save()
            
        else:
            # image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            
            # user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.save()
            
        return redirect('settings')
    
    return render(request, 'setting.html', {'user_profile': user_profile})

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
                
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user = user_model, id_user = user_model.id , first_name = user_model.first_name, last_name = user_model.last_name)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username =username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "You haven't signup yet")
            return redirect('login')
    else:
        return render(request, 'signin.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request , pk):
    user_object = User.objects.get(username = pk)
    profile_user = Profile.objects.get(user = user_object)
    user_posts = Post.objects.filter(user = pk)
    user_post_lenth = len(user_posts)
    
    follower = request.user.username
    followed_user = pk
    
    if FollowersCount.objects.filter(follower = follower, followed_user = followed_user).first():
        button_text = 'unfollow'
    else:
        button_text = 'follow'
        
    # users who followed this profile
    user_followers = len(FollowersCount.objects.filter(followed_user = pk))
    # users that this profile has follwed
    user_followings = len(FollowersCount.objects.filter(follower = pk))
        
    
    context = {
        'user_object': user_object,
        'profile_user': profile_user,
        'user_posts' : user_posts,
        'user_post_lenth' : user_post_lenth,
        'button_text' : button_text,
        'user_followers' : user_followers,
        'user_followings' : user_followings,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def follow(request):

    if request.method == 'POST':
        follower = request.user.username
        followed_user = request.POST['followed_user']
        
        if FollowersCount.objects.filter(follower = follower , followed_user = followed_user).first():
            follower_delete = FollowersCount.objects.get(follower = follower, followed_user = followed_user)
            follower_delete.delete()
            return redirect('/profile/'+followed_user)
        else:
            new_follower = FollowersCount.objects.create(follower = follower , followed_user = followed_user)
            new_follower.save()
            return redirect('/profile/'+followed_user)
        
    else:
        return redirect('/')
    