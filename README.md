# employee_api

urls

http://127.0.0.1:8000/api/employee/     GET & POST methods are available in this url for getting all employees and post single employees data

http://127.0.0.1:8000/api/employee/edit-employee/      GET,PUT,DELETE methodes are in here for editing employee and you can pass params in "regig"

all requirements are added on requirements.txt

python version 3.9.13
rest framework used for developing apis

am used ini file for connecting database details :

[settings]
DEBUG = True
SERVER = True
ALLOWED_HOSTS = *, .localhost, .127.0.0.1,
; Postgresql details
DB_NAME =
DB_USER =
DB_PASSWORD =
DB_HOST = localhost
DB_PORT = 5432

