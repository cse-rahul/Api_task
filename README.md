# Django App API

## Setup Instructions
1. Install dependencies:
  
   pip install django djangorestframework
   
2. Run migrations:
python manage.py makemigrations
python manage.py migrate

3.Start the server:
python manage.py runserver

4.Use the following endpoints:
Add App: POST /api/add-app/
Get App: GET /api/get-app/{id}/
Delete App: DELETE /api/delete-app/{id}/
