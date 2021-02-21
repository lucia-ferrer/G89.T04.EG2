def recognizer_nie(id):
    first_letter = {"x":0,"y":1,"z":2}
    letter = id[0]
    last_number = first_letter[letter]
    real_number = int(id[7])
    if last_number != real_number:
        return -1
    number = int(id[1:7])
    real_letter = converse_letter(number)
    if real_letter != id[8]:
        return -1
    return 0

def recognizer_nif(dni):
    letter=dni[-1]
    number=int(dni[0:7])
    if letter == converse_letter(number):
        return 0
    return -1

def converse_letter(n):
    letters = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}
    number = n/23
    return letters[number]