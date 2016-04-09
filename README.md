# forum

Install:

git clone <repo> .

virtualenv --no-site-packages venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
