from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rental_mobil import views as home

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return redirect(home.index)
	elif not request.user.is_authenticated:
		return redirect('user:signin')
	return render(request, 'user/index.html')

def signin(request):
	context = {
		'title' : 'Login | Rental Mobil',
	}
	if request.method == "POST":
		username_signin = request.POST['username']
		password_signin = request.POST['password']
		
		user = authenticate(username=username_signin, password=password_signin)

		if user is not None:
			print("youre logged in")
			login(request, user)
			return redirect(home.index)

		else:
			context['message'] = 'Username or Password wrong!';
			print("you have no account")
			return render(request, 'user/signin.html', context)


	return render(request, 'user/signin.html', context)

def signup(request):
	context = {
		'title' : 'Sign Up',
	}

	if request.method == "POST":

		username_signup = request.POST['username']
		password_signup = request.POST['password']
		email_signup    = request.POST['email']

		if User.objects.filter(email=email_signup).exists():
			print('this email already used for another account')
			context['message'] = 'This email already used for another account!'
		elif User.objects.filter(username=username_signup).exists():
			print('username already exists')
			context['message'] = "Username already exists!"
		else:
			print('account successfully created')
			User.objects.create_user(email=email_signup, username=username_signup, password=password_signup)
			user = authenticate(username=username_signup, password=password_signup)
			login(request, user)
			return redirect(home.index)



	return render(request, 'user/signup.html', context)

def signout(request):
	logout(request)
	return redirect(home.index)