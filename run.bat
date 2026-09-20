@echo off
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
  echo Creating venv...
  py -m venv venv
  call venv\Scripts\activate
  pip install -r requirements.txt
) else (
  call venv\Scripts\activate
)
if not exist db.sqlite3 (
  python manage.py migrate
  python manage.py shell --command="exec(open('seed_demo.py',encoding='utf-8').read())"
  echo seeded demo/demo12345
)
python manage.py runserver
