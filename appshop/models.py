from django.db import models

# Create your models here.


class Marka(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
class Brend(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class AKP(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Car(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    akp = models.ForeignKey(AKP, on_delete=models.CASCADE)
    engine = models.FloatField("Engine", default=0.0)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.FloatField("Price", default=0.0)
    image = models.ImageField(upload_to='images', default='images/no_image.jpg')