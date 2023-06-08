import requests
import answer

def message():
     ## paste the link of the form, NB: in case modify it so that it is similar to:
     ## https://docs.google.com/forms/d/e/rand0mL1nk
     ## for example usually you have to remove the final part
     ## EXAMPLE:
     ## form="https://docs.google.com/forms/d/e/rand0mL1nk"
    form= ""

    url = form + "/formResponse"

    ## modifica la struttura data con le entry delle domande e la funzione corretta:
    ## generate_random_string per domande in cui è presente un campo per inserire una stringa
    ## generate_random_choiches per domande a risposta chiusa: le opzioni devi modificarle perche
    ## rispecchino quelle del form
    
    ## modify the data structure with the correct entries and the correct function:
    ## choose the correct function from the file "answer.py" 
    data = {
            ## EXAMPLE:
            ##'entry.694206661': answer.generate_random_string(3,10),
            ##'entry.694206662': answer.generate_random_choiches(['Always', 'Usually', 'Often', 'Sometimes', 'Never']),
            ##'entry.694206663': answer.generate_random_telephone_number(),

            ## if the form requires one verified mail, uncomment the line below and fill the blank with a valid e-mail (xxx@gmail)
            ## NB, the e-mail address will be visible to the form owner, choose a burner one for privacy!
            # 'emailAddress': ''    
    }
    
    ## if the form requires one verified mail, complete the blank with the __Secure-3PSID cookie.
    ## the cookie string is in the "cookie" tab near the payload where you found the entries above
    ## it will be a string like AloTofCharactTers_S0met1meSthereIsals0anumb3r_Afacsg2j75Dyk.
    cookies={
            ## when will the cookie expire?Note that here!
            '__Secure-3PSID': ' '
     }

    ## if the form does not require one verified mail, do not sent the cookies value, delete ", cookies=cookies".
    response = requests.post(url, data=data, cookies=cookies)
  
    return response.status_code