web: gunicorn papa_site.wsgi -c ./gunicorn.conf
release: python manage.py makemigrations app; python manage.py migrate