"""Beginning access manager"""
import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest


class AccessManager:
    """This class begins here."""
    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        """This function validates the dni"""
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE DNI
        # RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE
        letter = dni[-1]
        number = int(dni[0:8])
        letters = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
                   7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N",
                   13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H",
                   19: "L", 20: "C", 21: "K", 22: "E"}
        n = number % 23
        if letter == letters[n]:
            return True
        return False

    def readaccess_requestfromjson(self, fi):
        """This function reads Jason's request"""
        try:
            with open(fi) as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") \
                from e
        except json.JSONDecodeError as e:
            raise AccessManagementException\
                ("JSON Decode Error - Wrong JSON Format") from e

        try:
            id_doc = data["id"]
            name = data["name"]
            req = AccessRequest(id_doc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") \
                from e

        if not self.validate_dni(id_doc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req
