from django.contrib import admin
from .models import CityDetails


class CityDetailsAdmin(admin.ModelAdmin):
    class Meta:
        model = CityDetails

admin.site.register(CityDetails, CityDetailsAdmin)
