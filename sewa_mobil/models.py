from django.db import models
from django.utils.text import slugify
import datetime

# Create your models here.
class Mobil(models.Model):
	nama = models.CharField(max_length=100, default="nama")
	plat = models.CharField(max_length=10, default="000000")
	gambar = models.ImageField(upload_to = 'upload_img/')
	gambar2 = models.ImageField(upload_to = 'upload_img/')
	gambar3 = models.ImageField(upload_to = 'upload_img/')
	gambar4 = models.ImageField(upload_to = 'upload_img/')
	kategori = [
    	('Covertible', 'Covertible'),
    	('Coupe', 'Coupe'),
    	('Sedan', 'Sedan'),
    	('Hatchback', 'Hatchback'),
    	('SUV', 'SUV'),
    	('MPV', 'MPV'),
	]
	tipe = models.CharField(max_length=20, choices=kategori, default="MPV")
	harga = models.IntegerField(default=100000)
	deskripsi = models.TextField(default="deskripsi")
	status_choices = [
		('Available', 'Available'),
		('Not Available', 'Not Available'),
	]

	transmisi = models.CharField(max_length=10, default="Manual", choices=[('Auto', 'Auto'),('Manual', 'Manual')])
	status = models.CharField(max_length=20, choices=status_choices, default="Available")
	slug = models.SlugField(blank=True, editable=False)

	def save(self, *args, **kwargs):
		super(Mobil, self).save(*args, **kwargs)
		self.slug = slugify(self.plat)
		super().save()

	def __str__(self):
		return '{}({})'.format(self.nama, self.plat)


class Pesanan(models.Model):
	nama = models.CharField(max_length=100, default="nama")
	plat = models.CharField(max_length=10, default="000000")
	gambar = models.ImageField(upload_to = 'upload_img/')
	harga = models.IntegerField(default=100000)
	nama_user = models.CharField(max_length=50)
	lama = models.IntegerField()
	tgl_pesan = models.DateField()
	tgl_kembali = models.DateField()

	def denda(self):
		if self.tgl_kembali > datetime.datetime.now().date():
			self.harga += self.harga * 0.3

	def save(self, *args, **kwargs):
		# self.tgl_kembali = self.tgl_pesan + datetime.timedelta(self.lama) 
		# self.harga = self.harga * self.lama
		super(Pesanan, self).save(*args, **kwargs)

	def __str__(self):
		return '{}({}) - {}'.format(self.nama, self.plat, self.nama_user)

