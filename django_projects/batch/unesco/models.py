from django.db import models
class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    area_hectares = models.DecimalField(decimal_places=10, max_digits=100,null=True)

    def __str__(self) :
        return self.name

# Create your models here.
