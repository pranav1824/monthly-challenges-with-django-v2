# monthly-challenges-with-django-v2
monthly challenges with django v2


Monthly Challenges with Django v2
This repository contains a Django-based web application that showcases monthly challenges. Each challenge represents a unique task or goal that users can complete. The web app displays a list of challenges by month and provides detailed information about each challenge.

Features
Monthly Challenge Display: List of challenges based on the month.
Challenge Detail Page: Specific page for each challenge with more information.
Dynamic URL Routing: Users can visit each challenge through URLs corresponding to the month.
Error Handling: Custom error pages for invalid challenge URLs.
Technologies Used
Django 4.x: The web framework used for development.
HTML/CSS: For frontend UI and styling.
SQLite3: Django's default database for data storage.
Installation
To set up the project locally, follow these steps:

Clone the repository:
git clone https://github.com/pranav1824/monthly-challenges-with-django-v2.git

Navigate to the project directory:
cd monthly-challenges-with-django-v2

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate

On MacOS/Linux:
source venv/bin/activate


Install the required dependencies:
pip install -r requirements.txt

Run the Django server:
python manage.py runserver

Run the application and open your browser and go to:
http://127.0.0.1:8000/


Usage
Visit the homepage to view a list of monthly challenges.
Click on any month to see the details of the corresponding challenge.
Navigate through the months using dynamic URLs like /challenges/january.


Project Structure
monthly-challenges-with-django-v2/
│
├── challenges/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── challenges/
│   │       ├── index.html
│   │       ├── challenge.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── ...
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md

Contributing
Feel free to submit issues and pull requests. Contributions are welcome!






