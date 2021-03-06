# Generated by Django 3.1 on 2022-04-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.CharField(default='default', max_length=200, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='house',
            field=models.CharField(default='default', max_length=200, verbose_name='Номер дома'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='inn',
            field=models.CharField(default='default', max_length=200, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='office',
            field=models.CharField(default='default', max_length=200, verbose_name='Номер помещения'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='street',
            field=models.CharField(default='default', max_length=200, verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='zip_code',
            field=models.CharField(default='default', max_length=200, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='fathers_name',
            field=models.CharField(default='default', max_length=200, verbose_name='Отчество'),
        ),
    ]
