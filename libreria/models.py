from django.db import models

class Libros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='images/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    print(imagen.name)

    def __str__(self):
        fila = f'Titulo: {self.titulo} | Descripcion: {self.descripcion}'
        return fila


