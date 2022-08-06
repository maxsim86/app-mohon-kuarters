# Generated by Django 4.1 on 2022-08-05 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kuarters', '0002_alter_pemohon_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemohon',
            name='tinggal_bersama',
            field=models.CharField(choices=[('y', 'ya'), ('t', 'tidak')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
