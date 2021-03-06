# Generated by Django 4.0.2 on 2022-02-04 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rate', models.FloatField(default=0)),
                ('fk_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rating', to='core.book')),
            ],
        ),
    ]
