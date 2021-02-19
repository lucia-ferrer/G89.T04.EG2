def recognizer_nie(ID):
    letter = ID[0]
    number = ID[1:7]
    number = int(number)

def recognizer_nif(dni):
   letter=dni[-1]
   number=int(dni[0:7])
   if letter == converse_letter(number):
       return 0
   return -1

def converse_letter(n):