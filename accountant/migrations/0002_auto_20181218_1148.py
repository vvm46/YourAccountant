# Generated by Django 2.1.4 on 2018-12-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=555)),
                ('subtitle', models.TextField(default=None)),
                ('additionally', models.TextField(default=None)),
                ('enabled', models.BooleanField(default=False, help_text='Дозволити відображати на сайті')),
            ],
            options={
                'verbose_name': 'Комплексне обслуговування',
                'verbose_name_plural': 'Комплексне обслуговування',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_work', models.CharField(default=None, max_length=255)),
                ('street', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phones', models.CharField(default=None, max_length=255)),
                ('company_footer', models.CharField(default=None, max_length=455)),
                ('map', models.URLField()),
            ],
            options={
                'verbose_name': 'Контакти',
                'verbose_name_plural': 'Контакти',
            },
        ),
        migrations.AddField(
            model_name='aboutus',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Дозволити відображати на сайті'),
        ),
        migrations.AddField(
            model_name='advantages',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Дозволити відображати на сайті'),
        ),
        migrations.AddField(
            model_name='howwework',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Дозволити відображати на сайті'),
        ),
        migrations.AddField(
            model_name='services',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Дозволити відображати на сайті'),
        ),
        migrations.AddField(
            model_name='title',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Дозволити відображати на сайті'),
        ),
    ]
