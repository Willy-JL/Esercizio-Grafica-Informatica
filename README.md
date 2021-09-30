### Step:
 - Capisco come funziona il foglio di esempio:
   - Ogni riga ha una formattazione condizionale
   - Ogni casella viene colorata in base al numero (RGB standard 0-255) che contiene
 - Conto pixel nel foglio di esempio: altezza 106 larghezza 128
 - Scelgo un quadro (Il Palazzo dei Papi ad Avignone) e ritaglio l'immagine per arrivare alla stessa grandezza
 - Scrivo semplice algoritmo in Python per creare nuovi valori analoghi:
   - Apro l'immagine usando Pillow
   - Per ogni riga di pixel e successivamente ogni casella calcolo i valori rgb e li metto in memoria
   - Alla fine ottengo una tabella di dati con questa struttura:
   ```csv
   123,213,112,132,...,
   165,186,140,143,...,
   139,175,226,244,...,
   123,213,112,132,...,
   165,186,140,143,...,
   139,175,226,244,...,
   ```
   - Che posso poi incollare in excel, che li separa nelle corrette righe e colonne
 - Incollo l'output dello script Python sopra alle caselle dell esempio e salvo come output.xlsx
