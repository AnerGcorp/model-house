from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import (
    Language, SubCategory, Category, Logo, AboutUs, SubAboutUs,
    Slider, SubSlider, SubAboutCompany, AboutCompany, SubMoreAboutUs,
    MoreAboutUs, NewsImage, SubNews, News, SubService, Service,
    # Statistics, SubStatistics,
    #   Gallery,
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

class SubMoreAboutUsInlineAdmin(admin.StackedInline):
    model = SubMoreAboutUs

class MoreAboutUsAdmin(admin.ModelAdmin):
    inlines = [SubMoreAboutUsInlineAdmin, ]

class NewsImageInlineAdmin(admin.TabularInline):
    model = NewsImage

class SubNewsInlineAdmin(admin.StackedInline):
    model = SubNews

class NewsAdmin(admin.ModelAdmin):
    inlines = (SubNewsInlineAdmin, NewsImageInlineAdmin)

class SubServiceInlineAdmin(admin.StackedInline):
    model = SubService

class ServiceAdmin(admin.ModelAdmin):
    inlines = [SubServiceInlineAdmin, ]


admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Logo)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(AboutCompany, AboutCompanyAdmin)
admin.site.register(MoreAboutUs, MoreAboutUsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Service, ServiceAdmin)