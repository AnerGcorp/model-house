from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Category, Logo, AboutUs, Slider, AboutCompany, MoreAboutUs, News,
    Service, Gallery
)

from .serializers import (
    CategorySerializer, LogoSerializer, AboutUsSerializer,
    SliderSerializer, AboutCompanySerializer, MoreAboutUsSerializer,
    NewsSerializer, ServiceSerializer, GallerySerializer
)

from .utils import JSONListFormatter

# Create your views here.

class CategoryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        try:
            data = JSONListFormatter("category", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class CategoryDetailApiView(APIView):

    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id, *args, **kwargs):
        '''
            Retrieves the Post with given category_id
        '''
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"response": "Post with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CategorySerializer(category_instance)
        try:
            data = JSONListFormatter("category", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class LogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Logo.objects.all().order_by("id")
    serializer_class = LogoSerializer

class AboutUsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.objects.all().order_by('-id')
        serializer = AboutUsSerializer(about_us, many=True)
        try:
            data = JSONListFormatter("about_us", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class AboutUsDetailApiView(APIView):

    def get_object(self, abu_id):
        try:
            return AboutUs.objects.get(id=abu_id)
        except AboutUs.DoesNotExist:
            return None

    def get(self, request, abu_id, *args, **kwargs):
        '''
            Retrieves the object with given abu_id
        '''
        abu_instance = self.get_object(abu_id)
        if not abu_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AboutUsSerializer(abu_instance)
        try:
            data = JSONListFormatter("about_us", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class SliderListApiView(APIView):

    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.all().order_by('-id')
        serializer = SliderSerializer(sliders, many=True)
        try:
            data = JSONListFormatter("slider", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class SliderDetailApiView(APIView):

    def get_object(self, slider_id):
        try:
            return Slider.objects.get(id=slider_id)
        except Slider.DoesNotExist:
            return None

    def get(self, request, slider_id, *args, **kwargs):
        '''
            Retrieves the Post with given slider_id
        '''
        slider_instance = self.get_object(slider_id)
        if not slider_instance:
            return Response(
                {"response": "Post with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = SliderSerializer(slider_instance)
        try:
            data = JSONListFormatter("slider", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class AboutCompanyListApiView(APIView):

    def get(self, request, *args, **kwargs):
        company = AboutCompany.objects.all().order_by('-id')
        serializer = AboutCompanySerializer(company, many=True)
        try:
            data = JSONListFormatter("company", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class AboutCompanyDetailApiView(APIView):

    def get_object(self, com_id):
        try:
            return AboutCompany.objects.get(id=com_id)
        except AboutCompany.DoesNotExist:
            return None

    def get(self, request, com_id, *args, **kwargs):
        '''
            Retrieves the object with given com_id
        '''
        com_instance = self.get_object(com_id)
        if not com_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = AboutCompanySerializer(com_instance)
        try:
            data = JSONListFormatter("company", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class MoreAboutUsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        more_about_us = MoreAboutUs.objects.all().order_by('-id')
        serializer = MoreAboutUsSerializer(more_about_us, many=True)
        try:
            data = JSONListFormatter("more_about_us", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class MoreAboutUsDetailApiView(APIView):

    def get_object(self, mau_id):
        try:
            return MoreAboutUs.objects.get(id=mau_id)
        except MoreAboutUs.DoesNotExist:
            return None

    def get(self, request, mau_id, *args, **kwargs):
        '''
            Retrieves the object with given mau_id
        '''
        mau_instance = self.get_object(mau_id)
        if not mau_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MoreAboutUsSerializer(mau_instance)
        try:
            data = JSONListFormatter("more_about_us", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class NewsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-id')
        serializer = NewsSerializer(news, many=True)
        try:
            data = JSONListFormatter("news", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class NewsDetailApiView(APIView):

    def get_object(self, news_id):
        try:
            return News.objects.get(id=news_id)
        except News.DoesNotExist:
            return None

    def get(self, request, news_id, *args, **kwargs):
        '''
            Retrieves the object with given news_id
        '''
        news_instance = self.get_object(news_id)
        if not news_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = NewsSerializer(news_instance)
        try:
            data = JSONListFormatter("news", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class ServiceListApiView(APIView):

    def get(self, request, *args, **kwargs):
        service = Service.objects.all().order_by('-id')
        serializer = ServiceSerializer(service, many=True)
        try:
            data = JSONListFormatter("service", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class ServiceDetailApiView(APIView):

    def get_object(self, ser_id):
        try:
            return Service.objects.get(id=ser_id)
        except Service.DoesNotExist:
            return None

    def get(self, request, ser_id, *args, **kwargs):
        '''
            Retrieves the object with given ser_id
        '''
        ser_instance = self.get_object(ser_id)
        if not ser_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ServiceSerializer(ser_instance)
        try:
            data = JSONListFormatter("service", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)

class GalleryListApiView(APIView):

    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.all().order_by('-id')
        serializer = GallerySerializer(gallery, many=True)
        print(serializer.data)
        try:
            data = JSONListFormatter("gallery", serializer.data)
        except:
            data = []

        return Response(data, status=status.HTTP_200_OK)

class GalleryDetailApiView(APIView):

    def get_object(self, gallery_id):
        try:
            return Gallery.objects.get(id=gallery_id)
        except Gallery.DoesNotExist:
            return None

    def get(self, request, gallery_id, *args, **kwargs):
        '''
            Retrieves the object with given gallery_id
        '''
        gallery_instance = self.get_object(gallery_id)
        if not gallery_instance:
            return Response(
                {"response": "Object with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = GallerySerializer(gallery_instance)
        try:
            data = JSONListFormatter("gallery", name_obj=serializer.data)
        except:
            data = []
        return Response(data, status=status.HTTP_200_OK)
