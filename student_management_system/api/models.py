from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    username      = models.CharField(max_length=50, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username