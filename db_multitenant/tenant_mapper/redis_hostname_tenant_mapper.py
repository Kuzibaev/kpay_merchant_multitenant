from db_multitenant import mapper
from django.http import Http404
import redis

REDIS_POOL = redis.ConnectionPool(host='localhost', port=6379, db=0)


class RedisTenantMapper(mapper.TenantMapper):
    def get_tenant_name(self, request):
        """Assumes Redis maps hostname -> name name."""
        hostname = request.get_host().split(':')[0].lower()
        r = redis.Redis(connection_pool=REDIS_POOL)
        name = r.get(hostname)
        if not name:
            raise Http404('Unknown name for hostname: "%s"' % hostname)
        return name

    def get_db_name(self, request, tenant_name):
        """Returns name-<tenant_name>, using name name from Redis."""
        return 'name-%s' % tenant_name

    def get_cache_prefix(self, request, tenant_name, db_name):
        """The arguments db_name and tenant_name are provided by the methods of this TenantMapper.
           Returns name-<tenant_name>, using name name from Redis."""
        return 'name-%s' % tenant_name
