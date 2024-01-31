required package:
asgiref==3.7.2
Django==5.0.1
django-multiupload==0.6.1
djangorestframework==3.14.0
pillow==10.2.0
psycopg2-binary==2.9.9
python-decouple==3.8
pytz==2023.4
sqlparse==0.4.4
typing_extensions==4.9.0
tzdata==2023.4

Installation:
step-by-step instructions on how to install the project locally. Including commands:

git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt

Configuration:
Environment Variables:
Create a .env file with the following content:

# .env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=task_db
DB_USER=postgres
DB_PASSWORD=kpHq979#
DB_HOST=localhost
DB_PORT=5432


Running the Project:
Database Setup:
python manage.py migrate

Run Development Server:
python manage.py runserver

API Documentation:
API Endpoints:
Document your API endpoints, including their paths:

List all tasks:

Endpoint: http://127.0.0.1:8000/tasks/
Method: GET

Create a task:

Endpoint: http://127.0.0.1:8000/tasks/create/
Method: POST

retrieve a single task:

Endpoint: http://127.0.0.1:8000/tasks/3/
Method: GET

update an existing task:

Endpoint: http://127.0.0.1:8000/tasks/update/3/
Method: PUT

delete an task:

Endpoint: http://127.0.0.1:8000/tasks/delete/3/
Method: 







