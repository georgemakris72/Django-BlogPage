from django.shortcuts import render, get_object_or_404#will return a 404 error if object does not exist, such as if you put post 1000 at end of url and didnt have that many posts
from .models import Post

# Create your views here.
def home(request):
    posts=Post.objects.order_by('-pub_date')#negative sign does it from bottom down whereas if you don't put this it will go by order of entry
    return render(request, 'posts/home.html', {'posts':posts})

def post_details(request, post_id):
    #post=Post.objects.get(pk=post_id)==>This was used prior to adding the error exception method below
    post =get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post':post})
