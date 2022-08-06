# Generated by Django 4.1 on 2022-08-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pemohon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('no_kp', models.CharField(max_length=200)),
                ('jawatan', models.CharField(max_length=200)),
                ('tarikh_lahir', models.CharField(max_length=200)),
                ('gred', models.CharField(max_length=10)),
                ('tarikh_mula_bekerja', models.DateField()),
                ('elaun', models.CharField(max_length=50)),
                ('no_tel_bimbit', models.CharField(max_length=40)),
                ('nama_pasangan', models.CharField(max_length=60)),
                ('pekerjaan_pasangan', models.CharField(max_length=200)),
                ('gaji', models.CharField(max_length=20)),
                ('alamat_tempat_kerja', models.CharField(max_length=200)),
                ('bil_anak', models.CharField(max_length=5)),
                ('alamat_rumah', models.CharField(max_length=200)),
                ('masih_menyewa', models.CharField(max_length=60)),
                ('sewa_sebulan', models.CharField(max_length=10)),
                ('detail', models.IntegerField(max_length=200)),
            ],
        ),
    ]
