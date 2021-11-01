from django.contrib import admin

from vorwaerts.models import ClassifiedAd
from vorwaerts.models import NewspaperPage


admin.site.register(NewspaperPage)
admin.site.register(ClassifiedAd)
