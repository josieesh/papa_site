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

## To run app locally
Create venv and install requirements
```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Configure development environment.
First run the python shell:
```
python manage.py shell
```
Then enter the following lines sequentially:
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

Run the server.
```
python manage.py runserver
```

## Pushing latest commit to Heroku
```
git push heroku master
```