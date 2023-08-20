from rest_framework import serializers
from .models import (
    Language, Category, SubCategory, Logo, SubAboutUs, AboutUs,
    SubSlider, Slider

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

class SubAboutUsSerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubAboutUs
        exclude = ("id", "belong",)

class AboutUsSerializer(serializers.ModelSerializer):
    about_us = SubAboutUsSerializer(many=True)
    class Meta:
        model = AboutUs
        fields = "__all__"

class SubSliderSerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubSlider
        exclude = ("id", "belong",)

class SliderSerializer(serializers.ModelSerializer):
    slider = SubSliderSerializer(many=True)
    class Meta:
        model = Slider
        fields = "__all__"
