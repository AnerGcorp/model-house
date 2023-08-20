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

