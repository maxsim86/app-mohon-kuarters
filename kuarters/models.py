from django.db import models

# Create your models here.

STATUS_PILIHAN = [
    ("b", "bujang"),
    ("k", "berkahwin"),
]

TINGGAL_BERSAMA = (
    ("y", "ya"),
    ("t", "tidak"),
)


class Pemohon(models.Model):
    nama = models.CharField(max_length=200)
    no_kp = models.CharField(max_length=200)
    jawatan = models.CharField(max_length=200)
    tarikh_lahir = models.CharField(max_length=200)
    gred = models.CharField(max_length=10)
    # tarikh_mula_bekerja = models.DateField()
    elaun = models.CharField(max_length=50)
    no_tel_bimbit = models.CharField(max_length=40)
    status = models.CharField(max_length=1, choices=STATUS_PILIHAN)
    tinggal_bersama = models.CharField(max_length=1, choices=TINGGAL_BERSAMA)
    nama_pasangan = models.CharField(max_length=60)
    pekerjaan_pasangan = models.CharField(max_length=200)
    gaji = models.CharField(max_length=20)
    alamat_tempat_kerja = models.CharField(max_length=200)
    bil_anak = models.CharField(max_length=5)
    alamat_rumah = models.CharField(max_length=200)
    masih_menyewa = models.CharField(max_length=60)
    sewa_sebulan = models.CharField(max_length=10)
    detail = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.nama} {self.no_kp} {self.status}"
