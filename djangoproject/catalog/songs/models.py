from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=100,verbose_name='Şarkı İsmi')
    description = models.TextField(verbose_name='Şarkı Açıklaması')
    image = models.CharField(max_length=50,verbose_name='Şarkı Resmi')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Eklediği Tarih')
    isPublished = models.BooleanField(default=True,verbose_name='Şarkı Yayındamı')

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image