from django.shortcuts import render, redirect
from .models import Mobil, Pesanan
import datetime
from rental_mobil.views import index as home

# Create your views here.
def index(request):
	mobil_all = Mobil.objects.all()

	context = {
		'mobil_all':mobil_all,
		'columns':[1,2,3],
	}

	return render(request, 'sewa_mobil/car.html', context)

def detail(request, plat):
	mobil_dipilih = Mobil.objects.get(slug=plat)

	context = {
		'nama' : mobil_dipilih.nama,
		'plat' : mobil_dipilih.plat,
		'gambar' : mobil_dipilih.gambar.url,
		'gambar2' : mobil_dipilih.gambar2.url,
		'gambar3' : mobil_dipilih.gambar3.url,
		'gambar4' : mobil_dipilih.gambar4.url,	
		'harga' : mobil_dipilih.harga,
		'deskripsi': mobil_dipilih.deskripsi,
		'tipe' : mobil_dipilih.tipe,
		'transmisi': mobil_dipilih.transmisi,
		'status': mobil_dipilih.status,
	}

	return render(request, 'sewa_mobil/product-detail.html', context)

def pesan(request, plat):
	mobil_dipilih = Mobil.objects.get(slug=plat)

	context = {
		'nama' : mobil_dipilih.nama,
		'plat' : mobil_dipilih.plat,
		'gambar' : mobil_dipilih.gambar.url,
		'harga' : mobil_dipilih.harga,
	}

	print(datetime.date.today())
	print('cs')

	if request.method ==  "POST":

		Pesanan.objects.create(
			nama_user = request.user.username,
			nama = mobil_dipilih.nama,
			plat = mobil_dipilih.plat,
			harga = mobil_dipilih.harga,
			gambar = mobil_dipilih.gambar.url,
			tgl_pesan = datetime.datetime.now(),
			lama = int(request.POST['lama']),
			tgl_kembali = datetime.datetime.now() + datetime.timedelta(days=int(request.POST['lama'])),
			denda = (mobil_dipilih.harga * int(request.POST['lama']) * 0.1),
			total_bayar = mobil_dipilih.harga * int(request.POST['lama']),

		) 

		return redirect("http://localhost:8000")

	return render(request, 'sewa_mobil/form_pemesanan.html', context)

def batalPesan(request, plat):
	pesanan = Pesanan.objects.get(plat=plat)
	pesanan.delete()

	return redirect(home)