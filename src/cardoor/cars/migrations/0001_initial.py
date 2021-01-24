# Generated by Django 3.1.2 on 2020-11-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('availability', models.BooleanField()),
                ('rent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]