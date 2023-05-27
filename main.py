import random

def generate_password(length, chars):
    passw = ''
    for i in range(int(length)):
        passw += random.choice(chars)
    return passw

def is_digit(text):
    while True:
        num = input(text)
        if num.isdigit() == False:
            print('\nНужно ввести цифрами!\n')
            continue
        else:
            if 0 < int(num) < 101:
                return num
            else:
                print('\nСлишком большая цифра!\n')
                continue

def yes_no(text):
    while True:
        answer = input(text)
        if answer.lower() not in ['y', 'n']:
            print('\nНужно ввести "y" or "n"!\n')
            continue
        else:
            return answer

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

asks = [
    'Укажите количество паролей для генерации: ',
    'Укажите длину одного пароля: ',
    'Включать ли цифры 0123456789? (y/n) : ',
    'Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) : ',
    'Включать строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) : ',
    'Исключать неоднозначные символы il1Lo0O? (y/n) : ',
    '\nПовторить? : '
    ]

while True:
    chars = ''
    amount = is_digit(asks[0])
    length = is_digit(asks[1])
    on_digit = yes_no(asks[2])
    if on_digit == 'y':
        chars += DIGITS
    on_ALPH = yes_no(asks[3])
    if on_ALPH == 'y':
        chars += UPPERCASE_LETTERS
    on_alph = yes_no(asks[4])
    if on_alph == 'y':
        chars += LOWERCASE_LETTERS
    on_except = yes_no(asks[5])
    if on_except == 'y':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    for i in range(int(amount)):
        print()
        print(generate_password(length, chars))
    repeat = yes_no(asks[6])
    if repeat == 'y':
        print()
        continue
    else:
        break
