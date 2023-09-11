# DBMS Project

This is the Postgraduate students management software project for managing postgraduate students' academic records and research projects.

## Installation

**Fork the project to your GitHub account**

**Clone the repo to your local machine**

**Create a python virtual environment**

On Windows:
```sh
$ python -m virtualenv env
```
On Linux/macOS:
```sh
$ python3 -m venv env
```

**Activate the virtual environment**

On Windows:
```sh
$ env\Script\activate
```
On Linux/macOS:
```sh
$ source env/bin/activate
```
**Install project packages**

On Windows & Linux/macOS:
```sh
$ pip install -r requirements.txt
```
- You're all set! 🕺🏽

---

## Project setup

**Within the root folder, create a .env**

**Update the .env file with the details in .env.example**

**Substitute the SECRET_KEY value with one you generated**

**Migrate the database**

On Windows:
```sh
$ python manage.py makemigrations
```
```sh
$ python manage.py migrate
```
Linux/macOS:
```sh
$ python3 manage.py makemigrations
```
```sh
$ python3 manage.py migrate
```

**You can now start making amazing contributions! 👍🏾**

---

> Please note that if you meet any bug during the setup, feel free to reach out so that all the bugs can be _crushed_. 😁
