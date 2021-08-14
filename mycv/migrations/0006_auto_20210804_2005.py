# Generated by Django 3.1.2 on 2021-08-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0005_auto_20210804_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='description',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]