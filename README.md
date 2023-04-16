# e-wallet-rest-creative-solution
For the creative solution dev test
Build with python 3.8 + FastAPI

Run task 1 and 2
------------------
Go into directory called task-1-and-2
simply run:
```
python3 palindrome.py
python3 sudoku.py
```
in your terminal or cmd


Run task 3
------------------

Virtual Environment
====================
To run the project, you must create and activate the virtual environment first.

Windows : 
- python3 -m venv env
- cd env/Script/activate

Linux : 
- python3 -m venv env
- source ./env/bin/activate
- install dependencies from requirements.txt (file is inside the app folder)
- pip3 install -r requirements.txt

after that, you must create .env file with the value below (copy all of this):
```
APP_NAME = "ewallet-rest-api"
ORIGINS=["*"]
CORS_ALLOW_METHODS=["*"]
CORS_ALLOW_HEADERS=["*"]
DATABASE_URL = "postgresql://{postgres_user}:{pass}@{your_host}/{your_db_name}"
SECRET_KEY = "dRgUjXn2r5u8x/A?D(G+KbPeShVmYp3s6v9y$B&E)H@McQfTjWnZr4u7w!z%C*F-"
```

create database in postgresql:
```
create database {your_db_name}
```

and then you can run it by:
```
python3 main.py
```
