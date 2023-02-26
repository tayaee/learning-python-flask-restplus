# learning-python-flask-restplus

Learning Python Flask-RESTPlus
from https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/

* setup
    * git clone ...
    * set "PATH=<path-to-python.exe-3.11>\bin;%PATH%"
    * setup-venv.bat
        * Replaced virtualenvwrapper with venv
* flask-migrate with flask
    * python manage.py run // OK
    * set "FLASK_APP=app.main:create_app('dev')" & set FLASK_DEBUG=0
    * flask db init
    * flask db migrate
    * flask db upgrade
    * dir app\main\main.db // created but no tables
* test
    * python manage.py test // all succeeded