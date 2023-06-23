from django.db import models

# Create your models here.

class UserDetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    @staticmethod
    def get_user_email(email=email):
        try:
            return UserDetails.objects.get(email=email)
        except:
            return False
    
