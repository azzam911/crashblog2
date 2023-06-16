from django.urls import path
from .views import frontpage , about
app_name = 'home'
urlpatterns = [
    path('', frontpage, name="home"),
    path('about/', about, name="about"),
]
