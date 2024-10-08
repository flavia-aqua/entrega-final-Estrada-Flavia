# Generated by Django 5.0.7 on 2024-08-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=60)),
                ('tema', models.CharField(choices=[('1', 'GTM'), ('2', 'GA4'), ('3', 'BQ')], default='1', max_length=1)),
                ('cuerpo', models.TextField(blank=True, null=True)),
                ('autor', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nivel', models.CharField(choices=[('1', 'Básico'), ('2', 'Intermedio'), ('3', 'Avanzado')], default='1', max_length=1)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tema', models.CharField(choices=[('1', 'GTM'), ('2', 'GA4'), ('3', 'BQ')], default='1', max_length=1)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
    ]
