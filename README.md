# Portfolio
General Portfolio for fun and profit - build in Python / Django, and more. 

to start up for localhost: 

python -m venv thisenv
source thisenv/bin/activate

*thisenv can be changed to whatever you like. I saw venv used often.*

cd mydjangoserver

as of v1.3, now secure: 
python manage.py runsslserver
server address https://127.0.0.1:8000/

Admin panel:
https://127.0.0.1:8000/admin/

if initial users are needed, utilize: 
python manage.py create_initial_users

Current next steps: 
 Set up auth backend
 set up admin page
 set front end - index page with login-> content based on role

older instructions: 
  python manage.py runserver 
  (defaults to http://127.0.0.1:8000/)

