from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from posts.models import Post
from orgs.models import Org
from accounts.models import UserProfile
from django.contrib.auth.models import User
from .serializers import PostSerializer
from .serializers import OrgSerializer
from .serializers import UserProfileSerializer
from .serializers import UserSerializer

# Posts
class ListPostsAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Orgs
class ListOrgsAPI(generics.ListAPIView):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer

# UserProfiles
class ListUserProfilesAPI(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Users
class ListUsersAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
