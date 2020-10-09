from django.shortcuts import render
from sewa_mobil.models import Pesanan
from sewa_mobil.models import Mobil
from django.contrib.auth.models import User
import datetime

def index(request):
	if request.user.is_authenticated:
		pesanan_user = Pesanan.objects.filter(nama_user = request.user.username)
		seluruh_mobil = Mobil.objects.all()
		
		context = {
			'seluruh_mobil': seluruh_mobil,
			'jumlah_pesanan' : pesanan_user,
			'hari_ini':datetime.date.today(),
		}

		if request.method == "POST":
			mobil_terkait = Mobil.objects.get(plat = request.POST['plat_mobil'])
			mobil_terkait.rating = (mobil_terkait.rating + int(request.POST['rating'])) / 2
			mobil_terkait.ratinged_by.add(User.objects.get(username=request.user.username))
			mobil_terkait.save()

		return render(request, 'userIndex.html', context)
	return render(request, 'index.html')