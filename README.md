# Blog + Dashboard — Django MVT (Portfolio Project 2)

Solo build — نفس ستاك الـ E-Shop: Django + SQLite/PostgreSQL + Bootstrap 5 + HTML/CSS/JS.

## الفكرة (للعميل العربي)
موقع مقالات/أخبار مع لوحة تحكم: تسجيل دخول، إضافة/تعديل/حذف مقال، تعليقات، بحث، تصنيفات.

## هتبنيه في يوم واحد — Checklist
- [ ] `py -m venv venv` + `pip install django pillow`
- [ ] `django-admin startproject config .` + `python manage.py startapp blog`
- [ ] Models:
```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    def __str__(self): return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```
- [ ] Admin: سجل الـ 3 موديلز في `admin.py`
- [ ] Views: list + detail + search (`?q=`) + filter by category + Create/Update/Delete بـ `LoginRequiredMixin`
- [ ] Templates بـ Bootstrap 5 (انسخ `base.html` من مشروع E-Shop عندك وغير الألوان)
- [ ] Auth جاهز من Django: `/accounts/login/` + register بسيط
- [ ] Seed: 5 مقالات تجريبية + سكرينتين

## Run
```powershell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## للرفع على GitHub
1. اعمل repo جديد `blog-dashboard-django`
2. `git init; git add .; git commit -m "blog + dashboard solo"; git push`
3. خد سكرينين (رئيسية + لوحة تحكم) وحطهم في README فوق + لينك اللايف لو رفعه على Render/PythonAnywhere

## وصف جاهز لمستقل (انسخه)
> **مدونة احترافية مع لوحة تحكم - Django + Bootstrap**
> نظام مقالات كامل: تصنيفات، بحث لحظي، تعليقات، رفع صور، ولوحة تحكم للنشر والتعديل والحذف مع صلاحيات. بناء فردي كامل من الصفر بقاعدة SQLite/PostgreSQL وتصميم متجاوب.
