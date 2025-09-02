text = 'ta mère est la personne la plus formidable au monde maxime'
caesartext = ''


def caesar(text, caesartext):
        
    for letter in text:
        number = ord(letter)
        if number+1 >= 123:
            number = 96
        if number+1 == 33:
            number = 31
        letters = chr(number+1)
        caesartext = caesartext+letters
    print(caesartext)


caesar(text, caesartext)

