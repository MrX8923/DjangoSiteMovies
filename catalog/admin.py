from django.contrib import admin
from .models import *


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = "movies"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


class MultiDBTabularInline(admin.TabularInline):
    using = "movies"

    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


class ActorTable(MultiDBModelAdmin):
    list_display = ('name', 'surname', 'birthday', 'country')
    list_display_links = ('name', 'surname', 'birthday')


admin.site.register(Actor, ActorTable)


class DirectorTable(MultiDBModelAdmin):
    list_display = ('name', 'surname')
    list_display_links = ('name', 'surname')


admin.site.register(Director, DirectorTable)


class MovieTable(MultiDBModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('subscription', 'genre', 'rating')
    fieldsets = (
        ('О фильме', {'fields': ('title', 'summary', 'actors')}),
        ('Рейтинг', {'fields': ('rating', 'age_rating', 'subscription')}),
        ('Остальное', {'fields': ('director', 'genre', 'year', 'country')})
    )


admin.site.register(Movie, MovieTable)
for mod in models_tuple:
    admin.site.register(mod, MultiDBModelAdmin)

# class SubInLine(MultiDBTabularInline):
#     model = Subscription
#
#
# class SubscriptionAdmin(MultiDBModelAdmin):
#     inlines = [SubInLine]

#
# admin.site.register(Subscription, SubscriptionAdmin)
