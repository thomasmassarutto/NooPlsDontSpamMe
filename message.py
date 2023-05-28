import requests
import functions

def message():
    ## incolla il link del form, NB: in caso modificalo perche sia simile a:
    ## https://docs.google.com/forms/d/e/randomLetters
    ## ad esempio solitamente bisogna togliere la perte finale
    ## ESEMPIO: 
    ## form= "https://docs.google.com/forms/d/e/randomLetters"
    form= ""

    url = form + "/formResponse"

    ## modifica la struttura data con le entry delle domande e la funzione corretta:
    ## generate_random_string per domande in cui è presente un campo per inserire una stringa
    ## generate_random_choiches per domande a risposta chiusa: le opzioni devi modificarle perche
    ## rispecchino quelle del form
    data = {
            #ESEMPIO:
            ##'entry.69420666': functions.generate_random_string(3,10),
            ##'entry.69420666': functions.generate_random_choiches(['Molto', 'Tanto', 'Abbastanza', 'Poco', 'Per nulla']),
            ##'entry.69420666': functions.generate_random_telephone_number(10),
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Richiesta inviata con successo!')## il messaggio è corretto, POTREBBE essere arrivato
    else:
        print('Errore nella richiesta:', response.status_code)