from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.contrib import messages
from .models import Post, Category
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 9
    def get_queryset(self):
        qs = Post.objects.filter(is_published=True).select_related('author', 'category')
        q = self.request.GET.get('q', '').strip()
        cat = self.request.GET.get('category', '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        if cat:
            qs = qs.filter(category__slug=cat)
        return qs
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.annotate(n=Count('posts'))
        ctx['q'] = self.request.GET.get('q', '')
        ctx['active_cat'] = self.request.GET.get('category', '')
        return ctx

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = CommentForm()
        ctx['comments'] = self.object.comments.all()
        return ctx
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False); c.post = self.object; c.save()
            messages.success(request, 'تم نشر تعليقك بنجاح')
            return redirect(self.object.get_absolute_url())
        ctx = self.get_context_data(); ctx['form'] = form
        return self.render_to_response(ctx)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post; form_class = PostForm; template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'تم نشر المقال')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post; form_class = PostForm; template_name = 'blog/post_form.html'
    slug_field = 'slug'
    def get_queryset(self): return Post.objects.filter(author=self.request.user)
    def form_valid(self, form):
        messages.success(self.request, 'تم حفظ التعديلات')
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post; template_name = 'blog/post_confirm_delete.html'
    slug_field = 'slug'; success_url = reverse_lazy('blog:post_list')
    def get_queryset(self): return Post.objects.filter(author=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'تم حذف المقال')
        return super().delete(request, *args, **kwargs)

def register_view(request):
    if request.user.is_authenticated: return redirect('blog:post_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(); login(request, user)
            messages.success(request, 'تم إنشاء حسابك بنجاح')
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()
    return __import__('django.shortcuts', fromlist=['render']).render(request, 'registration/register.html', {'form': form})
