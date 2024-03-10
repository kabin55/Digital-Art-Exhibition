from django.db import models

# Create your models here.
class contact (models.Model):
    name = models.CharField(max_length=20, null=False)
    email =  models.EmailField(unique=True,null=False)
    # phone = models.IntegerField(unique=True,null=False)
    message = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " - " + str(self.date)
    

class UserCreationForm(models.Model):
    username  = models.CharField(max_length=30, unique=True)
    password  = models.CharField(max_length=16)
    
    def createUser(self):
        return self.username()



