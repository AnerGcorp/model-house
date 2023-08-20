from rest_framework import serializers
from .models import (
    Language, Category, SubCategory, Logo
)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'long', )

class SubCategorySerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubCategory
        exclude = ("id", "belong",)

class CategorySerializer(serializers.ModelSerializer):
    category = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"

