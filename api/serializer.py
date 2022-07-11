
from rest_framework import serializers

from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'Category_id',
            'Category_Name',
            'Category_Description',
            # 'Category_Image',
            'Category_Status',
        ]

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'State_id',
            'State_Name',
            'State_Description',
            # 'State_Image',
        ]

class ZoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = [
            'Zone_id',
            'Zone_Name',
            'Zone_Description',
            # 'Zone_Image',
        ]

class PackagesTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackagesType
        fields = [
            'PackagesType_Name',
            'PackagesType_Description',
            # 'PackagesType_Image', 
        ]
    

class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'Package_id',
            'Package_Name',
            'Package_Description',
            # 'Package_BannerImage',
            'package_Duration',
            'package_Inclusion',
            'package_Category_id',
            'Category_id',
            'State_id',
            'Zone_id',
        ]
        
class Itinerary_itemsSerializer(serializers.Serializer):
    class Meta:
        model = Package_Itinerary_items
        fields = [
            'Itinerary_items_id',
            'Itinerary_items_title',
            'Itinerary_items_Day',
            # 'Itinerary_items_Image',
            'Itinerary_items_Description',
        ]