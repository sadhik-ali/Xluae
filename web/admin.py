from django.contrib import admin
from web.models import Contact
from web.models import EducationalPrograms
from web.models import Feature
from web.models import SocialMedia
from web.models import Team
from web.models import WeOffer
from web.models import Magazine

# Register your models here.


@admin.register(WeOffer)
class WeOfferAdmin(admin.ModelAdmin):
    list_display = ("heading",)


@admin.register(EducationalPrograms)
class EducationalProgramsAdmin(admin.ModelAdmin):
    list_display = ("course_name",)
    prepopulated_fields = {"slug": ("course_name",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("platform",)

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ("name","month")
