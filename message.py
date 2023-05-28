import requests
import functions

def message():
    ## incolla il link del form, NB: in caso modificalo perche sia simile a:
    ## https://docs.google.com/forms/d/e/randomLetters
    ## ad esempio solitamente bisogna togliere la perte finale
    ## ESEMPIO: 
    ## form= "https://docs.google.com/forms/d/e/randomLetters"
    form= "https://docs.google.com/forms/d/e/1FAIpQLSea8s-v3JhTRKkY8MhW9vre6_UfW4Lag0sDkTCGQqLBaKQq2w"

    url = form + "/formResponse"

    ## modifica la struttura data con le entry delle domande e la funzione corretta:
    ## generate_random_string per domande in cui è presente un campo per inserire una stringa
    ## generate_random_choiches per domande a risposta chiusa: le opzioni devi modificarle perche
    ## rispecchino quelle del form
    data = {
            #ESEMPIO:
            ##'entry.69420666': c,
            ##'entry.69420666': functions.generate_random_choiches(['Molto', 'Tanto', 'Abbastanza', 'Poco', 'Per nulla']),
            ##'entry.69420666': functions.generate_random_telephone_number(10),
            
            'entry.489441377': functions.generate_random_age(18,20),
            'entry.239216472': functions.generate_random_text(7,10),
            'entry.1597939621': functions.generate_random_choiches(['Opzione 1', 'Opzione 2']),
            'entry.1140745251': functions.generate_random_choiches(['Opzione 1', 'Opzione 2']),
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Richiesta inviata con successo!')## il messaggio è corretto, POTREBBE essere arrivato
    else:
        print('Errore nella richiesta:', response.status_code)