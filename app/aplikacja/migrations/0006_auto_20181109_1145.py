# Generated by Django 2.1.2 on 2018-11-09 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0005_auto_20181109_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_ratio', models.DecimalField(decimal_places=5, max_digits=10)),
                ('year', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018')], default='2018', max_length=64)),
                ('cash', models.DecimalField(decimal_places=3, max_digits=10)),
                ('current_liabilities', models.DecimalField(decimal_places=3, max_digits=10)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.Company')),
            ],
        ),
        migrations.CreateModel(
            name='QuickRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quick_ratio', models.DecimalField(decimal_places=5, max_digits=10)),
                ('year', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018')], default='2018', max_length=64)),
                ('cash', models.DecimalField(decimal_places=3, max_digits=10)),
                ('marketable_securities', models.DecimalField(decimal_places=3, max_digits=10)),
                ('accounts_receivable', models.DecimalField(decimal_places=3, max_digits=10)),
                ('current_liabilities', models.DecimalField(decimal_places=3, max_digits=10)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplikacja.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='currentratio',
            name='current_ratio',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterUniqueTogether(
            name='quickratio',
            unique_together={('company_name', 'year')},
        ),
        migrations.AlterUniqueTogether(
            name='cashratio',
            unique_together={('company_name', 'year')},
        ),
    ]
