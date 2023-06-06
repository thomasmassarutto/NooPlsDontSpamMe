import random
import string

## genera una stringa casuale di caratteri  
def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    characters= string.ascii_lowercase
    random_value = ''.join(random.choices(characters, k=length))
    return random_value
## output: 'uyrtuftybu'

## genera due stringhe separate da spazio
def generate_random_name_surname():
    min_length= 5 
    max_length= 10
    name = generate_random_string(min_length, max_length).capitalize()
    surname = generate_random_string(min_length, max_length).capitalize()
    return  name + ' ' + surname
## output: 'Ghvf Pbhj'

## genera un testo 
def generate_random_text(min_length, max_length):
    length = random.randint(min_length, max_length)
    text= generate_random_string(1, 10).capitalize() + ' '
    for i in range(length -1):
        text = text + generate_random_string(1, 10) + ' '
    return text
## output: 'Hcgfd vfj jhb'

## genera una stringa di charatteri che termina con @gmail.com
def generate_random_mail():
    min_length= 5
    max_length= 10
    length = random.randint(min_length, max_length)
    characters= string.ascii_lowercase
    random_value = ''.join(random.choices(characters, k=length))
    return random_value + '@gmail.com'
## output: ghbj@gmail.com

## data una lista di opzioni ne sceglie una a caso
def generate_random_choiches(options):
    random_option= random.choice(options)
    return random_option
## output: 'Opzione 1'

## genera un numero di telefono che comincia con 3, così non sembra fasullo (almeno in ita)
def generate_random_telephone_number():
    digits= string.digits
    random_value = ''.join(random.choices(digits, k=9))
    return '3' + random_value
## output: '3097653589'

## genera un numero compreso fra un min e un max (bypass)
def generate_random_number(min_age, max_age):
    age = random.randint(min_age, max_age)
    return age
## output: 20