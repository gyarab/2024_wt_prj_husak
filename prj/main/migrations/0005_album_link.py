# Generated by Django 5.1.6 on 2025-04-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_genre_instrument_member_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='link',
            field=models.TextField(blank=True, default='#'),
        ),
    ]
