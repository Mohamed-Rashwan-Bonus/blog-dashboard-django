# مدونة بلوحة تحكم — Django

عملت المشروع ده عشان كان عندي عملاء بيطلبوا موقع مقالات بسيط مع لوحة تحكم عربي، فحبيت يكون عندي Base جاهز أعدل عليه.

## بيشتغل إزاي
- الرئيسية: قايمة مقالات بتصنيفات + بحث + ترقيم صفحات
- صفحة المقال: المحتوى + التعليقات + فورم تعليق
- لو عايز تنشر: سجل حساب جديد من `/accounts/register/` وبعدها زرار "مقال جديد" بيظهر فوق
- التعديل والحذف ظاهرين لصاحب المقال بس
- الأدمن الكامل على `/admin/` (تصنيفات/مقالات/تعليقات)

## التشغيل عندي (Windows)
```powershell
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())"
python manage.py runserver
```
بعدها افتح `http://127.0.0.1:8000` وجرب حساب `demo / demo12345`.

ملحوظة: الصور بتترفع في `media/` وهي معمولها ignore، والـ seed بيعمل 5 مقالات تجريبية وتعليق واحد على كل مقال.

## اللي اتعلمته وأنا ببنيه
- السلاج العربي كان بيكسر الـ URL عشان `<slug:slug>` مبتقبلش عربي، فغيرتها لـ `<str:slug>`.
- كنت بجيب `get_absolute_url` غلط في الأول مع الترقيم، ظبطها بعد التجربة.
- التعليقات عملتها POST في نفس صفحة المقال عشان مفيش داعي لصفحة منفصلة.

## الملفات المهمة
`blog/models.py` (Category/Post/Comment) — `blog/views.py` (List/Detail/Create/Update/Delete) — `templates/blog/` — `seed_demo.py`

## مشاريعي التانية
- المتجر: https://github.com/Mohamed-Rashwan-Bonus/eshop-django
- الحجوزات: https://github.com/Mohamed-Rashwan-Bonus/clinic-booking-django

محمد رشوان — Django Full-Stack (القاهرة)
