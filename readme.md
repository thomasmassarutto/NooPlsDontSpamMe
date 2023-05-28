# NooPlsDontSpamMe
 \* +39 420 666 6969  entra nella chat \*

 +39 420 666 6969:
> \*link al Google form\*
> "Ciao, compila il form se vuoi diventare ricco, bello, famoso e possedere 3 arachidi entro  le 7 di sera"

 \* +39 420 666 6969  esce dalla chat \*

Evidentemente il bro vuole iniziare una gara di spam, valutiamo le opzioni disponibili:
1.  Lascio perdere come una persona normale e vado a finire di vedre Breaking Bad prima che lo tolgano da Netflix.
2. Gli scrivo dicendo che ha fatto una cosa brutta e che ora il suo angelo custode piange perche' ha compiuto una brutta azione.
3. Spammo il form perche' sono un cavolo di psicopatico.

Considerando che sei qua, deduco che Breaking Bad lo hai visto nel 2015 come una persona normale e che non credi in tutta quella storia degli angeli, quindi eccoti il bot.

P.S. Saul mi dice di aggiungere che:
_Il presente bot è stato sviluppato esclusivamente per il testing interno di un modulo Google specifico. È strettamente vietato utilizzare il bot per scopi diversi dal testing, come l'invio di risposte inutilizzabili o lo spam. È fondamentale operare in modo etico, responsabile e conforme alle normative vigenti. Si raccomanda di rispettare rigorosamente le condizioni d'uso del modulo Google e di considerare attentamente le possibili conseguenze legali di un utilizzo improprio._
Insomma, non fare monate.

## Come lo uso?
### Intro
Il programma si basa sulla capacità di generare un link precompilato del modulo Google. Lo script genera una moltitudine di link che vengono utilizzati per simulare la compilazione effettiva del modulo da parte di un utente. I dati inseriti nelle risposte sono randomizzati in base alle funzioni utilizzate.

## Utilizzo
Prima di cominciare assicurarsi di aver installato _requests_:
`pip install requests`
Ah e ovviamente Python... (testato con python 3.10.11)

1. **Incollare il link del form da spammare**:
Solitamente i link sono in questo formato:
`https://docs.google.com/forms/d/e/randomLetters/viewform`
bisogna eliminare il `/viewform` di modo che il link risulti:
`https://docs.google.com/forms/d/e/randomLetters` e 
inserilo nella variabile `form` di *message.py*:
`form=https://docs.google.com/forms/d/e/randomLetters`

2. **Ricavare il payload**:
Sta parte è un po' arzigogolata, se non capisci cerca su internet: "How to Check Submitted Form Data in Chrome Dev Tools". Ci sara' sicuramente qualche video.
Accedere al form da spammare, avviare lo strumento _ispeziona_, compilare il form una volta e inviare la risposta "manualmente".
Con lo strumento _ispeziona_ spostarsi nella sezione **Network**. Nel menu laterale sinistro di centro pagina selezionare l'elemento **formResponse**, visualizando il suo **Payload**. In modalità **view source**.
dovrebbe risultare una stringa del genere: `entry.239216472=aaa&entry.1597939621=Opzione+1&entry.1140745251=Opzione+2&dlut=1685189687612&entry.1597939621_sentinel=&entry.1140745251_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-2859418861210136122%22%5D&pageHistory=0&fbzx=-2859418861210136122`.
Questa e' la codifica della risposta che e' appena stata inviata al form: `entry` specifica la domanda e la risposta e' specificata dopo l'"=", ad esempio:
`entry.239216472=aaa`
Significa che alla domanda `entry.239216472` abbiamo risposto con `aaa`.
Copiare la stringa in un editor di testo per modificarla nel passo successivo.

3. **Inserire i dati**:
Inserire tutte le entry nel file *message.py* all'interno della struttura *data* associate alla corrette funzioni in grado di generare rispose random, come nell'esempio:
```python
data = {
        'entry.239216472': functions.generate_random_string(3, 10),
        'entry.1140745251': functions.generate_random_choiches(['Opzione 1', 'Opzione 2']),
        'entry.1597939621': functions.generate_random_choiches(['Opzione 1', 'Opzione 2']),
    }
```
Un elemento di `data` e' quindi composto da `entry.id : functions.funzione_randomizzatrice(),`

4. **Far partire lo script**:
Da *NooPlsDontSpamMe.py* scegliere quanti messaggi inviare modificando il valore della variabile `how_much` e far partire il programma.
Lasciare in esecuzione il programma fino al completamento.

Tecnicamente dovrebbe andare, l'ho testato su qualche mio form, basico e non ha dato problemi. Se ci sono errori, cavoli tuoi, ho fatto questo coso in una giornata solo perche' continuavano a spammare quei cavolo di questionari. Non c'e' ne garanzia, ne supporto, però sei libero di modificarlo quanto vuoi eh.
P.s. Ti consiglio di testarlo prima su un form di prova dove puoi controllare che tutto fili liscio, così non fai correre il tuo pc settordici ore per nulla.

## Errori comuni
La scelta della funzione appaiata alla corretta entry e' fondamentale, gli errori piu' comuni sono:
- non compilare tutte le domande obbligatorie del form
- inserire le opzioni sbagliate con `functions.generate_random_choiches()`, ricorda che 'ciao' != 'Ciao' != ' ciao'
- non rispettare i vincoli imposti dal form: alcuni form hanno dei filtri che segnano errata una risposta se non rispetta dati canoni, ad esempio se in un campo viene richiesta la mail, il form accettera' solo le risposte contenenti una stringa che potrebbe essere una mail, ovvero che termina per @​qualcosa.qualcosa. Assicurati di rispettare i vincoli usando le funzioni apposite, o aggiungi manualmente una stringa.

## Esempio di funzioni randomizzatrici
Per rendere più difficile il filtraggio delle risposte spam vengono usate delle funzioni in grado di randomizzare le risposte date ad ogni singola domanda. Alcuni esempi:
- `functions.generate_random_string(3, 10)`: 
genera una stringa casuale lunga minimo 3, massimo 10 caratteri.

- `functions.generate_random_choiches(['Opzione 1', 'Opzione 2'])`:
seleziona una fra le opzioni. Le opzioni devono essere inserite manualmente fra apici singoli e devono essere identiche a quelle presenti nel form.

Sono presenti anche altre altre funzioni per usi piu specifici, per ulteriori informazioni consulta il codice.

## FAQ
**Q: Quanto devo essere scimmia per usarlo?**

A: 3/10, se sai dell'esistenza di Github, probabilmente sei in grado di usare sto bot.

------------

**Q: Ma e' corretto utilizzarlo?**

A: Non lo so, ma se qua scrivo che e' solo a scopo di test magari la gente non rompe.

------------

**Q: Come posso difendermi da questo bot?**

A: Ci sono un sacco di modi, leggiti la documentazione dei forms di Google per scegliere quello che reputi il migliore (ehh volevi che ti dessi la soluzione bella che pronta, guarda che faccia, guarda che faccia, non se l'aspettava, pensavi li col blocco note, le dita pronte a scrivere, ma sai una cosa? **LEGGITI LA DOCUMENTAZIONE**).

------------

**Q: Quanto spamma?**

A: Se non si inceppa siamo tipo sui 90/100 form al minuto e non l'ho ancora visto fermarsi con messaggi del tipo "Fermo bro, mi sa che hai inviato troppe risposte".

------------
**Q: Quali sono le limitazioni del bot?**

A: E' in grado di spammare solo su form Google che permettono l'invio di più risposte che non raccolgono l'indirizzo Gmail, che cmq e' gia' la maggior parte dei form spammati sui gruppi del genere "Calcetto", "Fortnite Squad 420", "Gruppo di studio Uni".