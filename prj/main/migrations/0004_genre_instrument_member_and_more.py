# Generated by Django 5.1.7 on 2025-04-01 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_album_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('birth_year', models.IntegerField()),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='member_images/default.png', null=True, upload_to='member_images/')),
            ],
        ),
        migrations.RenameField(
            model_name='band',
            old_name='activeYears',
            new_name='endYear',
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, default='album_images/default.png', null=True, upload_to='album_images/'),
        ),
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.ImageField(blank=True, default='band_images/default.png', null=True, upload_to='band_images/'),
        ),
        migrations.AddField(
            model_name='band',
            name='startYear',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='band',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='BandGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.band')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.genre')),
            ],
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startYear', models.IntegerField()),
                ('endYear', models.IntegerField(blank=True, null=True)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.band')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.instrument')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.member')),
            ],
        ),
    ]
