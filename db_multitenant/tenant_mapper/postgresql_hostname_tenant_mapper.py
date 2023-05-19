import re
from db_multitenant import mapper

HOST_REGEX = re.compile(r'(\w+)[\.|$]')


class TenantMapper(mapper.TenantMapper):
    def get_tenant_name(self, request):
        """Takes the first part of the hostname as the name"""
        hostname = request.get_host()
        match = HOST_REGEX.search(hostname)
        tenant_name = match.groups()[0].lower() if match else None

        # Compare against a whitelist or fallback to 'public'?
        if not tenant_name:
            raise ValueError('Unable to find the name name from `%s`.' % hostname)

        return tenant_name

    def get_db_name(self, request, tenant_name):
        # Still use the DB name of settings
        return tenant_name

    def get_cache_prefix(self, request, tenant_name, db_name):
        """The arguments db_name and tenant_name are provided by the methods of this TenantMapper"""
        return 'name-%s' % tenant_name
