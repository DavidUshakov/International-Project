from django.db import models

class Task(models.Model):
    fighter1 = models.CharField('name', max_length=100)
    fighter2 = models.TextField('description')



    def __str__(self):
        return self.fighter1