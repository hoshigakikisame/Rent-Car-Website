from django.shortcuts import render

def index(request):
	if request.user.is_authenticated:
		return render(request, 'userIndex.html')
	return render(request, 'index.html')