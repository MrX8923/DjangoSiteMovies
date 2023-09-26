from django.contrib import admin
from .models import *


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = "vet_clinic"

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
    using = "vet_clinic"

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


class HumanTable(MultiDBModelAdmin):
    list_display = ('name', 'surname', 'lastname')
    list_display_links = ('name', 'surname', 'lastname')


admin.site.register(Human, HumanTable)


class VetDoctorTable(MultiDBModelAdmin):
    list_display = ('name', 'surname', 'lastname', 'speciality')
    list_display_links = ('name', 'surname', 'lastname', 'speciality')


admin.site.register(VetDoctor, VetDoctorTable)


class PetOwnerTable(MultiDBModelAdmin):
    list_display = ('name', 'surname', 'lastname')
    list_display_links = ('name', 'surname', 'lastname')



admin.site.register(PetOwner, PetOwnerTable)


class PetTable(MultiDBModelAdmin):
    list_display = ('name', 'age', 'animal_type', 'specialist', 'pet_owner')
    list_filter = ('specialist', 'pet_owner', 'menace')
    fieldsets = (
        ('О звере', {'fields': ('name', 'animal_type', 'age', 'menace', 'pet_owner')}),
        ('Лечение', {'fields': ('specialist', 'treatment')})
    )


admin.site.register(Pet, PetTable)
