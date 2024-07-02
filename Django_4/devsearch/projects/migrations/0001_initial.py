# Generated by Django 5.0.6 on 2024-07-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', upload_to='projects/%Y/%m/%d/')),
                ('demo_link', models.CharField(blank=True, max_length=500)),
                ('source_link', models.CharField(blank=True, max_length=500)),
                ('vote_total', models.IntegerField(default=0)),
                ('vote_ratio', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='projects.tag')),
            ],
        ),
    ]
