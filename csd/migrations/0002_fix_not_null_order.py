# Generated by Django 4.1 on 2022-08-11 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csd', '0001_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='csd.service'),
        ),
    ]
