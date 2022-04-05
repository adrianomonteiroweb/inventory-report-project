from abc import abstractmethod


class Importer:
    @abstractmethod
    def import_data(data):
        raise NotImplementedError


# # https://stackoverflow.com/questions/4382945/abstract-methods-in-python
