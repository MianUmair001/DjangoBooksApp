# Generated by Django 4.2.4 on 2023-09-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]