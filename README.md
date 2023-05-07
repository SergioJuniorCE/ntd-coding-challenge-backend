NTD Coding Challenge backend

# Requisites

- Having python 3.7+ installed
- Having virtualenv module installed
  - If not run:
  - `pip install virtualenv`

# Steps to run

- Create a environment

  - `python -m virtualenv env`
- Then activate the script

  - For Windows
    - `env/Scripts/Activate`
  - For Linux/Mac
    - `env/bin/activate`
- Once the environment is created installed all the modules necesary

  - `pip install -r requirements.txt`
- Add the required `.env` file attatched to the email to the root folder
- Run the server with

  - `python manage.py runserver`

# Production URL

https://ntd-coding-challenge-backend.herokuapp.com/
