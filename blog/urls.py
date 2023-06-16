
from django.urls import path
from . import views

app_name = "detail"
urlpatterns = [
    path("search/", views.search, name="search"),
    path("<slug:category_slug>/<slug:slug>", views.detail, name="post_detail"),
    path("<slug:slug>/", views.category, name="category_detail"),
] 
