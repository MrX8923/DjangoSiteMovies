class MovieRouter:
    route_app_labels = {'catalog'}
    movies_tuple = (
            'movies_table', 'movies_genre',
            'movies_actor', 'movies_country',
            'movies_director', 'movies_age_rating',
            'movies_subscription'
    )

    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.movies_tuple:
            return 'movies'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.movies_tuple:
            return 'movies'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'movies'
        return None


class VetClinicRouter:
    route_app_labels = {'vet_clinic'}
    clinic_tuple = (
            'clinic_pet', 'clinic_pet_owner',
            'clinic_doctor'
    )

    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.clinic_tuple:
            return 'vet_clinic'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.clinic_tuple:
            return 'vet_clinic'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'vet_clinic'
        return None
