# Learning Project based on "Добрый, добрый Django" course on <a href='https://stepik.org/course/183363/'>Stepik.org</a>

### The project is available <a href='https://k-dimitry.ru/'>here</a>. (link will be available until 18 April 2025)

### How it looks:
<img src="sitewomen/media/photos/2025/04/04/Screenshot k-dimitry.png" width="350" height="200">


### Technologies:
- Django
- PostrgeSQL
- Regis
- Nginx
- Docker

### Requirements:
```
asgiref==3.8.1
asttokens==3.0.0
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
cryptography==44.0.2
decorator==5.2.1
defusedxml==0.7.1
Django==5.1.7
django-debug-toolbar==5.1.0
django-environ==0.12.0
django-extensions==3.2.3
django-ranged-response==0.2.0
django-simple-captcha==0.6.2
executing==2.2.0
hiredis==3.1.0
idna==3.10
ipython==9.0.2
ipython_pygments_lexers==1.1.1
jedi==0.19.2
MarkupSafe==3.0.2
matplotlib-inline==0.1.7
oauthlib==3.2.2
parso==0.8.4
pexpect==4.9.0
pillow==11.1.0
prompt_toolkit==3.0.50
psycopg==3.2.6
psycopg-binary==3.2.6
psycopg-pool==3.2.6
ptyprocess==0.7.0
pure_eval==0.2.3
pycparser==2.22
Pygments==2.19.1
PyJWT==2.10.1
pyOpenSSL==25.0.0
python3-openid==3.2.0
redis==5.2.1
requests==2.32.3
requests-oauthlib==2.0.0
social-auth-app-django==5.4.3
social-auth-core==4.5.6
sqlparse==0.5.3
stack-data==0.6.3
traitlets==5.14.3
typing_extensions==4.13.1
Unidecode==1.3.8
urllib3==2.3.0
wcwidth==0.2.13
Werkzeug==3.1.3
```
### Installation
```commandline
cd sitewomen
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Starting the project
```commandline
python manage.py runserver
```
