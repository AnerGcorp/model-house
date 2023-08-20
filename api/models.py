from django.db import models
from django.core.validators import FileExtensionValidator
# from ckeditor.fields import RichTextField

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

