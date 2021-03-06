from django.db import models

# Create your models here.
from beers.utils import image_upload_location
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_CHOICES = (
        (1, 'Yellow'),
        (2, 'Black'),
        (3, 'Amber'),
        (4, 'Brown'),
    )

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    is_filtered = models.BooleanField('Is filtered?', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=1)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='beer_ids')

    class Meta:  # Añade informacion y configuracion a la clase
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beer_ids = models.ManyToManyField(Beer, blank=True, related_name='special_ingredient_ids')

    class Meta:
        verbose_name = 'Special ingredient'
        verbose_name_plural = 'Special ingredients'
        ordering = ['name']

    def __str__(self):
        return self.name
