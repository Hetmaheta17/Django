from django.db import models

# makemigration- creat changes and store in a file
# migrate - apply the pending chamges created by makemigration

# Create your models here.
class Contect(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    Phonenumber = models.CharField(max_length=15)
    date = models.DateField()

    # it is used to show name in database table

    def __str__(self):
        return self.name
    

