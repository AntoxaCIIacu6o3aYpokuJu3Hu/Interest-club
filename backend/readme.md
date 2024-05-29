**How to get the backend server up and running**

You need to run a series of commands in the terminal

The assumption is that you are using Windows. If you are on Linux or Mac (and so, are using bash instead of cmd or powershell), you would need to edit some commands (replace '\' with '/', maybe 'python' with 'python3', and the process of activating the virtual environment could also be different).

Change directory to the backend:
```
cd .\backend
```
Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment. This step depends on the terminal you are using. If you are using cmd:
```
.\venv\Scripts\activate.bat
```
If you are using powershell:
```
.\venv\Scripts\activate.ps1
```
Install all the needed dependencies:
```
pip install -r requirements.txt
```
Move to the django project directory, make and apply database migrations:
```
cd .\interest_club
python .\manage.py startapp makemigrations
python .\manage.py startapp migrate
```
Create an admin user. Run the following command and follow the prompts:
```
python manage.py createsuperuser 
```
Start the server
```
python manage.py runserver
```

**Exploring the API**

Start the server and follow this link:

[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

The the page is completely blank, try oppening in an another tab.

On this page you can see all the endpoint implemented on the backend. You can send request to each of them - the page would have examples of request bodies that you can modify.

To access most endpoint, you need to be logged in. Use the /api/token endoint with your username and password (you can create a user with the /api/users/registration/ endpoint, through the admin page or with 'python manage.py createsuperuser'). You would be given an short-lived access token and an long-lived refresh token. You can use the refresh token to get a new access token through the /api/token/refresh/ endpoint once the previous one expires. You can log in by pressing a big green 'Authorize' button on the top-right of the page and entering an access token.

**Accessing the admin menu**

Start the server and follow this link:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

You can use the admin panel to add, modify and delete database entries, such as users, groups, records(events/topics) and comments.
