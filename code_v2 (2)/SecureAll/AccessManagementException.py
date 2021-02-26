""" This class is to manage exceptions """


class AccessManagementException(Exception):
    """ This class is to manage exceptions """

    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """ This function requires """
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
