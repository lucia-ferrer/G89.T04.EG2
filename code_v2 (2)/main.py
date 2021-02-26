"""The program begins here."""
from SecureAll import AccessManager
from SecureAll import AccessRequest


def main():
    """This function starts the program"""
    mng = AccessManager()
    res = mng.readaccess_requestfromjson("test.json")
    print(res)


if __name__ == "__main__":
    main()
