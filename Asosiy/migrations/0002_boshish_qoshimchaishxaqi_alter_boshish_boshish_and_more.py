# Generated by Django 5.0.6 on 2024-06-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boshish',
            name='qoshimchaishxaqi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='boshish',
            name='boshish',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='boshish',
            name='ishxaqi',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='boshish',
            name='stavka',
            field=models.CharField(max_length=100),
        ),
    ]
