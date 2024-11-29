# Generated by Django 5.1.2 on 2024-11-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pindorama', '0010_criaturas_etiquetas_criaturas_modo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criaturas',
            name='modo',
            field=models.CharField(blank=True, choices=[('permanente', 'Permanente'), ('periodico', 'Periódico'), ('temporario', 'Temporário'), ('metamorfico', 'Metamórfico')], max_length=20, null=True),
        ),
    ]