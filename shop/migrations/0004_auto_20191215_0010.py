# Generated by Django 2.2.7 on 2019-12-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191214_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('DRESSES', 'Dresses'), ('SWEATERS', 'Sweaters'), ('JACKETS', 'Jackets'), ('BLOUSES', 'Blouses'), ('SHORTS', 'Shorts'), ('SKIRTS', 'Skirts'), ('PANTS', 'Pants')], max_length=8),
        ),
    ]
