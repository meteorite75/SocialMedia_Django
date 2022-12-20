from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Likepost

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
    
@login_required(login_url='login')
def like_post(request):
    post_id = request.GET.get('post_id')
    post_liker = request.user.username
    
    post = Post.objects.get(id=post_id)
    
    like_filter = Likepost.objects.filter(post_id=post_id, post_liker=post_liker).first()
    
    if like_filter: 
        like_filter = like_filter.delete()
        post.num_of_likes -= 1
        post.save()
        return redirect('/')
        
    else:    
        new_like = Likepost.objects.create(post_id=post_id, post_liker=post_liker)
        new_like.save()
        post.num_of_likes += 1
        post.save()
        return redirect('/')
        
    