# Generated by Django 2.1.2 on 2018-10-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181013_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Resim'),
        ),
    ]
