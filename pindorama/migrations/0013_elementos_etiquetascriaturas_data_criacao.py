# Generated by Django 5.1.2 on 2024-11-18 17:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pindorama', '0012_remove_criaturas_etiquetas_etiquetascriaturas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elemento', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=20)),
                ('descricao', models.TextField()),
                ('foto_elemento', models.ImageField(upload_to='foto_elemento/%Y/%m/%d')),
                ('data_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='etiquetascriaturas',
            name='data_criacao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
