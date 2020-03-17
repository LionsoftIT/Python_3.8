"""
Creatore: LEONARDO ESSAM DEI ROSSI
E-Mail: leonardo.deirossi@icloud.com
"""

""" Iniziazione """
numero1 = 0.0;
numero2 = 0.0;
risultato = 0.0;

""" Dati in ingresso """
numero1 = float(input("Inserisci il primo numero: "));
nuero2 = float(input("Inserisci il secondo numero: "));

""" Dati in uscita """
if(numero1 > numero2): result = numero1 + numero2;
elif(numero2 > numero1): result = numero1 - numero2;
else: print("I due numeri sono uguali!");

""" Output """
if(result != 0.0): print("Il risultato è", risultato);
