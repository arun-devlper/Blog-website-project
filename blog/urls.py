from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.blog_list, name="list"),
    path('posts/<int:pk>/', views.blog_detail, name="detail"),
    path('like_posts/<int:pk>/', views.post_like, name="like"),
    path('post/search_results', views.search, name='search')
]
