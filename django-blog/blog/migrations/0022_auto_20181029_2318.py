# Generated by Django 2.1.2 on 2018-10-29 20:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_auto_20181029_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='surname',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, null=True, verbose_name='Yorum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=True, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
