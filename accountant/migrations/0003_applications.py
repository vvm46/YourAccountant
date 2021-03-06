# Generated by Django 2.1.4 on 2018-12-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0002_auto_20181218_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('activity', models.CharField(max_length=155)),
                ('organizational_form', models.CharField(max_length=155)),
                ('tax_system', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name_plural': 'Заявки',
                'verbose_name': 'Заявка',
            },
        ),
    ]
