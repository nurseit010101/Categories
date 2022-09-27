from django.db import models

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=30, verbose_name='Название')
    def __str__(self):
        return self.title

class Meals(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(verbose_name='Название')
    image = models.ImageField(upload_to='main', verbose_name='Image')
    Categry = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE)