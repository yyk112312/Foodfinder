# Generated by Django 3.1.6 on 2021-03-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='식품명')),
                ('once', models.IntegerField(default=0, verbose_name='1회 제공량')),
                ('cabor', models.IntegerField(default=0, verbose_name='탄수화물')),
                ('protein', models.IntegerField(default=0, verbose_name='단백질')),
                ('fat', models.IntegerField(default=0, verbose_name='지방')),
            ],
        ),
    ]