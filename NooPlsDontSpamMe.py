import message
import time
import spam_utils

## Decidi quanti messaggi inviare. True se non vuoi avere un limite, consigliato inserire un valore pause
how_much= True
## Decidi quanti secondi aspettare prima di inviare un nuovo messaggio. Nb
pause= 0

i=1
while spam_utils.i_feel_like_continuing_spam(i, how_much):
    status= message.message()
    
    if status == 200:
        print('Richiesta', i, 'inviata con successo!')
    else:
        print('Errore nella richiesta', i ,': ', status )
    
    i= i+1
    
    time.sleep(pause)

print('Fine')