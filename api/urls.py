from django.urls import include, path
from rest_framework import routers
from .views import (
    CategoryListApiView, CategoryDetailApiView, LogoViewSet, AboutUsListApiView,
    AboutUsDetailApiView, SliderListApiView, SliderDetailApiView,
    AboutCompanyListApiView, AboutCompanyDetailApiView, MoreAboutUsListApiView,
    MoreAboutUsDetailApiView, NewsListApiView, NewsDetailApiView,
    ServiceListApiView, ServiceDetailApiView, GalleryListApiView,
    GalleryDetailApiView,    ContactsListApiView, ContactsDetailApiView
)

app_name = 'modeller'

router = routers.DefaultRouter()
router.register(r"logo", LogoViewSet, basename="logo")

urlpatterns = [
    path(r'', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('category/', CategoryListApiView.as_view(), name="category"),
    path('category/<int:category_id>', CategoryDetailApiView.as_view(), name="category_detail"),
    path('about-us/', AboutUsListApiView.as_view(), name="abu"),
    path('about-us/<int:abu_id>', AboutUsDetailApiView.as_view(), name="abu_detail"),
    path('slider/', SliderListApiView.as_view(), name="slider"),
    path('slider/<int:slider_id>', SliderDetailApiView.as_view(), name="slider_detail"),
    path('company/', AboutCompanyListApiView.as_view(), name="com"),
    path('company/<int:com_id>', AboutCompanyDetailApiView.as_view(), name="com_detail"),
    # banners
    path('banners/', MoreAboutUsListApiView.as_view(), name="banner"),
    path('banners/<int:mau_id>', MoreAboutUsDetailApiView.as_view(), name="banner_detail"),
    path('news/', NewsListApiView.as_view(), name="news"),
    path("news/<int:news_id>", NewsDetailApiView.as_view(), name="news_detail"),
    # services
    path('services/', ServiceListApiView.as_view(), name="service"),
    path('services/<int:ser_id>', ServiceDetailApiView.as_view(), name="service_detail"),
    path('gallery/', GalleryListApiView.as_view(), name="gallery"),
    path("gallery/<int:gallery_id>", GalleryDetailApiView.as_view(), name="gallery_detail"),
    path('contacts/', ContactsListApiView.as_view(), name="cont"),
    path('contacts/<int:cont_id>', ContactsDetailApiView.as_view(), name="cont_detail"),

]
