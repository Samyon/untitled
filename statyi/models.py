from django.db import models

# Create your models here.
from django.db import models


class Statyi(models.Model):
    Name_of_statya = models.CharField(max_length=200)
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')