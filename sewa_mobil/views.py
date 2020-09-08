from django.shortcuts import render
from .models import Mobil

# Create your views here.
def index(request):
	mobil_all = Mobil.objects.all()

	context = {
		'mobil_all':mobil_all,
		'columns':[1,2,3],
	}

	return render(request, 'sewa_mobil/car.html', context)