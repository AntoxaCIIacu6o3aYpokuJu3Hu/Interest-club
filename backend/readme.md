**How to get the backend server up and running**

You need not run a series of commands in the terminal

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