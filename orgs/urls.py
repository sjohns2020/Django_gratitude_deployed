from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name='orgs'),
    path('new/', views.org_new, name='org_new'),
    path('<int:id>/', views.org_details, name='org_details')
]