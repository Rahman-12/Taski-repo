from django.db import models

# Create your models here.
class Customer(models.Model): 
    id = models.AutoField(primary_key=True) # incremental, integer 
    username = models.CharField(max_length=25, null=True)
    password = models.CharField(max_length=255, null=True)
    phone_number= models.CharField(max_length=255, null=True)
    e_mail=models.CharField(max_length=255, null=True)
    



class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    customer_id = models.ForeignKey("Customer", on_delete=models.CASCADE)























































'''
    CREATE TABLE user ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT
        username VARCHAR(255) NOT NULL
        password VARCHAR(255) NOT NULL
    )
'''
