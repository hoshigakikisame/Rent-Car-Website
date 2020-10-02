from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('detail/<str:plat>', views.detail, name='detail'),
	path('pesan/<str:plat>', views.pesan, name='pesan'),
	path('batalPesan/<str:plat>', views.batalPesan, name='batalPesan')
]