# Generated by Django 5.1.1 on 2024-10-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('ano_publicacao', models.IntegerField()),
            ],
        ),
    ]