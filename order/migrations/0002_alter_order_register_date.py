# Generated by Django 3.2 on 2021-04-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜'),
        ),
    ]