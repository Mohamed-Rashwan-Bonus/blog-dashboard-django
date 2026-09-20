from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True) or self.name.replace(' ', '-')
        super().save(*args, **kwargs)
    def __str__(self): return self.name
    class Meta: verbose_name_plural = 'Categories'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: ordering = ['-created_at']
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title, allow_unicode=True) or 'post'
            slug, i = base, 1
            while Post.objects.filter(slug=slug).exists():
                i += 1; slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)
    def get_absolute_url(self): return reverse('blog:post_detail', args=[self.slug])
    def __str__(self): return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['created_at']
    def __str__(self): return f"{self.name} on {self.post.title[:30]}"
