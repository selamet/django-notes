# Generated by Django 2.1.2 on 2018-10-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181014_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='unique_id',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
    ]
