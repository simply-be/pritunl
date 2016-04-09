from pritunl.settings.group_mongo import SettingsGroupMongo

class SettingsApp(SettingsGroupMongo):
    group = 'app'
    fields = {
        'server_ssl': True,
        'server_port': 443,
        'reverse_proxy': False,
        'reverse_proxy_header': 'X-Forwarded-For',
        'redirect_server': True,
        'server_watch': True,
        'server_watch_timeout': 10,
        'demo_mode': False,
        'allow_insecure_session': False,
        'auditing': None,
        'monitoring': None,
        'prometheus_port': 9780,
        'datadog_api_key': None,
        'settings_check_interval': 600,
        'key_link_timeout': 86400,
        'password_len_limit': 128,
        'public_ip_server': 'https://app.pritunl.com/ip',
        'public_ip6_server': 'https://app6.pritunl.com/ip',
        'notification_server': 'https://app.pritunl.com/notification',
        'update_check_rate': 3600,
        'session_limit': 16,
        'session_timeout': 86400,
        'peer_limit': 500,
        'peer_limit_timeout': 10,
        'log_limit': 10000,
        'log_entry_limit': 50,
        'log_db_delay': 1,
        'log_web_errors': False,
        'rate_limit_sleep': 0.5,
        'short_url_length': 8,
        'license': None,
        'license_plan': None,
        'http_request_timeout': 15,
        'request_queue_size': 8,
        'request_thread_count': 256,
        'static_cache_time': 43200,
        'auth_time_window': 300,
        'auth_limiter_ttl': 60,
        'auth_limiter_count_max': 30,
        'org_pool_size': 1,
        'user_pool_size': 6,
        'server_pool_size': 4,
        'server_user_pool_size': 2,
        'dh_param_bits_pool': [1536],
        'cookie_secret': None,
        'email_server': None,
        'email_username': None,
        'email_password': None,
        'email_from': None,
        'id': None,
        'sso': False,
        'sso_match': None,
        'sso_host': None,
        'sso_token': None,
        'sso_secret': None,
        'sso_timeout': 60,
        'sso_org': None,
        'sso_saml_url': None,
        'sso_saml_issuer_url': None,
        'sso_saml_cert': None,
        'sso_saml_duo_skip_unavailable': False,
        'sso_okta_token': None,
        'sso_okta_poll_rate': 0.25,
        'sso_okta_skip_unavailable': True,
        'sso_onelogin_key': None,
        'queue_low_thread_limit': 4,
        'queue_med_thread_limit': 2,
        'queue_high_thread_limit': 1,
        'host_ping': 10,
        'host_ping_ttl': 30,
        'theme': 'dark',
        'org_page_count': 5,
        'server_page_count': 3,
        'host_page_count': 10,
        'acme_api_url': 'https://acme-v01.api.letsencrypt.org',
        'acme_timestamp': None,
        'acme_key': None,
        'acme_domain': None,
        'acme_renew': 2592000,
        'server_cert': None,
        'server_key': None,
        'server_dh_params': None,
        'server_dh_size': 1024,
        'cloud_provider': None,
        'us_east_1_access_key': None,
        'us_east_1_secret_key': None,
        'us_west_1_access_key': None,
        'us_west_1_secret_key': None,
        'us_west_2_access_key': None,
        'us_west_2_secret_key': None,
        'eu_west_1_access_key': None,
        'eu_west_1_secret_key': None,
        'eu_central_1_access_key': None,
        'eu_central_1_secret_key': None,
        'ap_northeast_1_access_key': None,
        'ap_northeast_1_secret_key': None,
        'ap_northeast_2_access_key': None,
        'ap_northeast_2_secret_key': None,
        'ap_southeast_1_access_key': None,
        'ap_southeast_1_secret_key': None,
        'ap_southeast_2_access_key': None,
        'ap_southeast_2_secret_key': None,
        'sa_east_1_access_key': None,
        'sa_east_1_secret_key': None,
    }
