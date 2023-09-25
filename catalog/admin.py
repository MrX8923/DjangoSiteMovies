from django.contrib import admin
from .models import *


for mod in models_list:
    admin.site.register(mod)


class ActorTable(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday', 'country')
    list_display_links = ('name', 'surname', 'birthday')


admin.site.register(Actor, ActorTable)


class DirectorTable(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_display_links = ('name', 'surname')


admin.site.register(Director, DirectorTable)


class MovieTable(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('subscription', 'genre', 'rating')
    fieldsets = (
        ('О фильме', {'fields': ('title', 'summary', 'actors')}),
        ('Рейтинг', {'fields': ('rating', 'age_rating', 'subscription')}),
        ('Остальное', {'fields': ('director', 'genre', 'year', 'country')})
    )


admin.site.register(Movie, MovieTable)


class SubInLine(admin.TabularInline):
    model = Movie


class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubInLine]


admin.site.register(Subscription, SubscriptionAdmin)
