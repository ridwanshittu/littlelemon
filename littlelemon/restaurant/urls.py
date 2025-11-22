#define URL route for index() view
from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Create a new router instance
#router = DefaultRouter()


urlpatterns = [

    path('', views.index, name='index'),
    #add following lines to urlpatterns list 
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
