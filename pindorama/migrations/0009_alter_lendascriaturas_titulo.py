# Generated by Django 5.1.2 on 2024-11-06 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pindorama', '0008_lendascriaturas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendascriaturas',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
