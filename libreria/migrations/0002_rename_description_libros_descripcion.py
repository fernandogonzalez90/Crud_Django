# Generated by Django 4.1.7 on 2023-03-15 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libros',
            old_name='description',
            new_name='descripcion',
        ),
    ]
