from uuid import UUID


class Scanner:
    def __init__(self, id: int, uuid: UUID, name: str, type: str, status: str,
                 scan_count: int, engine_version: str, platform: str,
                 ):
        self.id = id
        self.uuid = uuid
        self.name = name
        self.type = type


example_scanner = {
    'aws_availability_zone': None,
    'aws_update_interval': None,
    'challenge': '8771c11a79e78516e20599f9e19eb5e24d65d56f',
    'creation_date': 1432583601,
    'engine_build': 'M20111',
    'engine_version': '7.0.3',
    'expiration': 1554004800,
    'expiration_time': 353,
    'id': 1,
    'key': '00faf587f7d455883db88d85538cadae00ca6988e9311be97986281eb6853cca7e',
    'last_connect': None,
    'last_modification_date': 1432583601,
    'linked': 1,
    'loadavg': None,
    'loaded_plugin_set': '201804110615',
    'name': 'Local Scanner',
    'needs_restart': None,
    'num_hosts': None,
    'num_scans': 6,
    'num_sessions': None,
    'num_tcp_sessions': None,
    'owner': 'nessus_ms_agent',
    'owner_id': 1,
    'owner_name': 'system',
    'platform': 'LINUX',
    'registration_code': 'SSJB-YUDA-8AQS-QA73',
    'scan_count': 6,
    'shared': 1,
    'status': 'on',
    'timestamp': 1432583601,
    'token': None,
    'type': 'local',
    'ui_build': '111',
    'ui_version': '7.0.3',
    'user_permissions': 64,
    'uuid': '00000000-0000-0000-0000-00000000000000000000000000000',
    'license': {'activation_code': 'SSJB-YUDA-8AQS-QA73',
                'agents_used': 0,
                'expiration_date': 1554004800,
                'features': {'api': True,
                             'custom_reports': False,
                             'email_reports': False,
                             'local_scanner': True,
                             'logs': False,
                             'plugin_rules': True,
                             'remote_link': True,
                             'report': True,
                             'scan_api': True,
                             'smtp': True,
                             'software_update': True,
                             'users': True},
                'mode': 2,
                'name': 'Nessus Professional',
                'restricted': True,
                'scanners_used': 0,
                'type': 'professional',
                'update_password': '5a799a3505b77e1ee15bd738ee7a2e5e',
                'update_url': 'https://plugins.nessus.org/v2/nessus.php'},
}
