## To run a migration
When model is altered in the 'app' app:

```
python manage.py makemigrations app
```

To see the resultant sql script:

```
python manage.py sqlmigrate app <migration number>
```

```
python manage.py migrate
```