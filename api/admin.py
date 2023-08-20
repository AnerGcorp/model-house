from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import (
    Language, SubCategory, Category, Logo, AboutUs, SubAboutUs,
    Slider, SubSlider, SubAboutCompany, AboutCompany
    # Statistics, SubStatistics,
    # MoreAboutUs, SubMoreAboutUs, News, NewsImage, SubNews, Gallery,
    # GalleryImage, SubGallery, ContactUs, AboutUs, SubAboutUs, Contacts,
    # SubContacts, AboutCompany, SubAboutCompany, Partner
    )

class SubCategoryInlineAdmin(admin.StackedInline):
    model = SubCategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInlineAdmin, ]

class SubAboutUsInlineAdmin(admin.StackedInline):
    model = SubAboutUs

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [SubAboutUsInlineAdmin, ]

class SubSliderInlineAdmin(admin.StackedInline):
    model = SubSlider

class SliderAdmin(admin.ModelAdmin):
    inlines = [SubSliderInlineAdmin, ]

class SubAboutCompanyInlineAdmin(admin.StackedInline):
    model = SubAboutCompany

class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [SubAboutCompanyInlineAdmin, ]

admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Logo)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(AboutCompany, AboutCompanyAdmin)