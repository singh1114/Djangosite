from django.contrib import admin

from .models import Cement
# Register your models here.

class CementModelAdmin(admin.ModelAdmin):
	list_display = ["company_name", "Type", "Grade", "price"]
	list_editable = ["price"]
	class Meta:
		model = Cement

admin.site.register(Cement, CementModelAdmin)
