"""'
Una nuova compagnia telefonica ha promosso l’offerta “oltre80”. Alla
cifra fissa di € 0,10 (costo alla risposta), occorre aggiungere la cifra
di € 0,15 per ogni secondo del tempo della telefonata; però oltre gli
80 secondi la tariffa per ogni secondo è di € 0,09. Fornito da tastiera
il numero dei secondi della telefonata, visualizzare il costo totale
della chiamata.
..."""



#inizializzazione

SOGLIA = 80.0
COSTO_RISP = 0.10
COSTO_SEC = 0.15
OLTRE_SOGLIA = 0.09
tempo_chiamata = 0.0
costo_chiamata = 0.0

#input

tempo_chiamata = float(input("Inserisci la durata della chiamata in secondi: "))

if tempo_chiamata != 0:
  if tempo_chiamata > SOGLIA: 
   costo_chiamata = COSTO_RISP + COSTO_SEC * SOGLIA + (tempo_chiamata - SOGLIA) * OLTRE_SOGLIA
   print("Il costo della chiamata equivale a: ", costo_chiamata, "euro")
  else:
   costo_chiamata = COSTO_RISP + COSTO_SEC * tempo_chiamata
   print("Il costo della chiamata equivale a: ", costo_chiamata, "euro")
else: 
  costo_chiamata = 0.0
  print("il costo della chiamata è uguale a: ", costo_chiamata, "€")
   
print("Grazie e arrivederci")
