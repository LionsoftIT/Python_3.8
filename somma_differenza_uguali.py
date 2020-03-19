"""
Creatore: LEONARDO ESSAM DEI ROSSI
E-Mail: leonardo.deirossi@icloud.com
"""

""" Iniziazione """
numero1 = 0.0
numero2 = 0.0
risultato = 0.0

""" Dati in ingresso """
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

""" Dati in uscita """
if(numero1 > numero2): risultato = numero1 + numero2
elif(numero2 > numero1): risultato = numero1 - numero2
else: print("I due numeri sono uguali!")

""" Output """
print("Il risultato è", risultato)
