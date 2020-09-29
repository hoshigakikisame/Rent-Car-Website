from django.shortcuts import render
from sewa_mobil.models import Pesanan
import datetime

def index(request):
	if request.user.is_authenticated:
		pesanan_user = Pesanan.objects.filter(nama_user = request.user.username)
		
		context = {
			'jumlah_pesanan' : pesanan_user,
		}

		return render(request, 'userIndex.html', context)
	return render(request, 'index.html')