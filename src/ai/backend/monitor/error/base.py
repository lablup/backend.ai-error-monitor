from abc import ABC, abstractmethod


class AbstractErrorMonitor(ABC):

    @abstractmethod
    def init(self, config):
        raise NotImplementedError

    @abstractmethod
    def capture_exception(self, *args):
        raise NotImplementedError

    @abstractmethod
    def capture_message(self, msg):
        raise NotImplementedError

    @abstractmethod
    def set_context(self, context):
        raise NotImplementedError
