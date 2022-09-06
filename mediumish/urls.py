from django.urls import path
from . import views

app_name = 'mediumish'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostView.as_view(), name='post'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('author/<int:user_id>', views.AuthorDetailView.as_view(), name='authordetail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('post/<slug:slug>', views.IndexDetailView.as_view(), name='detail'),
]

