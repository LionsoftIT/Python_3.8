"""
Creatore: LEONARDO ESSAM DEI ROSSI
E-Mail: leonardo.deirossi@icloud.com
"""

""" Variabili """
costo_studenti = 35;
costo_adulti = 60;
studenti_req_sconto = 3;
sconto_studenti = 25;
totale_adulti = 0;
totale_studenti = 0;
costo_totale = 0;

""" Inserimento dati """
totale_adulti = int(input("Inserisci il numero di adulti: "));
totale_studenti = int(input("Inserisci il numero di studenti: "));

""" Calcoli """
if (totale_studenti >= studenti_req_sconto):
    costo_studenti = sconto_studenti;

costo_totale = (totale_adulti * costo_adulti)+(totale_studenti * costo_studenti);

""" In uscita """
print("Il prezzo finale dell'abbonamento è di " + str(costo_totale));
