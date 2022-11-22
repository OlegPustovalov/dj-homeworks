from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)



 
