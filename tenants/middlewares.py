import threading

from django.http import Http404

from .helpers import add_tenant_into_connections
from .models import Tenant
from .utils import tenant_db_from_request, hostname_from_request

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from main.settings.base import DEBUG

        host = request.get_host().split(':')[0]
        # user if not debug true replace hostname or host
        if not DEBUG and host == "hostname":
            request.urlconf = "main.urls"
        elif DEBUG and host == "localhost":
            request.urlconf = "main.urls"
        else:
            tenant = Tenant.objects.filter(name=tenant_db_from_request(request)).first()
            if not tenant:
                raise Http404("Tenant not found")

            request.urlconf = "main.tenant_urls"
            from django.db import connections
            add_tenant_into_connections(connections, tenant.name)
            set_tenant_router(tenant.name)

        response = self.get_response(request)
        return response


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_tenant_router(db):
    setattr(THREAD_LOCAL, "DB", db)
