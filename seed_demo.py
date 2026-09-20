"""Seed demo data: python manage.py shell < seed_demo.py"""
from django.contrib.auth.models import User
from blog.models import Category, Post, Comment
u, _ = User.objects.get_or_create(username='demo', defaults={'email': 'demo@test.com'})
u.set_password('demo12345'); u.save()
cats = []
for name, slug in [('تقنية', 'tech'), ('أعمال', 'business'), ('تعليم', 'learn')]:
    c, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
    cats.append(c)
samples = [
    ('لماذا Django مناسب للشركات الناشئة؟', 'tech', 'Django يوفر Admin جاهز، ORM قوي، وحماية CSRF/XSS افتراضيا...'),
    ('كيف تسعّر خدماتك على خمسات؟', 'business', 'احسب العمولة 20% ثم أضف هامش الدعم بعد التسليم...'),
    ('خطة تعلم Full-Stack في 90 يوم', 'learn', 'HTML/CSS ثم Python ثم Django ثم مشروع متجر كامل...'),
    ('PostgreSQL vs SQLite', 'tech', 'ابدأ SQLite ثم انتقل PostgreSQL عند النمو...'),
    ('نظام حجوزات يزيد مبيعات العيادات', 'business', 'فورم حجز + تحقق رقم + تذكير...'),
]
for title, cat_slug, body in samples:
    cat = Category.objects.get(slug=cat_slug)
    p, created = Post.objects.get_or_create(title=title, defaults={'author': u, 'category': cat, 'content': body})
    if created:
        Comment.objects.create(post=p, name='زائر', body='مقال مفيد، شكرا!')
print('seed done: demo/demo12345')
