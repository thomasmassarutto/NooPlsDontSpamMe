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
def generate_random_name_surname(min_length, max_length):
    return generate_random_string(min_length, max_length) + ' ' + generate_random_string(min_length, max_length)
## output: 'ghvf gbhj'

## genera un testo 
def generate_random_text(min_length, max_length):
    length = random.randint(min_length, max_length)
    text= ''
    for i in range(length):
        text = text + generate_random_string(1, 10) + ' '
    return text
## output: 'hcgfd vfj jhb'

## genera una stringa di charatteri che termina con @gmail.com
def generate_random_mail(min_length, max_length):
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
def generate_random_telephone_number(length):
    characters= string.digits
    random_value = ''.join(random.choices(characters, k=length-1))
    return '3' + random_value
## output: '3097653589'

def generate_random_age(min_age, max_age):
    age = random.randint(min_age, max_age)
    return age