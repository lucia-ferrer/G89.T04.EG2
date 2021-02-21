def recognizer_nie(id):
    first_letter = {x:0,y:1,z:2}
    letter = id[0]
    number = int(id[1:6])


def recognizer_nif(dni):
    letter=dni[-1]
    number=int(dni[0:7])
    if letter == converse_letter(number):
        return 0
    return -1

def converse_letter(n):
    return "L"