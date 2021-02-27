""" Import data and classes"""
import json
from datetime import datetime


class AccessRequest:
    """ Here are the methods and attributes regarding Access Request"""
    def __init__(self, id_document, full_name):
        self.__name = full_name
        self.__id_document = id_document
        just_now = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(just_now)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def name(self):
        """ This represents the getter and setter"""
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id_document(self):
        """ This function contains 1 functions representing the getter in python """
        return self.__id_document
    @id_document.setter
    def id_document(self, value):
        self.__id_document = value
