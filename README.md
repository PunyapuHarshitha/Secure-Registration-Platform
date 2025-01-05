# Registration Form Project

A Django-based web application to manage user registrations with file uploads and validation. Users can submit their personal details, upload documents, and register for an institution using the provided form.

## Features

- Registration form with fields like person name, mobile number, Aadhar number, institute details, and more.
- File upload for Aadhar card front, back, and institution registration copy.
- Password confirmation and validation to prevent mismatched passwords.
- Admin interface to manage and view user registrations.
  
## Technologies Used

- Django (Python web framework)
- HTML/CSS for frontend
- JavaScript for basic form validations
- SQLite (default Django database) for storing registration data

## Prerequisites

Before setting up this project, make sure you have the following installed:

- Python 3.8 or higher
- Django 3.x or higher

## Setup Instructions

###1. Clone the repository

```bash
git clone https://github.com/yourusername/registration-form.git
cd registration-form
```

###2. Install dependencies
Create a virtual environment (recommended) and install the necessary dependencies:

```bash
python -m venv env
source env/bin/activate   # For Linux/MacOS
env\Scripts\activate      # For Windows
pip install -r requirements.txt
```
###3. Set up database
Run migrations to set up the database schema:

```bash
python manage.py migrate
```
###4. Run the development server
Now, run the development server to see the app in action:

```bash
python manage.py runserver
```
You can access the application by navigating to http://127.0.0.1:8000/ in your browser.

###5. Create a superuser
To access the Django admin interface, create a superuser by running:

```bash
python manage.py createsuperuser
```
Follow the prompts to create the superuser account.

###6. Admin interface
You can manage registrations and perform other admin tasks by visiting http://127.0.0.1:8000/admin/ and logging in with the superuser credentials.

###File Structure
```
registration-form/
├── manage.py                # Django project management commands
├── registration/             # Your Django app
│   ├── admin.py              # Admin panel configurations
│   ├── apps.py               # App configuration
│   ├── models.py             # Models (Registration Model)
│   ├── views.py              # Views for handling registration logic
│   ├── templates/            # HTML templates
│   │   └── form.html         # Registration form HTML
├── requirements.txt          # Project dependencies
└── db.sqlite3                # SQLite database (automatically created)
```
###Project Details
###Models
The Registration model contains the following fields:

person_name - Full name of the user.
person_mobile_no - Mobile number of the user.
adhar_no - Aadhar number of the user.
institute_name - Name of the institute.
institute_govt_reg_no - Government registration number of the institute.
institute_website - Website of the institute.
password - User's password.
confirm_password - Password confirmation.
adhar_front, adhar_back, institute_reg_copy - File uploads for the Aadhar card and institute registration copy.
###Views
The register view handles the registration form submission. It processes the form data, checks if passwords match, and saves the data to the database. If an error occurs, it will render an error message.

###Admin Interface
The admin interface is configured to manage Registration entries. You can view and search registrations through the Django admin panel.

###File Uploads
Ensure the Django project is set up correctly to handle media file uploads. Add the following to the settings.py file:


```bash
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
Make sure to update urls.py to serve media files during development:

```bash
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
# Your URLs here...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
##Contributing
Feel free to fork this repository and contribute. Submit a pull request with your improvements.


