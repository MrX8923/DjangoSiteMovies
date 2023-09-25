# Generated by Django 4.2.5 on 2023-09-25 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('birthday_date', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgeRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('бесплатно', 'бесплатно'), ('базовая', 'базовая'), ('СУПЕР', 'СУПЕР')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('rating', models.FloatField()),
                ('summary', models.TextField(max_length=500)),
                ('year', models.IntegerField()),
                ('actors', models.ManyToManyField(to='catalog.actor')),
                ('age_rating', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.agerating')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.country')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director')),
                ('genre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.genre')),
                ('subscription', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.subscription')),
            ],
        ),
    ]
