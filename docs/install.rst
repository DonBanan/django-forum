Установка
=========

* Скопируйте или склонируйте проект в необходимую Вам папку ``git clone https://github.com/DonBanan/django-forum``
* Установите виртуально окружение ``virtualenv --no-site-packages venv``
* Активируйте виртуально окружение ``source venv/bin/activate``
* Установите все зависимости ``pip install -r requirements.txt``
* Синхронизируйте базу данных командой ``python manage.py migrate``
* Соберите статику ``python manage.py collectstatic``
* Создайте администратора ``python manage.py createsuperuser``