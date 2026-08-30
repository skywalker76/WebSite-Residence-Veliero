# Guida al lancio della Deep Research — procedura operativa

> **File dei prompt:** `RUN1_aziende.txt`, `RUN2_intermediari.txt`, `RUN3_canali_ingresso.txt`
> in questa stessa cartella. Sono già pronti: si aprono, si seleziona tutto, si copia.

---

## PASSO 0 — Compila i due placeholder (obbligatorio)

In `RUN1_aziende.txt` e `RUN2_intermediari.txt` cerca e sostituisci:

| Segnaposto | Cosa metterci |
|---|---|
| `[N_APPARTAMENTI]` | Numero di unità realmente destinabili al long stay |
| `[N_POSTI_LETTO]` | Capienza complessiva di quelle unità |

Il dato **non è nel sito né nella knowledge base**: va chiesto ai Masini.

Se non ce l'hai ancora, non bloccarti: metti il numero totale delle unità dei due residence
e aggiungi in fondo alla riga `(dato da confermare)`. Serve al modello per capire l'ordine di
grandezza — se un cantiere richiede 40 posti letto e tu ne hai 30, deve saperlo.

**Non lanciare con i segnaposto dentro:** lo scoring del volume girerebbe a vuoto.

---

## PASSO 1 — Apri una conversazione NUOVA e attiva Deep Research

- Una conversazione **vuota**, non una in cui hai già parlato d'altro
- Attiva esplicitamente la modalità **Deep Research** prima di inviare
- Non allegare file, non incollare altro contesto: il prompt è autosufficiente

---

## PASSO 2 — Incolla il RUN 1 e invia

Apri `RUN1_aziende.txt`, seleziona tutto, copia, incolla, invia.

**Non aggiungere nulla** né prima né dopo. Ogni frase in più diluisce le regole.

---

## PASSO 3 — Rispondi alle domande di chiarimento

La deep research quasi sempre pone 2–4 domande prima di partire. È il momento più delicato:
**risposte brevi che rimandano al prompt**, senza aprire direzioni nuove.

| Se ti chiede | Rispondi |
|---|---|
| Italia o anche estero? | *"Aziende italiane con attività verificabile nell'area indicata. Aziende estere solo se hanno commesse o cantieri attivi in quell'area."* |
| Quanti risultati vuoi? | *"25–30 verificati. Se le regole di verificabilità non permettono di arrivarci, consegnane meno."* |
| Che arco temporale? | *"Notizie degli ultimi 24 mesi e progetti programmati per i prossimi 24."* |
| Vuoi includere il settore X? | *"Segui le priorità settoriali indicate nel prompt."* |
| Posso restringere lo scope? | *"Sì sulla quantità, no sulla verificabilità."* |
| Vuoi contatti nominativi? | *"No. Nessuna persona fisica, nessun URL LinkedIn individuale."* |

**Regola d'oro:** non aggiungere requisiti nuovi in questa fase. Se ti viene la tentazione
di specificare qualcosa, annotala e valutala dopo aver visto l'output.

---

## PASSO 4 — Lascialo lavorare

Tipicamente 5–30 minuti. Non interromperlo, non mandare messaggi mentre lavora.

---

## PASSO 5 — Valida PRIMA di usare i risultati

Scorri l'output con questa checklist:

- [ ] ogni riga della lista principale ha **URL e data** nella colonna fonte
- [ ] **nessuna partita IVA** nell'output
- [ ] i prospect senza fonte sono nella lista "DA VERIFICARE", non tra i Tier
- [ ] per ogni Tier 1: le persone vengono **nell'area**, non ne escono
- [ ] nessuna ragione sociale assorbita, fusa o rinominata senza segnalazione
- [ ] compare almeno qualche prospect trovato da **annunci con alloggio fornito**
- [ ] il modello ha dichiarato **cosa non è riuscito a determinare**

### Segnali che l'output è da rilanciare

| Sintomo | Significato |
|---|---|
| 60 prospect tutti in Tier 1 | Le regole non sono state applicate |
| Colonna fonte con "sito aziendale" senza URL | Verificabilità ignorata |
| Aziende che *mandano fuori* i tecnici in Tier 1 | Direzione del flusso sbagliata |
| Nessuna lista "DA VERIFICARE" | Ha incluso tutto senza filtrare |
| Compaiono nomi di persone | Ha ignorato il vincolo |

**Messaggio di correzione da inviare nella stessa conversazione:**

> Rivedi l'output applicando rigorosamente le regole che ti ho dato. Elimina dalla lista
> principale ogni prospect privo di fonte pubblica con URL e data, spostandolo in "DA
> VERIFICARE". Verifica per ciascun Tier 1 la direzione del flusso: devono portare persone
> nell'area, non inviarle fuori. Rimuovi partite IVA e qualsiasi dato non verificabile.
> Consegna meno prospect, non di più.

---

## PASSO 6 — Salva l'output

Salvalo in questa cartella come `OUTPUT_RUN1_[data].md`, incollando la risposta integrale.
Serve per il confronto con i run successivi e per non ripetere il lavoro.

---

## PASSO 7 — RUN 2, in una conversazione NUOVA

Stessa procedura, con `RUN2_intermediari.txt`. **Conversazione separata**, non di seguito
al run 1: il contesto precedente inquinerebbe la ricerca.

Domanda di chiarimento tipica di questo run:

> *"Vuoi che verifichi le condizioni di iscrizione delle piattaforme?"* → **"Sì, è la parte
> più importante: requisiti, commissioni, durata minima e URL della pagina di candidatura."**

Salva come `OUTPUT_RUN2_[data].md`.

---

## PASSO 8 — Filtra a mano, prima del RUN 3

Questo passaggio è tuo, non del modello. Dai due output, scegli **le 15–25 organizzazioni
che vuoi davvero contattare**. Criterio: Tier 1 e Tier 2 con potenziale invernale alto.

Apri `RUN3_canali_ingresso.txt` e sostituisci la riga
`[INSERIRE QUI L'ELENCO DEI TIER 1 E TIER 2 EMERSI DAI RUN 1 E 2]`
con l'elenco che hai scelto, un nome per riga.

**Perché a mano:** far cercare i canali di ingresso per sessanta aziende di cui trenta non
contatterai mai è spreco di budget di ricerca. E il filtro richiede il tuo giudizio
commerciale, non quello del modello.

---

## PASSO 9 — RUN 3, in una conversazione NUOVA

Stessa procedura. Salva come `OUTPUT_RUN3_[data].md`.

---

## PASSO 10 — Dopo

Con i tre output in mano si può:

1. **Incrociare e ripulire** le liste, eliminando i duplicati e le entità dubbie
2. **Costruire il file di lavoro commerciale** — un elenco unico ordinato per priorità, con
   canale di ingresso e argomento di apertura
3. **Scrivere i messaggi di primo contatto**, differenziati per agenzie e aziende
4. **Alimentare la landing Corporate**: i pain point che emergono dai segnali di domanda
   sono il contenuto della pagina, non un'aggiunta

I risultati vanno anche a validare il pricing: se le aziende trovate alloggiano oggi il
proprio personale in hotel a 80–120 € a notte, il canone di 1.100–1.300 € al mese è
difendibile con un fatto, non con un'opinione.

---

## Errori da evitare

| ❌ Non fare | ✅ Fai |
|---|---|
| Lanciare i tre run insieme o di seguito | Tre conversazioni separate |
| Lanciare con i placeholder non compilati | Compila prima, anche con dato da confermare |
| Aggiungere contesto nelle risposte alle domande | Risposte brevi che rimandano al prompt |
| Accettare l'output senza validarlo | Checklist del passo 5 |
| Chiedere "più risultati" se sono pochi | Pochi e verificati è il risultato corretto |
| Far cercare canali per tutti i prospect | Filtra prima, poi lancia il run 3 |
