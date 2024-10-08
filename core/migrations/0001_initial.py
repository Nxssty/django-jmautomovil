# Generated by Django 5.0.7 on 2024-08-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('cilindrada', models.CharField(max_length=5)),
                ('anio', models.CharField(max_length=5)),
                ('transmision', models.CharField(max_length=20)),
                ('kilometraje', models.CharField(max_length=20)),
                ('combustible', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=1000)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='autos/')),
            ],
        ),
    ]
