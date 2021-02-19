def recognizer_nie(id):
    letter = id[0]
    number = id[1:7]
    number = int(number)

def recognizer_nif(dni):
   letter=dni[-1]
   number=int(dni[0:7])
   if letter == converse_letter(number):
       return 0
   return -1

def converse_letter(n):
    return "L"