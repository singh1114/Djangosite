from django.contrib import admin

from .models import *
# Register your models here.

class CementModelAdmin(admin.ModelAdmin):
	list_display = ["Company_Name", "Type_of_Cement", "Grade_of_Cement", "Price_of_Cement"]
	list_editable = ["Price_of_Cement"]
	class Meta:
		model = Cement

admin.site.register(Cement, CementModelAdmin)


class BrickModelAdmin(admin.ModelAdmin):
	list_display = ["Brick_or_Tiles", "Brand_of_Brick", "Grade_of_Brick", "Price_of_Brick"]
	list_editable = ["Price_of_Brick"]
	class Meta:
		model = BrickOrTile


admin.site.register(BrickOrTile, BrickModelAdmin)


class TankerModelAdmin(admin.ModelAdmin):
	list_display = ["Company_of_tanker", "Capacity_of_Tanker", "Price_of_Tanker"]
	list_editable = ["Price_of_Tanker"]
	class Meta:
		model = WaterTanker

admin.site.register(WaterTanker, TankerModelAdmin)

class SandModelAdmin(admin.ModelAdmin):
	list_display = ["Type_of_Sand", "Price_of_Sand"]
	list_editable = ["Price_of_Sand"]
	class Meta:
		model = Sand

admin.site.register(Sand, SandModelAdmin)

class CourseModelAdmin(admin.ModelAdmin):
	list_display = ["Place_of_course", "Size_of_course", "Amount_of_course", "Price_of_Course"]
	list_editable = ["Price_of_Course"]
	class Meta:
		model = CourseAggregate
admin.site.register(CourseAggregate, CourseModelAdmin)