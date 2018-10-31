import raven

from .base import AbstractErrorMonitor


class SentryRavenErrorMonitor(AbstractErrorMonitor):

    def __init__(self):
        self.sentry = None

    def init(self, config):
        self.sentry = raven.Client(
            config.raven_uri,
            release=raven.fetch_package_version('backend.ai-manager'))

    def capture_exception(self, *args):
        self.sentry.capture_exception(*args)

    def capture_message(self, msg):
        self.sentry.capture_message(msg)

    def set_context(self, context):
        self.sentry.update_context(context)


def add_plugin_args(parser):
    parser.add('--raven-uri', env_var='RAVEN_URI',
               type=str, default=None,
               help='The sentry.io event report URL with DSN.')


def get_plugin(config):
    error_monitor = SentryRavenErrorMonitor()
    error_monitor.init(config)
    return error_monitor
