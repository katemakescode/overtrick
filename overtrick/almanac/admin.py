from django.contrib import admin

from almanac.models import Session
from pairs.models import Pair


class PairInline(admin.TabularInline):
    model = Pair


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['club', 'date', 'time', 'event']
    inlines = [PairInline]
