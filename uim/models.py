from django.db import models

class SejarahKampus(models.Model):
    nama = models.CharField(max_length=100)
    tanggal_berdiri = models.DateField()

    def __str__(self):
        return self.nama 

class VisiMisi(models.Model):
    visi = models.TextField()
    misi = models.TextField()
    sejarahkampus_id = models.ForeignKey(SejarahKampus, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.visi

