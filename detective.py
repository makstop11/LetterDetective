print(' Добро пожаловать в программу "Буква-Детектив"')

print('Выберите алфавит: 1 - Латинский, 2 - Кирилица')

alphabet: str = input('Введите номер алфавита:')

if alphabet not in ('1', '2'):
    print('"Упс! Выбран неверный режим. Попробуйте ещё раз...')
else:
    letter: str = input('Введите букву').upper()

    vowel = ['А', 'У', 'О', 'И', 'Э', 'Ы', 'Я', 'Ю', 'Е', 'Ё']
    consonant = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
                 'Щ']
    eng_vowels = ['A', 'E', 'I', 'O', 'U']
    eng_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',
                      'Z']

    if letter in vowel or letter in eng_vowels:
        print(letter, '- буква гласная')
    elif letter in consonant or letter in eng_consonants:
        print(letter, '- буква согласная')
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
