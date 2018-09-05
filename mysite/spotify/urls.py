from django.urls import path
from . import views
app_name = "spotify"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('prompt/', views.prompt, name='prompt'),
    path('home/', views.home, name='home'),
]