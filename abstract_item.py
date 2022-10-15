from abc import ABC, abstractmethod


class AbstractItem(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    # @abstractmethod
    # def increase_health(self):
    #     pass
    #
    @property
    @abstractmethod
    def unit_types(self):
        pass

    @property
    @abstractmethod
    def set_type(self):
        pass
    #
    # @abstractmethod
    # def modify_health_scale(self):
    #     pass
