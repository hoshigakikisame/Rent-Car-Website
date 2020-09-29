from django.contrib import admin
from . models import Mobil, Pesanan

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ['slug']
# Register your models here.
admin.site.register(Mobil, PostAdmin)
admin.site.register(Pesanan)