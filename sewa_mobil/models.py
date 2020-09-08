from django.db import models

# Create your models here.
class Mobil(models.Model):
	nama = models.CharField(max_length=100, default="nama")
	plat = models.CharField(max_length=10, default="000000")
	gambar = models.ImageField(upload_to = 'upload_img/')
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
	status = models.CharField(max_length=20, choices=status_choices, default="Available")

	def __str__(self):
		return '{}({})'.format(self.nama, self.plat)  