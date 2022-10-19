from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Lead(models.Model):
    # source.choices = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    #     ('Other', 'Other'),
    # )
    first_name = models.CharField(max_length=20) #charfield is a string field
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=source.choices, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True) #images are stored in the media folder
    # special_files = models.FileField() #file fields are used for files like pdfs, word docs, etc.


    # def __str__(self):
    #     return self.first_name + " " + self.last_name

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one relationship with a user
    # profile_picture = models.ImageField()
    # phone_number = models.CharField(max_length=20)
    # is_organizer = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.user.email