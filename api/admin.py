from django.contrib import admin
from .models import *


# Register your models here.

#admin.site.register(Category)
# admin.site.register(State),
# admin.site.register(Zone),
# admin.site.register(PackagesType),
# admin.site.register(Package),
# admin.site.register(Package_Itinerary_items)

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = [
            'Category_id',
            'Category_Name',
            'Category_Description',
            'Category_Image',
            'Category_Status',
        ]
    
@admin.register(State)
class Stateadmin(admin.ModelAdmin):
    list_display = [
            'State_id',
            'State_Name',
            'State_Description',
            'State_Image',
        ]
    
@admin.register(Zone)
class Zoneadmin(admin.ModelAdmin):
    list_display = [
            'Zone_id',
            'Zone_Name',
            'Zone_Description',
            'Zone_Image',
        ]
    
@admin.register(PackagesType)
class PackagesTypeadmin(admin.ModelAdmin):
    list_display = [
            'PackagesType_Name',
            'PackagesType_Description',
            'PackagesType_Image', 
        ]
    
@admin.register(Package)
class Packageadmin(admin.ModelAdmin):
    list_display = [
            'Package_id',
            'Package_Name',
            'Package_Description',
            'Package_BannerImage',
            'package_Duration',
            'package_Inclusion',
            'package_Category_id',
            'Category_id',
            'State_id',
            'Zone_id',
        ]
    
@admin.register(Package_Itinerary_items)
class Itinerary_itemadmin(admin.ModelAdmin):
    list_display = [
            'Itinerary_items_id',
            'Itinerary_items_title',
            'Itinerary_items_Day',
            'Itinerary_items_Image',
            'Itinerary_items_Description',
        ]