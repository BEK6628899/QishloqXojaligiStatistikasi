from django.db import models



class HududiyBolimlar(models.Model):
    ism = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=50)
    def __str__(self):
        return self.ism



class BoshIsh(models.Model):
    boshish = models.CharField(max_length=100)
    talablar = models.CharField(max_length=500)
    ishxaqi = models.CharField(max_length=100)
    qoshimchaishxaqi = models.CharField(max_length=100, null=True, blank=True)
    stavka = models.CharField(max_length=100)
    def __str__(self):
        return self.boshish



class Matbuotlar(models.Model):
    rasm = models.FileField()
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    matn = models.CharField(max_length=1000)
    def __str__(self):
        return self.sarlavha