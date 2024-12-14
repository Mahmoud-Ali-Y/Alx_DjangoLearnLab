from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.messages import messages
from .forms import PostForm, UserRegisterForm
from django.views.generic.edit import CreateView, SuccessMessageMixin, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class UserCreationForm(SuccessMessageMixin, CreateView):
  template_name = 'blog/register.html'
  success_url = reverse_lazy('blog/login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
  user = User.objects.create()

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class POST:
    def method():
        post = Post.objects.create()
        post.save()

class PostListView(ListView):
    model = Post
    template_name = 'post.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'
        
@permission_required('blog.can_add_Post', login_url="blog/login/")
class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'new.html'
    success_url = reverse_lazy('/post/')
    login_url = 'blog/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        # Attach the currently logged-in user as the author before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

@permission_required('blog.can_edit_Post', login_url="blog/login/")
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'update.html'
    success_url = reverse_lazy('/post/<int:pk>/')
    login_url = 'blog/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        # Attach the currently logged-in user as the author before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

@permission_required('blog.can_delete_Post', login_url="blog/login/")
class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('/post/')
    login_url = 'blog/login/'
    redirect_field_name = 'redirect_to'
    

