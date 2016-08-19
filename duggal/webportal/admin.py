from django.contrib import admin

from .models import *
# Register your models here.

class CementModelAdmin(admin.ModelAdmin):
	list_display = ["Company_Name", "Type_of_Cement", "Grade_of_Cement", "Price"]
	list_editable = ["Price"]
	class Meta:
		model = Cement

admin.site.register(Cement, CementModelAdmin)


class BrickModelAdmin(admin.ModelAdmin):
	list_display = ["Brick_or_Tiles", "Brand_of_Brick", "Grade_of_Brick", "Price"]
	list_editable = ["Price"]
	class Meta:
		model = BrickOrTile


admin.site.register(BrickOrTile, BrickModelAdmin)


class TankerModelAdmin(admin.ModelAdmin):
	list_display = ["Company_of_tanker", "Capacity_of_Tanker", "Price"]
	list_editable = ["Price"]
	class Meta:
		model = WaterTanker

admin.site.register(WaterTanker, TankerModelAdmin)

class SandModelAdmin(admin.ModelAdmin):
	list_display = ["Type_of_Sand", "Price"]
	list_editable = ["Price"]
	class Meta:
		model = Sand

admin.site.register(Sand, SandModelAdmin)

class CourseModelAdmin(admin.ModelAdmin):
	list_display = ["Place_of_course", "Size_of_course", "Amount_of_course", "Price"]
	list_editable = ["Price"]
	class Meta:
		model = CourseAggregate
admin.site.register(CourseAggregate, CourseModelAdmin)