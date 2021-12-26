def MorzeTranselate(text_message):

    Morzedict = {'а': '.-',
                 'б': '-...',
                 'в': '.--',
                 'г': '--.',
                 'д': '-..',
                 'е': '.',
                 'ж': '...-',
                 'з': '--..',
                 'и': '..',
                 'й': '.---',
                 'к': '-.-',
                 'л': '.-..',
                 'м': '--',
                 'н': '-.',
                 'о': '---',
                 'п': '.--.',
                 'р': '.-.',
                 'с': '...',
                 'т': '-',
                 'у': '..-',
                 'ф': '..-.',
                 'х': '....',
                 'ц': '-.-.',
                 'ч': '---.',
                 'ш': '----',
                 'щ': '--.-',
                 'ь': '-..-',
                 'э': '..-..',
                 'ю': '..--',
                 'я': '.-.-',
                 '1': '.----',
                 '2': '..---',
                 '3': '...--',
                 '4': '....-',
                 '5': '.....',
                 '6': '-....',
                 '7': '--...',
                 '8': '---..',
                 '9': '----.',
                 '0': '-----',
                 '.': '......',
                 ',': '.-.-.-',
                 ':': '---...',
                 ';': '-.-.-.',
                 '(': '-.--.-',
                 ')': '-.--.-',
                 '"': '.-..-.',
                 '-': '-....-',
                 '/': '-..-.',
                 '_': '..--.-',
                 '?': '..--..',
                 '!': '--..--',
                 '+': '.-.-.',
                 '@': '.--.-.',
                 'конецсвязи': '...-.-',
                 ' ': '  '
                 }

    text_message = text_message.lower()
    trans = []
    for letter in text_message:
        trans.append(Morzedict.get(letter))
    print(*trans)


def main(input_string):

    MorzeTranselate(input_string)


if __name__ == '__main__':
    main(input('Введите строку: '))
