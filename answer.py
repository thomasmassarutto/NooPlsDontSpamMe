## This file contains a list of useful functions that generate random data.

import random
import string

## generate a random string of characters
def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    characters= string.ascii_lowercase
    random_value = ''.join(random.choices(characters, k=length))
    return random_value
## output: 'uyrtuftybu'

## generates two strings separated by a space
def generate_random_name():
    name = random.choice(["Mario", "Luigi", "Francesca", "Giuseppe",
                         "Alessia", "Giovanni", "Anna", "Luca", "Laura",
                         "Roberto", "Matteo", "Federica", "Gabriele", "Andrea",
                         "Sebastiano", "Laura", "Ludovica","Chiara", "Fabrizio",
                         "Mauro", "Denise", "Larisa", "Marco", "Damiano", "Giulia", "Paola",
                         "Lucrezia", "Elena", "Jessica", "Beatrice"])
    return name
def generate_random_surname():
    surname = random.choice(["Rossi", "Bianchi", "Verdi", "Russo", "Ferrari", "Esposito",
                            "Colombo", "Romano", "Conti", "Galli", "Ricci", "Marino", "Costa",
                            "Gallo", "Rizzo", "Rinaldi", "Marchetti", "Coppola", "Palma", "Benedetti",
                            "Piazza", "Viscardis", "Marangon", "De Luca", "De Pasquale", "Casella", "Castaldi",
                            "Felici", "Gentilin", "Lopez", "Martinelli", "Moro", "Moro", "Moro", "Simonini",
                             "Santoro", "Zivkovic", "Zolnowski", "Giuliani", "Favero", "Ahamed", "Antosh", "Sina", 
                            "Ferrin", "Hossain", "Ahmad", "Abubakar", "Albani", "Chi", "Hang Yu"] )
    return surname
## output: 'Ghvf Pbhj'

## generate a text
def generate_random_text(min_length, max_length):
    length = random.randint(min_length, max_length)
    text= generate_random_string(1, 10).capitalize() + ' '
    for i in range(length -1):
        text = text + generate_random_string(1, 10) + ' '
    return text
## output: 'Hcgfd vfj jhb'

## generates a string of characters ending with @gmail.com
def generate_random_mail():
    min_length= 5
    max_length= 10
    length = random.randint(min_length, max_length)
    characters= string.ascii_lowercase
    random_value = ''.join(random.choices(characters, k=length))
    return random_value + '@gmail.com'
## output: ghbj@gmail.com

## given a list of options choose one at random
def generate_random_choiches(options):
    random_option= random.choice(options)
    return random_option
## output: 'Opzione 1'

## generate a phone number starting with 3, so it doesn't look fake (at least in Italy)
def generate_random_telephone_number():
    digits= string.digits
    random_value = ''.join(random.choices(digits, k=9))
    return '3' + random_value
## output: '3097653589'

## generate a number between a min and a max (this is a "bypass" for randint function)
def generate_random_number(min_age, max_age):
    nbr = random.randint(min_age, max_age)
    return nbr
## output: 20