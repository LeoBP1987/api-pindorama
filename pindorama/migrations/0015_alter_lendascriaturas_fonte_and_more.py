# Generated by Django 5.1.2 on 2024-12-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pindorama', '0014_alter_etiquetascriaturas_etiqueta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendascriaturas',
            name='fonte',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='lendascriaturas',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]