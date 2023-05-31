from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=200)
    neighbors = models.ManyToManyField('self', blank=True)
    inventaire = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    

class SubStation(models.Model):
    parent = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    inventaire = models.TextField()

    def __str__(self) -> str:
        return self.name
# Create your models here.
