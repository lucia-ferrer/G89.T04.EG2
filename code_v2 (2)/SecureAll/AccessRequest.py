import json
from datetime import datetime

class AccessRequest:
    def __init__(self, id_document, full_name):
        self.__name = full_name
        self.__id_document = id_document
        just_now = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(just_now)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id_document(self):
        return self.__id_document
    @name.setter
    def id_document(self, value):
        self.__id_document = value
