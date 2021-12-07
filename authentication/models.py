from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False)


# Here how to solve this properly.

# Follow these steps in your migrations folder inside the project:

# Delete the _pycache_ and the 0001_initial files.
# Delete the db.sqlite3 from the root directory (be careful all your data will go away).
# on the terminal run:
# python manage.py makemigrations
# python manage.py migrate
