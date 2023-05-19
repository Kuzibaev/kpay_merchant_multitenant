def add_tenant_into_connections(connections, tenant_name):
    default_conf = connections.settings['default'].copy()
    default_conf['NAME'] = tenant_name
    connections.settings[tenant_name] = default_conf
