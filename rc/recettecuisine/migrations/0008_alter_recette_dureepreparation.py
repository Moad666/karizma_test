# Generated by Django 4.1.7 on 2023-11-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettecuisine', '0007_alter_recette_dureepreparation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='dureePreparation',
            field=models.DateTimeField(),
        ),
    ]