from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    UserPostListView
                    )   
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
    path('material/new/', PostCreateView.as_view(), name = "materail-create"),
    path('material/<int:pk>/', PostDetailView.as_view(), name = "material-detail"),
    path('material/<int:pk>/update/', PostUpdateView.as_view(), name = "material-update"),
    path('material/<int:pk>/delete/', PostDeleteView.as_view(), name = "material-delete"),
    path('about/',views.about,name = 'blog-about'),

]
