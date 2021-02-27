""" This file contains the class to manage exceptions """


class AccessManagementException(Exception):
    """ Here are the sttributes and methods regarding Exceptions management """

    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """ This function represents the getter"""
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
