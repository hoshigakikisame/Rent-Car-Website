from .models import Mobil
from django import forms

class RatingForm(forms.ModelForm):
	class Meta:
		model = Mobil
		fields = ['rating']