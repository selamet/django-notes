# Generated by Django 2.1.2 on 2018-10-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181019_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='isim')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Soyisim')),
                ('email', models.EmailField(help_text='Bu alanın girilmesi gerek', max_length=254, null=True, verbose_name='Email')),
                ('content', models.TextField(help_text='Fikrinizi Yazınız', max_length=1000, null=True, verbose_name='Yorum')),
                ('blog', models.ForeignKey(null=True, on_delete=True, to='blog.Blog')),
            ],
        ),
    ]
