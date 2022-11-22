import csv
import slug
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        slug_ = ''
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            slug_ = slug.slug(phone['name'])
#Создаем z_phone экземпляр класса Phone
            z_phone = Phone(name=phone['name'],price=phone['price'],image=phone['image'],release_date=phone['release_date'],
                            lte_exists=phone['lte_exists'],slug=slug_,)
#Для записи в БД используем метод save            
            z_phone.save()