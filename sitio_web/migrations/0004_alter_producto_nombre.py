# Generated by Django 4.0.4 on 2024-04-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio_web', '0003_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]