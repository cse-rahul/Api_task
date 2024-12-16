# Django App API

## Setup Instructions
1. Install dependencies:<br>
  
   pip install django djangorestframework
   
2. Run migrations:<br>
python manage.py makemigrations<br>
python manage.py migrate

3.Start the server:<br>
python manage.py runserver

4.Use the following endpoints:<br>
Add App: POST /api/add-app/<br>
Get App: GET /api/get-app/{id}/<br>
Delete App: DELETE /api/delete-app/{id}/<br>
