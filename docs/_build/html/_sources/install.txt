Установка
=========

* Скопируйте или склонируйте проект в необходимую Вам папку ``https://github.com/DonBanan/django-forum``
* Установите виртуально окружение ``virtualenv --no-site-packages venv``
* Активируйте виртуально окружение ``source venv/bin/activate``
* Установите все зависимости ``pip install -r requirements.txt``
* Синхронизируйте базу данных командой ``manage.py migrate``
* Соберите статику ``manage.py collectstatic``