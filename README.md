"# DjangoRestAPI_0" 

## A RestFul API for CRUD operation using class-based based view

 1. Install pip
 # update pip version
 	python.exe -m pip install --upgrade pip

 2. Create virtual environment
	py -m venv virtualEnvName

 3. Activate Virtual Env
	virtualEnvName\Scripts\activate.bat

 4. Install Django (inside virtual environment)
	py -m pip install Django
	pip install django

 5. Check django version
	django-admin --version

 6. Create Django project (inside virtualEnvName)
	django-admin startproject projectName

	# create app
	py manage.py startapp appname

 7. Run the project
	py manage.py runserver

 8. Install rest-framework
	pip install djangorestframework

 9. Install cors-header
	pip install django-cors-headers

 10. Database drivers
	# postgress
	pip install pyscopg2

	solve improperly configured
	pip install psycopg2-binary --force-reinstall --no-cache-dir