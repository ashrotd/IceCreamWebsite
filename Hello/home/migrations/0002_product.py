# Generated by Django 3.2.2 on 2021-05-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('baby_age', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=122)),
                ('most_popular', models.BooleanField(default=False)),
                ('hot_selling', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Hello/images')),
            ],
        ),
    ]