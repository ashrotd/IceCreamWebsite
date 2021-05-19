# Generated by Django 3.2.2 on 2021-05-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='baby_age',
        ),
        migrations.AddField(
            model_name='product',
            name='year_in_school',
            field=models.CharField(choices=[('Fr', 'Freshman'), ('Sr', 'Sophomore'), ('Jr', 'Junior'), ('sen', 'Senior'), ('Grad', 'Graduate')], default='Fr', max_length=20),
        ),
    ]
