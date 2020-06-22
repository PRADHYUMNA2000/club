from django.db import models

class addstudent(models.Model):
    name = models.CharField(max_length = 25)
    roll_number = models.CharField(max_length = 25,unique=True)
    course = models.CharField(max_length = 20, null = True)
    email_id = models.EmailField(null = True)
    past_experiences = models.TextField(max_length=200,null=True)
   
    def __str__(self):
        return self.name