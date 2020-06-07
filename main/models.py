from django.db import models
from email.policy import default
class SignUpData(models.Model):
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
# Create your models here.
class SignUpOwnData(models.Model):
    ownername=models.CharField(max_length=50)
    owneremail=models.CharField(max_length=50)
    ownerpassword=models.CharField(max_length=50)
    ownercontact=models.CharField(max_length=50)
class PgDetailData(models.Model):
    owner_id=models.CharField(max_length=50)
    owner_contact=models.CharField(max_length=50)
    pg_location=models.CharField(max_length=50)
    pg_rent=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='images/')
    class Meta:
        db_table="pgtable"
        


