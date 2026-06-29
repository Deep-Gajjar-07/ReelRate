# ReelRate

A movie review webapp built using Django. Users can browse movies by movie title or genre, read reviews and share their own opinions. Movie details is managed by the admin.

## Features
- Browse / search movies by title and genre
- User registration and login page
- User can write, edit and delete their reviews
- User profile with review history and average user rating

## Tech Stack
- Python
- Django
- SQLite DB
- Bootstrap 5

## Setup Instructions

1. Clone the respository <br>  ``` git clone https://github.com/Deep-Gajjar-07/ReelRate```
2. Create a virtual environment <br> `python -m venv venv`
3. Activate virtual environment <br> `venv\Scripts\activate`
4. Install dependencies <br> `pip install -r requirements.txt `
5. Create / copy `.env` file from example <br> `cp .env.example .env` <br>
   Then add your own `SECRET_KEY` in `.env`
6. Run migrations <br> `python manage.py migrate`
7. Create superuser <br> `python manage.py createsuperuser`
8. Run server <br> `python manage.py runserver`

## Screenshots
<img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/7e741605-4330-4da6-ae1b-6f4b780a7d4d" />
<img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/b138a58b-959e-417f-bfca-7206812d4d11" />
<img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/853b61f4-0838-4c86-80f8-c08209af7c3f" />
<img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/8c3ee6df-3090-4034-b00d-f50447b5c962" />

***Note: Movie posters used for demo purposes only.***
