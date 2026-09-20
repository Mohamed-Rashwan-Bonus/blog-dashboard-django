# Blog + Dashboard — Django MVT (Solo Build)

![Django](https://img.shields.io/badge/Django-5.x-green) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple) ![SQLite](https://img.shields.io/badge/SQLite-ready-blue) ![Solo](https://img.shields.io/badge/Built-solo-orange)

مدونة عربية كاملة مع لوحة تحكم — نفس ستاك متجر E-Shop: **Django MVT + Bootstrap 5 + SQLite**.

## Demo
- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/` — demo: `demo / demo12345` (بعد تشغيل seed)
- Register: `/accounts/register/` — Login: `/accounts/login/` — New post: `/new/`

## Features
- مقالات بتصنيفات + بحث لحظي (`?q=`) + فلترة (`?category=slug`) + ترقيم صفحات (9/صفحة)
- صفحة مقال مع تعليقات + عداد تعليقات
- نشر/تعديل/حذف للمؤلف فقط (`LoginRequiredMixin` + queryset مقيد)
- رفع صور (`Pillow`) + Admin كامل (بحث/فلترة) + رسائل Toast
- تصميم RTL عربي متجاوب Bootstrap 5

## Run (Windows — دقيقتين)
```powershell
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())"
python manage.py runserver
```
أو دبل كليك على `run.bat`.

## Structure
```
config/ (settings, urls) | blog/ (models, views, urls, forms, admin)
templates/ (base, blog/*, registration/*) | static/css | seed_demo.py
```

## Models
`Category(name, slug)` — `Post(author, category, title, slug, content, image, is_published)` — `Comment(post, name, body)`

## Screenshots
حط هنا 2 سكرين (الرئيسية + صفحة مقال). مؤقتا استخدم أغلفة `../khamsat-covers/` عند الرفع لمستقل.

## Author
Solo build by **Mohamed Rashwan** — part of Django portfolio:
- E-Shop: https://github.com/Mohamed-Rashwan-Bonus/eshop-django
- Clinic booking: https://github.com/Mohamed-Rashwan-Bonus/clinic-booking-django
