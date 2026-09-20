#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell --command="from django.contrib.auth.models import User; User.objects.filter(username='demo').exists() or User.objects.create_superuser('demo','demo@test.com','demo12345')"
