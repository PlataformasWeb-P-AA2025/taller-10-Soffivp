from django.db import models



class Parroquia(models.Model):
    nombre = models.CharField(max_length=300)
    ubicacion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    def _str_(self):
        return f"Parroquia {self.nombre} - {self.ubicacion}"

class Barrio(models.Model):
    nombre = models.CharField(max_length=300)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField()
    numero_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def _str_(self):
        return f"Barrio {self.nombre}"
