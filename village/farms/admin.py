# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from django.contrib import admin
from .models import house_hold,persons_info,farm_info,season_info,well_info,well_observation,farm_location,crops

admin.site.register(house_hold)
admin.site.register(persons_info)
admin.site.register(farm_info)
admin.site.register(farm_location)
admin.site.register(season_info)
admin.site.register(crops)
admin.site.register(well_info)
admin.site.register(well_observation)
