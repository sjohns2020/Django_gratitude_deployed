from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from orgs.models import *
from .forms import OrgForm

# Create your views here.

def list(request):
    # posts = Post.objects.all()
    # for post in posts:
    #     print(post.id)
        # for user in post.recipients.all():
        #     print(user.profile)

    # filter_map = {
    #     'title': 'title__icontains',
    #     'author': 'author'
    # }

    # filters = {}
    # for key, value in request.GET.items():
    #     filter_key = filter_map[key]
    #     filters[filter_key] = value

    # posts = Post.objects.filter(**filters)
    orgs = Org.objects.all()
    return render(request, 'orgs/list.html',  {'orgs': orgs})



def org_details(request, id):
    org = get_object_or_404(Org, id=id)
    return render(request, 'orgs/show.html', {'org': org})


@login_required
def org_new(request):
    if request.method == "POST":
        form = OrgForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('orgs')
    else:
        form = OrgForm()
        return render(request, 'orgs/new.html', {'form': form})
