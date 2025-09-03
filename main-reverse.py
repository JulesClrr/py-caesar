text = "Ub nésf ftu mb qfstpoof mb qmvt gpsnjebcmf bv npoef Nbyjnf/"
caesartext = ""

def caesar(text, caesartext):
    for letter in text :
        number = ord(letter)
        if number == ord("a") :
            number = number + 26
        elif number == ord(" "):
            number = number + 1

        letters = chr(number-1)
        caesartext = caesartext + letters
        
    print(caesartext)

caesar(text, caesartext)