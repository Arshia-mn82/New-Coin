from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    total_saving = models.FloatField()
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class saving_plan(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.FloatField()
    current_amount = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

