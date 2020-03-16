from django.db import models

# Create your models here.

class User(models.Model):
  id = models.IntegerField(primary_key=True)
  #  FB has a max_length of 50 so I'm just copying that
  username = models.CharField(max_length=50, unique=True) 
  # highly unlikely we'll need higher than 32 bit int
  login_count = models.IntegerField(default=0)
  project_count = models.IntegerField(default=0)
  # while it's entirely possible a user never makes a log in
  # it appears the default is a account creation time, else I'd allow it to be blank
  last_login = models.DateTimeField(auto_now_add=True)
