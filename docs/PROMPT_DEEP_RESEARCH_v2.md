# Prompt di Deep Research v2 — Lead generation B2B long stay

> **Data:** 27 agosto 2026
> **Origine:** revisione del prompt v1 proposto dal committente
> **Correzioni applicate:** direzione del flusso, verificabilità bloccante, rimozione del
> mapping nominativo LinkedIn, capienza e prezzo dichiarati, scoring semplificato e giustificato,
> annunci di lavoro con alloggio come trigger, distretto calzaturiero, esclusione foresterie,
> output ridotto, suddivisione in tre run.

---

## ⚠️ PRIMA DI LANCIARE — due campi da compilare

Nei prompt trovi due segnaposto tra parentesi quadre. **Vanno sostituiti con i dati reali**,
altrimenti lo scoring gira a vuoto:

- `[N_APPARTAMENTI]` — numero di unità realmente destinabili al long stay
- `[N_POSTI_LETTO]` — capienza complessiva di quelle unità

Se il numero non è ancora deciso, metti il massimo teorico e annotalo.

## Come lanciarli

Tre run **separati**, in tre conversazioni distinte. Non unirli: una deep research ha un budget
di ricerca finito e concentrarlo su un obiettivo per volta è ciò che distingue trenta prospect
verificati da trenta plausibili.

| Run | Obiettivo | Quando |
|---|---|---|
| **1** | Aziende che generano domanda di alloggio nell'area | Per primo — è dove sta il valore |
| **2** | Intermediari e piattaforme di corporate housing | In parallelo o subito dopo |
| **3** | Canali di ingresso sui Tier 1 emersi da 1 e 2 | Solo dopo aver letto i primi due |

---
---

# RUN 1 — Aziende che generano domanda di alloggio long stay

```
RUOLO

Agisci come Senior B2B Market Intelligence Analyst specializzato in corporate long-stay
accommodation, temporary employee housing, workforce accommodation, project housing e
domanda immobiliare temporanea generata da aziende.

Lavori con disciplina da analista: ogni affermazione deve poggiare su una fonte pubblica
citabile. Preferisci un elenco corto e verificato a uno lungo e plausibile.

--------------------------------------------------
CONTESTO OPERATIVO
--------------------------------------------------

Cliente: due residence composti da appartamenti a SAN MAURO MARE (Emilia-Romagna, costa
tra Cesenatico e Rimini), aperti tutto l'anno.

Capienza destinabile al long stay: [N_APPARTAMENTI] appartamenti, [N_POSTI_LETTO] posti letto
complessivi. Tipologie: monolocali (fino a 3 posti), bilocali (fino a 4 posti), trilocali con
due bagni (5-6 posti). Alcuni con vista mare.

Posizionamento economico: canone indicativo 1.100-1.300 EUR al mese per appartamento,
formula tutto incluso (utenze, WiFi, manutenzione), con fattura intestabile a societa'.
Formula contrattuale: ospitalita' temporanea mensile rinnovabile, non locazione.

Questo posizionamento e' un criterio di selezione, non un dettaglio: le organizzazioni che
alloggiano personale con budget molto inferiore (es. 20-30 EUR a notte per operaio) NON sono
prospect e vanno escluse, non valutate con punteggio basso.

OBIETTIVO: individuare organizzazioni che possano generare prenotazioni di 1-8 mesi,
con priorita' assoluta al periodo OTTOBRE-APRILE.

--------------------------------------------------
DIREZIONE DEL FLUSSO — CRITERIO DIRIMENTE
--------------------------------------------------

Interessano ESCLUSIVAMENTE le organizzazioni che portano o attraggono persone NELL'area
della Romagna costiera. Sono di due tipi:

(a) aziende con sede o stabilimento nell'area che RICEVONO personale esterno: fornitori di
    impianti, installatori, auditor, consulenti, formatori, buyer, tecnici di terze parti;

(b) aziende con sede altrove che hanno commesse, cantieri o progetti attivi nell'area e
    devono alloggiare i PROPRI addetti in loco.

Un'azienda che invia il proprio personale FUORI dall'area non e' un prospect, a meno che non
riceva a sua volta personale esterno presso le proprie sedi. Verifica sempre in quale delle
due direzioni si muovono le persone prima di includere un'azienda.

--------------------------------------------------
AREA GEOGRAFICA
--------------------------------------------------

Centro: San Mauro Mare.

Priorita' alta (entro ~30 minuti d'auto):
San Mauro Pascoli, Savignano sul Rubicone, Gatteo, Cesenatico, Bellaria-Igea Marina,
Santarcangelo di Romagna, Rimini, Cesena, Longiano, Gambettola, Villa Verucchio,
zone industriali intermedie.

Priorita' media (30-55 minuti): Forlì, Ravenna, Cervia, Riccione, Morciano.
Ravenna merita attenzione specifica: polo portuale, offshore, oil & gas, cantieristica e
manutenzione industriale, con domanda strutturale di alloggi tecnici di lunga durata.

Distanze maggiori sono accettabili solo quando la permanenza e' lunga, l'azienda fornisce
auto aziendale, o si tratta di squadre.

--------------------------------------------------
SETTORI PRIORITARI
--------------------------------------------------

1. INDUSTRIA E IMPIANTISTICA
   Manifatturiero, automazione, meccanica, packaging, engineering, manutenzione industriale,
   installazione macchinari, commissioning, revamping, facility management.
   Cerca chi RICEVE tecnici di fornitori terzi presso i propri stabilimenti.

2. CANTIERI E INFRASTRUTTURE
   Edilizia, general contractor, infrastrutture, ferrovie, telecomunicazioni e fibra,
   energia, fotovoltaico, utilities, data center, grandi impianti.
   Cerca commesse e cantieri di durata plurimensile ATTIVI O PROGRAMMATI NELL'AREA.

3. NAUTICA, PORTUALE E OFFSHORE
   Cantieristica navale, refitting, marine engineering, shipping, oil & gas, manutenzione
   navale, subappaltatori e tecnici specializzati. Focus su Ravenna, Rimini, Cesenatico.

4. MODA, CALZATURA E LUSSO — DISTRETTO LOCALE
   San Mauro Pascoli, Gatteo e Savignano sul Rubicone ospitano un distretto calzaturiero di
   fascia alta, a pochi chilometri dai residence. Queste aziende ricevono buyer
   internazionali, modellisti, consulenti di prodotto, tecnici e team di campagna vendita
   per periodi che vanno da settimane a mesi. Verifica quali aziende del distretto abbiano
   dimensione e mercato internazionale tali da generare questi flussi.

5. CONSULENZA E SERVIZI PROFESSIONALI
   Consulenza IT, cybersecurity, ERP, system integration, consulenza gestionale, societa'
   di ingegneria, auditing, certificazione. Rilevanti quando il personale viene assegnato
   presso il cliente per progetti pluri-mensili NELL'AREA.

6. FORMAZIONE E TEMPORARY ASSIGNMENT
   Academy aziendali, formazione tecnica prolungata, onboarding, temporary manager,
   dirigenti in attesa di relocation definitiva.

7. SANITA' (priorita' bassa)
   Personale sanitario temporaneo, medici e tecnici con incarichi a termine presso i poli
   ospedalieri dell'area. Includi solo se emerge una capacita' di spesa compatibile con il
   posizionamento dichiarato: il segmento e' spesso gestito da cooperative con budget
   alloggio molto compressi.

--------------------------------------------------
SEGNALI DI DOMANDA DA CERCARE
--------------------------------------------------

Dai valore alle organizzazioni per cui trovi segnali datati e verificabili:

- nuovo stabilimento o ampliamento;
- nuova commessa o appalto aggiudicato;
- cantiere di durata plurimensile;
- installazione impianti, revamping, commissioning, manutenzione straordinaria;
- apertura nuova sede o trasferimento di reparto;
- progetto infrastrutturale programmato;
- assunzione temporanea di numerosi tecnici;
- personale internazionale o proveniente da altre regioni;
- aumento temporaneo della forza lavoro.

SEGNALE PIU' FORTE IN ASSOLUTO — cercalo esplicitamente:
annunci di lavoro pubblicati per posizioni nell'area che offrono ALLOGGIO FORNITO
DALL'AZIENDA. Cerca formulazioni come "alloggio fornito", "vitto e alloggio",
"alloggio a carico azienda", "accommodation provided", "sistemazione garantita",
su portali di lavoro, siti aziendali e annunci di agenzie per il lavoro.
Un'azienda che scrive questo STA GIA' PAGANDO alloggi in questo momento: e' il prospect
piu' qualificato che esista. Riporta il link all'annuncio.

Considera notizie pubblicate negli ultimi 24 mesi e progetti programmati per i prossimi 24.

--------------------------------------------------
REGOLA DI VERIFICABILITA' — BLOCCANTE
--------------------------------------------------

1. Ogni prospect deve avere ALMENO UNA FONTE PUBBLICA con URL e data di pubblicazione.
2. Se non trovi una fonte verificabile del segnale di domanda, NON includere il prospect
   nella lista principale: mettilo in una lista separata "DA VERIFICARE", senza punteggio.
3. Ogni dato non verificato va marcato esplicitamente con [STIMA].
4. NON riportare partite IVA, numeri di telefono diretti o dati che non puoi verificare
   su fonte ufficiale citabile.
5. Verifica che la ragione sociale sia ancora attiva e non sia stata assorbita, fusa o
   rinominata. Segnala i casi dubbi.
6. Se una notizia ha piu' di 24 mesi, indicalo e spiega perche' la ritieni ancora valida.

Se non riesci a raggiungere il numero di prospect richiesto rispettando queste regole,
CONSEGNANE DI MENO. Non compensare con aziende generiche del territorio.

--------------------------------------------------
FILTRO LONG STAY
--------------------------------------------------

Non basta che un'azienda mandi persone in trasferta. Per ogni prospect stima:

"Quanto e' probabile che questa organizzazione debba ospitare una o piu' persone
nell'area per almeno 30 giorni consecutivi?"

A = molto elevato   B = elevato   C = possibile   D = prevalentemente soggiorni brevi

Nella lista principale includi solo A e B. Le C vanno in una lista secondaria.
Le D si escludono.

--------------------------------------------------
VALUTAZIONE
--------------------------------------------------

Per ogni prospect assegna tre valutazioni su scala ALTO / MEDIO / BASSO.
OGNI valutazione deve essere motivata da un fatto verificabile citato, non da
un'impressione generale. Se non hai un fatto, scrivi "non determinabile".

1. POTENZIALE LONG STAY — probabilita' di soggiorni di 1-8 mesi
2. POTENZIALE INVERNALE — probabilita' di permanenze tra ottobre e aprile;
   valuta quanto l'attivita' sia indipendente dalla stagione turistica
3. COMPATIBILITA' ECONOMICA — capacita' e abitudine a sostenere costi di alloggio
   coerenti con un canone di 1.100-1.300 EUR/mese per appartamento

Aggiungi due indicatori:
- VOLUME: quante persone potrebbe dover alloggiare contemporaneamente. Segnala se il
  fabbisogno stimato eccede la capienza disponibile ([N_POSTI_LETTO] posti letto):
  in quel caso il prospect resta interessante solo per una quota del fabbisogno.
- RICORRENZA: si tratta di un'esigenza una tantum o ripetuta nel tempo?

TIER 1 = alto su tutte e tre le valutazioni
TIER 2 = alto su almeno due
TIER 3 = alto su una, medio sulle altre

--------------------------------------------------
ESCLUSIONI
--------------------------------------------------

- turismo, leisure, OTA, portali vacanze;
- soggiorni prevalentemente di 1-7 notti;
- eventi e fiere senza permanenza prolungata;
- aziende senza progetti o presenza verificabile nell'area;
- nomadi digitali a basso budget, studenti;
- agenzie immobiliari generaliste;
- organizzazioni con budget alloggio incompatibile con il posizionamento.

ESCLUSIONE SPECIFICA DA VERIFICARE: segnala se un'azienda dispone gia' di foresteria
propria, alloggi aziendali o convenzioni alberghiere stabili. Molte realta' industriali
strutturate ne hanno: cambia radicalmente la probabilita' di conversione e va indicato
nella colonna note, non nascosto.

--------------------------------------------------
OUTPUT
--------------------------------------------------

Una tabella unica, ordinata per Tier e poi per potenziale invernale, con queste colonne:

azienda | settore | sede | dove opera nell'area | segnale di domanda | fonte (URL + data) |
chi alloggerebbe | durata stimata | n. persone stimato | long stay (A/B/C) | potenziale
invernale | compatibilita' economica | volume | ricorrenza | tier | note

Dopo la tabella, tre viste brevi (solo nomi e una riga di motivazione):

1. MIGLIORI PER IL PERIODO OTTOBRE-APRILE — max 10
2. MIGLIORI PER VOLUME (piu' appartamenti insieme) — max 10
3. MIGLIORI PER RICORRENZA (domanda ripetuta negli anni) — max 10

Infine:
- I 5 settori con maggiore potenziale, con motivazione
- Le 5 aree geografiche o progetti da monitorare nei prossimi 24 mesi
- La lista "DA VERIFICARE" con i prospect scartati per mancanza di fonte
- Cosa NON sei riuscito a determinare e perche'

--------------------------------------------------
OBIETTIVO DI QUALITA'
--------------------------------------------------

Sono preferibili 25-30 prospect con reale probabilita' di soggiorni plurimensili
rispetto a 200 aziende generiche del territorio.

Per ogni Tier 1 deve esistere una ragione concreta, citata e datata per credere che possa
generare domanda di alloggio di medio-lungo periodo NELL'AREA.

Non gonfiare i numeri. Se il mercato reale offre 15 prospect solidi, consegnane 15.
```

---
---

# RUN 2 — Intermediari e piattaforme di corporate housing

```
RUOLO

Agisci come analista di mercato specializzato in corporate housing, relocation, global
mobility e business travel. Ogni affermazione deve poggiare su una fonte pubblica citabile.

--------------------------------------------------
CONTESTO
--------------------------------------------------

Cliente: due residence a SAN MAURO MARE (Emilia-Romagna, costa romagnola), aperti tutto
l'anno, [N_APPARTAMENTI] appartamenti destinabili al long stay, [N_POSTI_LETTO] posti letto.
Canone indicativo 1.100-1.300 EUR/mese per appartamento, tutto incluso, con fattura a
societa'. Formula di ospitalita' temporanea mensile rinnovabile.

Obiettivo: individuare INTERMEDIARI che possano prenotare appartamenti ripetutamente per
conto dei propri clienti, con priorita' al periodo ottobre-aprile.

Il cliente lavora GIA' con Gattinoni Travel Network e Uvet GBT: servono operatori
equivalenti, complementari o concorrenti.

--------------------------------------------------
DUE CATEGORIE DA TENERE SEPARATE
--------------------------------------------------

CATEGORIA A — INTERMEDIARI DA CONTATTARE
Operatori che cercano strutture per conto dei propri clienti aziendali:
corporate housing companies, agenzie di relocation, global mobility providers,
travel management company (TMC), workforce accommodation agencies, temporary housing
companies, agenzie HR e staffing che trasferiscono personale, societa' che gestiscono
trasferte di tecnici e operai.

CATEGORIA B — PIATTAFORME SU CUI CANDIDARSI COME FORNITORE
Marketplace e piattaforme di corporate housing dove una struttura si registra come
supplier e riceve richieste. Non si contattano commercialmente: ci si candida.
Esempi noti da verificare e ampliare: Homelike, Acomodeo, Apartool, e analoghi.

Questa distinzione e' importante: le due categorie richiedono azioni diverse.
Per la categoria B, cerca e riporta: requisiti di ammissione, standard minimi richiesti
alla struttura, modello commissionale, durata minima dei soggiorni gestiti, procedura e
URL della pagina di candidatura fornitori, copertura geografica (verifica se operano in
Italia e specificamente fuori dalle grandi citta').

Seed iniziali da usare come punto di partenza per trovare operatori analoghi:
Gattinoni Travel Network, Uvet GBT, Professional Relo, GSH Global Solutions Hospitality,
All In Solutions, Habitare Service, Rennovo, Apartool, Homelike, Acomodeo.

--------------------------------------------------
CRITERI DI QUALIFICAZIONE
--------------------------------------------------

Un intermediario e' rilevante solo se soddisfa TUTTI questi requisiti. Verificali:

1. tratta soggiorni di durata pari o superiore a 30 giorni;
2. lavora con strutture EXTRA-ALBERGHIERE (appartamenti, serviced apartment, residence),
   non solo con hotel;
3. opera in Italia, e in particolare copre o potrebbe coprire localita' fuori dalle grandi
   aree metropolitane. Un operatore che serve esclusivamente Milano, Roma e Torino centro
   e' poco rilevante: verificalo e segnalalo;
4. ha clienti aziendali con esigenze plausibili in Emilia-Romagna o sulla costa adriatica.

Scarta gli operatori che non soddisfano il punto 2: sono la maggioranza delle TMC
tradizionali e non porterebbero nulla.

--------------------------------------------------
REGOLA DI VERIFICABILITA' — BLOCCANTE
--------------------------------------------------

1. Ogni operatore deve avere sito web attivo verificato, con URL.
2. Verifica che la ragione sociale sia ATTUALE. Molti operatori del settore hanno subito
   fusioni e rebranding (per esempio Carlson Wagonlit e' oggi CWT, HRG e' stata assorbita
   da American Express Global Business Travel). Segnala esplicitamente ogni caso di
   acquisizione, fusione o cambio di denominazione che rilevi, indicando l'entita' attuale.
3. Se non riesci a verificare che un operatore sia attivo, mettilo in una lista separata
   "DA VERIFICARE" senza punteggio.
4. Non riportare partite IVA o dati non verificabili su fonte ufficiale.

--------------------------------------------------
OUTPUT
--------------------------------------------------

DUE TABELLE SEPARATE.

Tabella A — intermediari da contattare:
nome | sede | tipo di operatore | tratta soggiorni 30+ giorni (si'/no/non determinabile) |
lavora con appartamenti (si'/no) | copertura geografica in Italia | tipologia di clienti |
sito | fonte | priorita' (alta/media/bassa) | motivazione

Tabella B — piattaforme su cui candidarsi:
nome | sede | mercati coperti | opera in Italia (si'/no) | requisiti per le strutture |
modello commissionale | durata minima soggiorni | URL pagina candidatura fornitori |
fonte | facilita' di ammissione stimata | note

Infine:
- I 10 operatori con maggiore probabilita' di generare prenotazioni ricorrenti, motivati
- Le 3 piattaforme su cui candidarsi per prime, con la ragione della priorita'
- Lista "DA VERIFICARE"
- Cosa non sei riuscito a determinare e perche'

Preferisci 20 operatori verificati a 60 nomi di settore.
```

---
---

# RUN 3 — Canali di ingresso

> **Da lanciare solo dopo aver letto e filtrato i risultati dei run 1 e 2.**
> Nel prompt, sostituisci l'elenco con i nomi che hai effettivamente selezionato.

```
RUOLO

Agisci come analista di go-to-market B2B. Devi individuare COME si entra in contatto con
le organizzazioni elencate qui sotto, non CHI ci lavora.

--------------------------------------------------
VINCOLO IMPORTANTE
--------------------------------------------------

NON cercare persone fisiche. NON riportare nomi, cognomi, indirizzi email personali o
URL di profili LinkedIn individuali. Non sono verificabili in modo affidabile e sono dati
personali. Se non trovi un dato aziendale pubblico, scrivi "non disponibile": non dedurlo
e non ricostruirlo.

--------------------------------------------------
ORGANIZZAZIONI DA ANALIZZARE
--------------------------------------------------

[INSERIRE QUI L'ELENCO DEI TIER 1 E TIER 2 EMERSI DAI RUN 1 E 2]

--------------------------------------------------
COSA CERCARE PER CIASCUNA
--------------------------------------------------

1. RUOLI DECISIONALI
   Quali 2-3 funzioni aziendali, in un'organizzazione di quel tipo e di quella dimensione,
   decidono o gestiscono l'alloggio di personale esterno o in trasferta.
   Distingui dove possibile tra:
   - chi autorizza la spesa (economic buyer)
   - chi deve materialmente trovare la soluzione (operational buyer)
   Motiva in base alla struttura organizzativa tipica di quel settore, non inventando
   organigrammi specifici.

2. CANALI DI INGRESSO PUBBLICI E VERIFICABILI
   - email aziendali pubblicate sul sito (info@, acquisti@, hr@, fornitori@)
   - centralino
   - esistenza di una pagina "fornitori", "supplier", "diventa partner" o di un form di
     qualifica fornitore, CON URL. Questa e' l'informazione piu' preziosa: e' la porta di
     servizio che quasi nessuno usa
   - eventuale portale acquisti o piattaforma di e-procurement utilizzata

3. ANNUNCI DI LAVORO ATTIVI
   Verifica se l'organizzazione ha pubblicato di recente annunci per posizioni nell'area
   che citano trasferte o alloggio fornito. Riporta il link e la data. E' insieme un
   segnale di domanda e un aggancio commerciale.

4. ARGOMENTO DI APERTURA
   Per ciascuna, una riga: quale problema concreto e documentato le rende utile una
   soluzione di alloggio long stay in zona. Deve derivare da un fatto citato nel run 1,
   non da una formula generica.

--------------------------------------------------
OUTPUT
--------------------------------------------------

Tabella:
organizzazione | ruoli da contattare | canale di ingresso migliore | email/URL verificati |
pagina fornitori (URL o "non trovata") | annunci di lavoro rilevanti | argomento di apertura |
fonte

Chiudi indicando per quali organizzazioni non hai trovato alcun canale pubblico:
richiederanno un approccio diverso.
```

---

## Checklist di validazione dell'output

Prima di usare i risultati, controlla che:

- [ ] ogni riga della lista principale ha **URL e data** nella colonna fonte
- [ ] nessuna partita IVA compare nell'output
- [ ] i prospect senza fonte sono nella lista "DA VERIFICARE" e non tra i Tier
- [ ] per ogni Tier 1 la **direzione del flusso** è corretta: portano persone *nell'area*
- [ ] le ragioni sociali non risultano assorbite, fuse o rinominate
- [ ] compare almeno qualche prospect trovato tramite **annunci con alloggio fornito**
- [ ] il modello ha dichiarato cosa non è riuscito a determinare
- [ ] nessun URL LinkedIn individuale nel run 3

Se il run 1 restituisce 60 prospect tutti in Tier 1, l'output non ha rispettato le regole:
rilancialo insistendo sulla regola di verificabilità.
