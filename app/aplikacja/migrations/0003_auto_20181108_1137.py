# Generated by Django 2.1.2 on 2018-11-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0002_auto_20181108_1052'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='currentratio',
            unique_together={('company_name', 'year')},
        ),
    ]
