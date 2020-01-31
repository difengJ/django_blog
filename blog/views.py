from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView, DeleteView
from .models import Material
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def home(request):
    context = {
        "materials":Material.objects.all()
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):
    model = Material
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'materials'
    ordering = ['-date_added']
    paginate_by = 2

class UserPostListView(ListView):
    model = Material
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'materials'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,username =self.kwargs.get('username'))
        return Material.objects.filter(author = user).order_by('-date_added')


class PostDetailView(DetailView):
    model = Material

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Material
    fields =['material_name','purchase_price','stock_price']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Material
    fields =['material_name','purchase_price','stock_price']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        material = self.get_object()
        if self.request.user == material.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Material
    success_url = '/'
    def test_func(self):
        material = self.get_object()
        if self.request.user == material.author:
            return True
        return False


def about(request):
    return render(request,"blog/about.html",{"title":"here is title"})