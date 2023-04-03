from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from posts.models import *
from .forms import PostForm
from accounts.models import *

# Create your views here.

def list(request):
    # posts = Post.objects.all()
    # for post in posts:
    #     print(post.id)
        # for user in post.recipients.all():
        #     print(user.profile)

    filter_map = {
        'title': 'title__icontains',
        'author': 'author'
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value

    posts = Post.objects.filter(**filters)
    return render(request, 'posts/list.html',  {'posts': posts})


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/show.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.POST["recipients"])
        if form.is_valid():
            post = form.save(commit=False)
            #  Adding starts to the UserProfile and to the Organisation
            recipients = get_object_or_404(User, id=int(request.POST["recipients"]))
            uprofile = UserProfile.objects.filter(user=recipients)
            post.add_stars_to_recipients(request.POST["recipients"], int(request.POST["stars"]), uprofile )
            company = get_object_or_404(Org, id=int(request.POST["company"]))
            company.add_stars(request.POST["stars"])
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
        return render(request, 'posts/new.html', {'form': form})
