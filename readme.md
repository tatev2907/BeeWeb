# Project Title
The main object of the project is to build a URL shortening site, similar to bit.ly, tinyurl etc
## Instructions

As always ensure you create a virtual environment for this application and install the necessary libraries from the requirements.txt file.

Installation
-----------
Install dependencies from `requirements.txt`
```
$ pip install -r requirements.txt
```
How to run
-------------
```
(venv) $ ./manage.py runserver 
```
To see your application, access this url in your browser:
`http://127.0.0.1:8000` 

Create fake users
-------------
For query randomuser.me  100 accounts, then import them into the system just run
```bash
./manage.py manage.py	create_fake_users 100
```
