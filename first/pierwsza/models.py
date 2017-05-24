from django.db import models

# Create your models here.
class Muzyk(models. Model):
	imie = models.CharField(max_length=50)
	nazwisko = models.CharField(max_length=50)
	pseudonim = models.CharField(max_length=100)
	
class Album(models.Model):
	artysta = models.ForeignKey(Muzyk)
	tytul = models.CharField(max_length=100)
	data_wydania=models.DateField()
	liczba_gwiazdek = models.IntegerField()
