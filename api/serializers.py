from rest_framework import serializers
from .models import (
    Language, Category, SubCategory, Logo, SubAboutUs, AboutUs,
    SubSlider, Slider, SubAboutCompany, AboutCompany, SubMoreAboutUs,
    MoreAboutUs, NewsImage, SubNews, News, SubService, Service,

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

class SubAboutCompanySerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubAboutCompany
        exclude = ("id", "belong",)

class AboutCompanySerializer(serializers.ModelSerializer):
    company = SubAboutCompanySerializer(many=True)
    class Meta:
        model = AboutCompany
        fields = "__all__"

# Banner Serializer
class SubMoreAboutUsSerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubMoreAboutUs
        exclude = ("id", "belong",)

class MoreAboutUsSerializer(serializers.ModelSerializer):
    more_about_us = SubMoreAboutUsSerializer(many=True)
    class Meta:
        model = MoreAboutUs
        fields = "__all__"

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = "__all__"

class SubNewsSerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubNews
        exclude = ("id", "belong",)

class NewsSerializer(serializers.ModelSerializer):
    news = SubNewsSerializer(many=True)
    news_images = NewsImageSerializer(many=True)
    class Meta:
        model = News
        fields = "__all__"

class SubServiceSerializer(serializers.ModelSerializer):
    lang = LanguageSerializer()
    class Meta:
        model = SubService
        exclude = ("id", "belong",)

class ServiceSerializer(serializers.ModelSerializer):
    service = SubServiceSerializer(many=True)
    class Meta:
        model = Service
        fields = "__all__"
