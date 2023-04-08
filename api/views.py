from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from posts.models import Post
from orgs.models import Org
from accounts.models import UserProfile
from django.contrib.auth.models import User
from .serializers import (
    PostSerializer,
    OrgSerializer,
    UserProfileSerializer,
    UserSerializer,
    LoginSerializer,
    RegistrationSerializer,

)
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    AllowAny,
)
from rest_framework.decorators import (
    permission_classes,
    authentication_classes,
)
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse

csrf_protect_method = method_decorator(csrf_protect)
ensure_csrf = method_decorator(ensure_csrf_cookie)


method_decorator_csrf_protect = method_decorator(csrf_protect)
method_decorator_ensure_csrf_cookie = method_decorator(ensure_csrf_cookie)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

# Posts
class ListPostsAPI(generics.ListAPIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Orgs
class ListOrgsAPI(generics.ListAPIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    queryset = Org.objects.all()
    serializer_class = OrgSerializer

# UserProfiles
class ListUserProfilesAPI(generics.ListAPIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAuthenticated,]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Users (only Admin can see this)
class ListUsersAPI(generics.ListAPIView):
    authentication_classes=[SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SetCSRFCookie(APIView):
    permission_classes = []
    authentication_classes = []
    @ensure_csrf
    def get(self, request):
        return Response("CSRF Cookie set.")


class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    # @csrf_protect_method
    def post(self, request):
        csrf_token = get_token(request)

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("Logged in")

class LogoutView(APIView):
    authentication_classes=[SessionAuthentication,]
    permission_classes = [IsAuthenticated,]

    @method_decorator(csrf_protect)
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request):
        logout(request)
        response = Response({'detail': 'Logged out'}, status=status.HTTP_200_OK)
        response.delete_cookie('csrftoken')
        return response


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authenticated_user = serializer.save()
        login(request, authenticated_user)
        return Response("Registration successful")




