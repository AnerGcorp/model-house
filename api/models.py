from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

# Create your models here.
class Language(models.Model):
    code = models.CharField(max_length=3)
    long = models.CharField(max_length=50)

    def __str__(self):
        return self.long

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    icon = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(['png', 'jpg', 'svg', "jpeg", "webp"])],
        blank=True, null=True)
    link = models.CharField(max_length=2048)

class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "SubCategories"
        verbose_name = "SubCategory"

    name = models.CharField(max_length=255)
    belong = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang')

    def __str__(self):
        return self.name

class Logo(models.Model):
    icon = models.FileField(
        upload_to="images/",
        validators=[FileExtensionValidator(['png', 'jpg', 'svg', "jpeg", "webp"])],
        blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    class Meta:
        verbose_name_plural = "About Us"

    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    web_image = models.ImageField(upload_to="images/map")
    mobile_image = models.ImageField(upload_to="images/map")
    # can be the location of map, lantitute and longtitude
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email

class SubAboutUs(models.Model):
    class Meta:
        verbose_name_plural = "SubAbout Us"
    address = models.CharField(max_length=2000)
    belong = models.ForeignKey('AboutUs', on_delete=models.CASCADE, related_name='about_us')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_abu')


class Slider(models.Model):
    # One banner for slider
    web_image = models.ImageField(upload_to='images/slider')
    mobile_image = models.ImageField(upload_to='images/slider')
    # there are limited space in frontend
    link = models.CharField(max_length=2048)
    is_active = models.BooleanField(default=False)

class SubSlider(models.Model):
    title = models.CharField(max_length=500)
    button = models.CharField(max_length=100)
    belong = models.ForeignKey('Slider', on_delete=models.CASCADE, related_name='slider')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_sld')

class AboutCompany(models.Model):
    class Meta:
        verbose_name_plural = "About Company"
    logo = models.FileField(
        upload_to="images/logo",
        validators=[FileExtensionValidator(['png', 'jpg', 'svg', "jpeg", "webp"])],
        blank=True, null=True)

class SubAboutCompany(models.Model):
    class Meta:
        verbose_name_plural = "Sub About Company"

    name = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField()
    belong = models.ForeignKey('AboutCompany', on_delete=models.CASCADE, related_name='company')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_com')

# Banner Section
class MoreAboutUs(models.Model):
    class Meta:
        verbose_name_plural = "Banners"
        verbose_name = "Banner"

    # video or image link
    link = models.CharField(max_length=2048, blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="images/works", blank=False, null=False)
    is_active = models.BooleanField(default=False)

class SubMoreAboutUs(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    button = models.CharField(max_length=2048, blank=True, null=True)
    belong = models.ForeignKey('MoreAboutUs', on_delete=models.CASCADE, related_name='more_about_us')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_mau')

class News(models.Model):
    class Meta:
        verbose_name_plural = "News"

    link = models.CharField(max_length=2048, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, blank=True)


class SubNews(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    button = models.CharField(max_length=100, blank=True, null=True)
    belong = models.ForeignKey('News', on_delete=models.CASCADE, related_name='news')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_news')


    class Meta:
        verbose_name_plural = "SubNews"

class NewsImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images/news")
    belongs_to = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="news_images")
# Services
class Service(models.Model):
    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"

    # service page
    link = models.CharField(max_length=2048, blank=True, null=True)
    image = models.ImageField(
        upload_to="images/services", blank=False, null=False)
    is_active = models.BooleanField(default=False)

class SubService(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    button = models.CharField(max_length=2048, blank=True, null=True)
    belong = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='service')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_ser')

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/gallery", blank=True, null=True)
    belongs_to = models.ForeignKey(
        'SubGallery', on_delete=models.CASCADE, related_name="gallery_images")

class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Gallery"

    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, blank=True)


class SubGallery(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextField()
    button = models.CharField(max_length=100)
    belong = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='gallery')
    lang = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='lang_glr')
