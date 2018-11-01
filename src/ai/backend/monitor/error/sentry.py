import raven

from ai.backend.common.monitor import AbstractErrorMonitor


class SentryRavenErrorMonitor(AbstractErrorMonitor):

    def __init__(self):
        self.sentry = None

    def init(self, config):
        self.sentry = raven.Client(
            config.raven_uri,
            release=raven.fetch_package_version(config.app_name))

    def capture_exception(self, *args):
        self.sentry.captureException(*args)

    def capture_message(self, msg):
        self.sentry.captureMessage(msg)

    def set_context(self, context):
        self.sentry.user_context(context)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def add_plugin_args(parser):
    parser.add('--raven-uri', env_var='RAVEN_URI',
               type=str, default=None,
               help='The sentry.io event report URL with DSN.')


def get_plugin(config):
    error_monitor = SentryRavenErrorMonitor()
    error_monitor.init(config)
    return error_monitor
