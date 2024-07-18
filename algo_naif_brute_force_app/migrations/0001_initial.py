# Generated by Django 4.2 on 2024-07-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document1', models.FileField(upload_to='documents', verbose_name='Document 01')),
                ('document2', models.FileField(upload_to='documents', verbose_name='Document 02')),
            ],
        ),
    ]
