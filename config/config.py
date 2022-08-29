import yaml

config_file_dev = "C:/Users/HP/PycharmProjects/seleniumFramework/config/config_dev.yml"

with open(config_file_dev, 'r')as stream:
    cfg = yaml.safe_load(stream)
    # Basic application data
    APP_BASE_URL = cfg['app_base_url']
    APP_USER_LOGIN = cfg['app_user_login']
    APP_USER_PASS = cfg['app_user_pass']

    # Basic web driver config
    HEADLESS = cfg['headless']
    FULLSCREEN = cfg['fullscreen']
    DISABLE_NOTIFICATIONS = cfg['disable_notifications']
    MAX_WAIT = cfg['max_wait']
    MIN_WAIT = cfg['min_wait']
    TEST_RUN_TIMEOUT = cfg['test_run_timeout']
    RERUN = cfg['rerun']


