# Generated by Django 3.1.6 on 2021-03-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userslog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.IntegerField(max_length=10, null=True, verbose_name='키'),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.IntegerField(max_length=10, null=True, verbose_name='몸무게'),
        ),
    ]