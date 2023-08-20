from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import (
    Language, SubCategory, Category,
    # Slider, SubSlider, Statistics, SubStatistics,
    # MoreAboutUs, SubMoreAboutUs, News, NewsImage, SubNews, Gallery,
    # GalleryImage, SubGallery, ContactUs, AboutUs, SubAboutUs, Contacts,
    # SubContacts, AboutCompany, SubAboutCompany, Partner
    )

class SubCategoryInlineAdmin(admin.StackedInline):
    model = SubCategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInlineAdmin, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Language)