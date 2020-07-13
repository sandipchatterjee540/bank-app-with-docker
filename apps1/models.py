from django.db import models

# Create your models here.
class CreateAcount(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile=models.CharField(max_length=12)
    money=models.IntegerField()
    sax=models.CharField(max_length=10)
    date=models.CharField(max_length=60)

    def __str__(self):
        return self.username

class Balance(models.Model):
    old_balance=models.IntegerField()
    new_balance=models.IntegerField()
    username=models.ForeignKey(CreateAcount, on_delete=models.CASCADE)
    date=models.CharField(max_length=500)

    def __str__(self):
        return self.username.username
    
