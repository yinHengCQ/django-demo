from django.db import models
from datetime import date

# Create your models here.
class BoolInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateField()

    def __str__(self):
        return self.title.encode('utf-8')

class HeroInfo(models.Model):
    name=models.CharField(max_length=10)
    content=models.CharField(max_length=100)
    gender=models.BooleanField(default=True)
    book=models.ForeignKey(BoolInfo)

    def __str__(self):
        return self.name.encode('utf-8')