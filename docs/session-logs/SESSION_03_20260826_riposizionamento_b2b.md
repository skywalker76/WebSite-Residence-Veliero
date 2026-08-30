# 📋 Session 03 — 26/27 Agosto 2026
## Riposizionamento sulle fonti cliente e virata B2B

**Conversazione:** acquisizione delle fonti dalla proprietà e ridefinizione delle basi di progetto
**Obiettivo:** sostituire le assunzioni delle bozze con la voce reale dei titolari, e ridisegnare
l'architettura delle landing sul mercato che regge il prezzo richiesto

---

## 🎯 Il cambio di impostazione

Le landing prodotte prima di questa sessione (`veliero-smart-living-landing.html`,
`smart-living.html`, `veliero-smart-living.html`) erano **bozze esplorative pre-cliente**.
Su indicazione esplicita del committente **non sono più la base del lavoro**: restano come
repertorio di componenti riusabili.

La nuova base è il materiale prodotto dalla proprietà: la conversazione strategica del
26 agosto e i tre documenti operativi.

---

## ✅ Lavoro completato

### 1. Acquisizione e messa a fonte del materiale
Salvati in `docs/` come fonti autoritative, con avvertenze d'uso:

| File | Contenuto |
|---|---|
| `FONTE_01_PIANO_STRATEGICO_20260826.md` | Piano strategico — visione, target, pricing, AI indexing |
| `FONTE_02_BRIEFING_DOCUMENT_20260826.md` | Briefing — sintesi della trascrizione, target e requisiti |
| `FONTE_03_AFFITTO_ANNUALE_20260615.md` | Modello contrattuale e costi (15 giugno, estratto da .docx) |
| `FONTE_04_LISTE_RICERCA_20260826.md` | Liste agenzie e aziende del territorio (estratte da .docx) |

### 2. `ANALISI_GAP_20260826.md`
Confronto tra la voce del cliente e il materiale già prodotto. Esito: l'impianto narrativo
regge all'80%, il modello economico va rifatto.

### 3. `ARCHITETTURA_SISTEMA_2026.md`
Architettura del nuovo sistema: tre segmenti, due landing, presidio LinkedIn, requisiti
operativi B2B, sequenza di lavoro, modello contrattuale, nodo del livello di servizio.

---

## 🔍 Scoperte principali

### Il canale B2B è già aperto
Dal prompt di ricerca sulle agenzie, parole della proprietà: *"lavoro già con Gattinoni
Travel Network S.R.L. ... e anche con Uvet GBT S.p.A."*, con partite IVA.
**Non sono prospect, sono relazioni esistenti.** Il primo test di mercato è presentare
l'offerta invernale a loro, non lanciare una campagna.

### Il prezzo di 1.100–1.300 € nasce come filtro anti-morosità
Origine nel documento del 15 giugno: *"Il prezzo deve essere 1.100–1.250 € → seleziona
automaticamente il cliente giusto"*. Il contesto era come evitare chi smette di pagare dal
secondo mese. Non nasce da un'analisi di valore.

### Due modelli opposti allo stesso prezzo — ⚠️ nodo aperto
- **15 giugno:** pulizie, biancheria, lampadine e piccola manutenzione **a carico dell'ospite**
- **26 agosto:** tutto incluso, "Zero Sbatti", chiavi in mano
- **Prezzo identico in entrambi**

Inconciliabili. Il modello di giugno regge a 700–800 € su un altro pubblico; il prezzo
richiesto regge solo con il modello di agosto. **Da decidere prima di scrivere qualunque pagina.**

### Un terzo segmento: le aziende del territorio
Il secondo prompt rivela un mercato distinto — Electrolux, Marcegaglia, Ferretti, Orogel,
Technogym, Amadori, SCM, Maggioli, Focchi, Hera, Teddy, Del Conca — che alloggia tecnici,
installatori e formatori esterni. Trasferte **tutto l'anno, inverno incluso**, con un
vantaggio decisivo: **d'inverno gran parte della ricettività della Riviera è chiusa.**

### Un quarto segmento: staff stagionale delle strutture
Alberghi, ristoranti e stabilimenti che alloggiano il proprio personale. Finestra utile:
**spalle di stagione** (aprile-maggio, settembre-ottobre).

### Homelike e Acomodeo sono distribuzione, non prospecting
Piattaforme di corporate housing su cui candidarsi come struttura fornitrice.
Potenzialmente il canale più rapido: la domanda esiste già.

---

## ⚠️ Rischi rilevati

1. **Promesse non veritiere nelle bozze:** lavastoviglie assenti in tutta la struttura,
   lavanderia a gettoni promessa "senza gettoni", 100/20 Mbps mai misurati.
   Sul B2B una promessa non mantenuta chiude il rapporto.
2. **Contratto da validare legalmente:** clausola sui minori internamente contraddittoria,
   semplificazioni sulle procedure di allontanamento, GDPR sui documenti reddituali.
3. **Liste con entità obsolete:** HRG assorbita da Amex GBT, Carlson Wagonlit → CWT.
4. **Costi operativi non verificati:** stime generate presentate come margine netto,
   in realtà margine di contribuzione.
5. **Conflitto 12 mesi vs. modello ibrido:** l'estate turistica rende più di qualunque
   canone Smart Living. Il modello ibrido batte quello annuale puro.

---

## 📌 Stato tecnico della landing di prova

Verificato sul file: **nessun JSON-LD**, **nessun Open Graph** (LinkedIn è il canale primario
e i link condivisi sono ciechi), **GA4 non installato**, nessun `lang`, nessun multilingua,
8 FAQ. Il calcolatore di risparmio e l'impianto responsive sono invece validi e riusabili.

---

## ⏭️ Prossimi passi

**Non dipendono dai Masini:**
- Piano di misurazione (eventi, conversioni, audience, UTM) — **prima** delle pagine
- Verifica onboarding Homelike e Acomodeo
- Pulizia e verifica delle liste
- Ottimizzazione profilo LinkedIn del titolare

**Dipendono dalla riunione:**
- Livello di servizio (il nodo) → poi il prezzo
- Numero di unità dedicate, ibrido vs 12 mesi
- I 10 requisiti operativi B2B
- I due bloccanti: speed test in appartamento, costo riscaldamento invernale

**Ordine delle pagine:** Corporate **prima** della B2C — canale già aperto, ciclo più corto,
minore sensibilità al prezzo.

---

## 🔑 Accessi

GA4 e Google Ads: **account esistenti lato cliente**, accesso concesso. Da abilitare il
collegamento per l'uso via API. L'integrazione agentica ha senso solo dopo 3–4 settimane
di dati reali.

---

## 🔎 Coda sessione — Prompt di Deep Research per lead generation B2B

Il committente ha sottoposto un prompt di deep research (v1) da lanciare su ChatGPT per
individuare contatti B2B alto-spendenti. Valutato **7,5/10**: impianto strategico valido,
tre difetti che ne compromettevano la resa.

### Difetti rilevati nel v1

1. **Direzione del flusso ambigua** — chiedeva *"aziende che inviano tecnici presso clienti"*,
   ma al Veliero servono le organizzazioni che **portano persone nell'area**, non quelle che
   le mandano fuori. Metà dei risultati sarebbe stata del tipo sbagliato.
2. **LinkedIn contact mapping non eseguibile** — i profili non sono indicizzati in modo
   affidabile; chiedere "TOP 30 persone con URL" garantisce allucinazioni. In più è
   trattamento di dati personali.
3. **Sovraccarico** — 7 priorità settoriali, 4 liste, 9 blocchi executive e scoring a 6
   dimensioni in un solo run: ampiezza a scapito della verifica.

Minori: capienza e prezzo non dichiarati (lo scoring del volume girava a vuoto), regola di
verificabilità non bloccante, `partita_iva` nell'output (campo che un LLM inventa),
distretto calzaturiero locale assente, esclusione foresterie mancante.

### Correzione più preziosa individuata

Il segnale di domanda più forte, assente dal v1: **gli annunci di lavoro che offrono
alloggio fornito** ("vitto e alloggio", "accommodation provided"). Un'azienda che lo scrive
sta già pagando alloggi in questo momento. È pubblico, verificabile e datato.

### Prodotto

| File | Contenuto |
|---|---|
| `docs/PROMPT_DEEP_RESEARCH_v2.md` | Versione corretta commentata, con note di revisione |
| `docs/deep-research/RUN1_aziende.txt` | Aziende che generano domanda long stay nell'area |
| `docs/deep-research/RUN2_intermediari.txt` | Intermediari + piattaforme su cui candidarsi |
| `docs/deep-research/RUN3_canali_ingresso.txt` | Ruoli e canali pubblici sui Tier 1 filtrati |
| `docs/deep-research/GUIDA_LANCIO.md` | Procedura in 10 passi, checklist di validazione |

**Suddiviso in tre run separati**, da lanciare in conversazioni distinte: una deep research
ha budget di ricerca finito, e concentrarlo su un obiettivo per volta è ciò che distingue
30 prospect verificati da 30 plausibili.

### ⚠️ Da fare prima del lancio

Compilare `[N_APPARTAMENTI]` e `[N_POSTI_LETTO]` nei run 1 e 2. **Il dato non esiste né nel
sito né nella knowledge base**: va chiesto ai Masini. Verificato: `index.html` non dichiara
il numero di unità.

### Ritorno atteso oltre alle liste

Se le aziende individuate alloggiano oggi il proprio personale in hotel a 80–120 €/notte,
il canone di 1.100–1.300 €/mese diventa difendibile **con un fatto** invece che con
un'opinione — che è precisamente il nodo aperto con la proprietà.

---

## 📍 Punto di ripresa

**Stato:** basi di progetto consolidate, architettura definita, strumenti di lead generation
pronti al lancio.

**Attesa su due fronti:**
- il committente lancia i tre run di deep research e riporta gli output
- nuove informazioni dai Masini sui tre nodi decisionali

**Alla ripresa, in ordine:**
1. Se ci sono gli output della deep research → incrocio, pulizia liste, file di lavoro
   commerciale, messaggi di primo contatto
2. Se ci sono le decisioni dei Masini → piano di misurazione, poi landing Corporate
3. In assenza di entrambi → piano di misurazione (non dipende da nessuno) e ottimizzazione
   del profilo LinkedIn del titolare
