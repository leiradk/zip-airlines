from django.db import models

class Airplane(models.Model):
    airplane_id = models.IntegerField()
    passenger = models.IntegerField()
    
    def __str__(self):
        return self.airplane_id