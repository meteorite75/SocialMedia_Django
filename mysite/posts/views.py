from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        post_image = request.FILES.get('post_image')
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user=user, image = post_image, caption = caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')