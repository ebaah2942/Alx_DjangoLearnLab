from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import ProfileForm, PostForm, CommentForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from django.db.models import Q
from taggit.models import Tag



# Create your views here.
# class PostByTagListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         tag_slug = self.kwargs['tag_slug']
#         tag = Tag.objects.get(slug=tag_slug)
#         return Post.objects.filter(tags=tag)


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'



class PostDetailView(DetailView):
    model = Post    
    template_name = 'blog/post_detail.html'
   

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = self.object.pk
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Retrieve the related blog post
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.blog_post = post  # Associate comment with the blog post
        form.instance.author = self.request.user  # Set the comment author
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.blog_post.get_absolute_url()    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        return self.get_object().author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        return self.get_object().author == self.request.user         



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # fields = ['title', 'content', 'tags']
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        tags = form.cleaned_data.get('tags')
        if tags:
            self.object.tags.set(*tags.split(','))  # Split tags and set them
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'posts_by_tag.html', {'posts': posts, 'tag': tag})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})


def is_staff_and_superuser(user):
    return user.is_staff and user.is_superuser
@login_required
def edit_profile(request):
      # Default to only basic fields for regular users
    allowed_fields = ['first_name', 'last_name', 'email']

    if request.user.is_superuser:
        # Superuser: Access all fields
        allowed_fields = '__all__'
    elif request.user.is_staff:
        # Staff: Additional permissions (optional, modify if needed)
        allowed_fields = ['first_name', 'last_name', 'email']

    # Initialize the form with dynamic fields
    form = ProfileForm(request.POST or None, instance=request.user, user=request.user, allowed_fields=allowed_fields)

    # Handle form submission
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'blog/edit_profile.html', {'form': form})



def home_view(request):
    return render(request, 'blog/home.html')



def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})



# def posts_by_tag(request, tag_name):
#     tag = get_object_or_404(Tag, name=tag_name)
#     posts = tag.posts.all()
#     return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})


def logout(request):
    logout(request)
    return redirect('login')

