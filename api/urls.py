from django.urls import path
from . import views

urlpatterns = [
    path('listposts/', views.ListPostsAPI.as_view(), name='list_posts'),
    path('listorgs/', views.ListOrgsAPI.as_view(), name='list_orgs'),
    path('listuserprofiles/', views.ListUserProfilesAPI.as_view(), name='list_userprofile'),
    path('listusers/', views.ListUsersAPI.as_view(), name='list_userprofile'),
    path('setcsrf/', views.SetCSRFCookie.as_view(), name='setcsrf'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]