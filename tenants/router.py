from .middlewares import get_current_db_name


class TenantRouter:
    def db_for_read(self, model, **hints):
        tenant = get_current_db_name()
        return tenant

    def db_for_write(self, model, **hints):
        tenant = get_current_db_name()
        return tenant

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None
