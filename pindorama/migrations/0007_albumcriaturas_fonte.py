# Generated by Django 5.1.2 on 2024-11-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pindorama', '0006_albumcriaturas'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumcriaturas',
            name='fonte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
