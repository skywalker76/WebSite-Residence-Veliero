# Architettura del sistema — Residence Veliero Smart Living

> **Versione:** 1.0 — 27 agosto 2026
> **Base autoritativa:** `FONTE_01_PIANO_STRATEGICO_20260826.md`, `FONTE_02_BRIEFING_DOCUMENT_20260826.md`,
> più i tre documenti in `materiale ricevuto da tom/`: i due prompt di ricerca (26 agosto 2026)
> e `affitto annuale tutto compreso — pro e contro` (15 giugno 2026)
> **⚠️ Prima di procedere leggere §9 e §10:** il documento di giugno definisce un modello
> contrattuale utilizzabile ma un livello di servizio **opposto** a quello di agosto, allo stesso prezzo.
> **Status del materiale precedente:** `veliero-smart-living-landing.html`, `smart-living.html`,
> `veliero-smart-living.html` sono **bozze esplorative pre-cliente**. Non sono la base del lavoro.
> Restano come repertorio di componenti riusabili (vedi §7). `STRATEGIA_SMART_LIVING_VELIERO.md`
> resta valido come analisi di mercato, **non** come definizione di prodotto e prezzo.

---

## 1. Il fatto che cambia la sequenza

Dal prompt di ricerca sulle agenzie, parole della proprietà:

> *"lavoro già con Gattinoni Travel Network S.R.L. di Milano P.IVA 02713750137 e anche con Uvet GBT S.p.A. di Milano P.IVA 03227380965"*

**Il canale B2B è già aperto.** Non va conquistato da zero: va strutturato e riempito con l'offerta invernale.

Conseguenze operative:

1. **Il primo test di mercato non è una campagna.** È presentare l'offerta Smart Living invernale ai due partner esistenti e misurare la reazione. Costo zero, tempo di risposta giorni, e valida (o smonta) il pricing prima di spendere in Ads.
2. **La prova sociale più forte della landing B2B esiste già** — se autorizzati a nominarli, o quantomeno a scrivere "partner di primari network di business travel italiani".
3. **Le condizioni contrattuali sono già state negoziate almeno una volta.** Sappiamo quindi che la struttura è in grado di lavorare con una TMC: fatturazione, condizioni, tempi di pagamento. Va solo verificato a quali condizioni.

---

## 2. I tre segmenti

| | **A — Smart Worker** | **B — Agenzie / TMC** | **C — Aziende del territorio** |
|---|---|---|---|
| **Chi è** | Professionista full remote, 30–45, Milano / Bologna / Roma | Corporate housing, business travel, relocation: Gattinoni, Uvet, Cisalpina, BCD, CWT | Aziende Rimini / Cesena / Forlì con >15 dipendenti: Electrolux, Marcegaglia, Ferretti, Orogel |
| **Chi paga** | La persona | Il cliente finale, tramite agenzia | L'azienda |
| **Confronta con** | Affitto in città (~1.607 €/mese tutto compreso) | Il proprio portafoglio strutture | Hotel, 80–120 €/notte |
| **Motivazione** | Emozionale: cambio vita, tempo, potere d'acquisto | Operativa: margine, disponibilità, affidabilità | Economica: costa meno dell'hotel, ha la cucina, si fattura |
| **Durata tipica** | 1–6 mesi | Variabile, ricorrente | 1–4 mesi, ricorrente |
| **Stagionalità** | Ott–mag | Tutto l'anno | **Tutto l'anno, inverno incluso** |
| **Ciclo di vendita** | Settimane, decisione emotiva | Mesi, contrattuale | Giorni, decisione operativa |
| **Canale** | Google Ads intento + SEO + landing | LinkedIn + rapporto diretto | Outbound email/telefono, LinkedIn per trovare il nome |
| **Sensibilità al prezzo** | Alta | Media | **Bassa** (il metro è l'hotel) |

### Il vantaggio competitivo che vale per B e C: l'inverno vuoto

D'inverno la maggior parte dell'offerta ricettiva della Riviera **è chiusa**. Un tecnico in trasferta di due mesi a Rimini o Cesena a gennaio ha pochissime alternative aperte, e quasi nessuna con cucina e lavanderia.

Questo capovolge il problema storico della struttura: **la stagione morta è morta per i turisti, non per chi lavora**. È l'argomento centrale della pagina Corporate.

### Nota sulle distanze (da usare, con onestà)

| Da San Mauro Mare a | Tempo auto |
|---|---|
| Rimini | ~20 min |
| Cesena | ~25 min |
| Santarcangelo | ~15 min |
| Forlì | ~35 min |
| Bologna | ~55 min |

Il segmento C funziona bene su Rimini, Cesena, Santarcangelo, Savignano; è più debole su Forlì. Le distanze vanno **verificate e dichiarate in pagina**: un ufficio acquisti le controlla in dieci secondi su Maps, e un dato gonfiato costa la credibilità dell'intera pagina.

### Segmenti esclusi in Fase 1

- **Pensionati** — mescolarli con lo smart working distrugge il posizionamento premium di entrambi. Eventuale pagina separata in Fase 3.
- **Nomadi digitali stranieri / est-europei** — Fase 2, con le versioni EN/DE.

---

## 3. Il sistema di pagine

**Due landing in Fase 1.** Non tre: si parte con due percorsi misurati e si separa quando i dati lo giustificano.

```
Sito attuale (index.html)  ──────────  invariato, resta turistico-famiglie
        │
        ├── /smart-living          →  LANDING 1 — Smart Worker (B2C)
        │
        └── /corporate             →  LANDING 2 — Corporate (B2B)
                                        ├── percorso "Sono un'agenzia"
                                        └── percorso "Sono un'azienda"
```

Il sito esistente **non si tocca**: è un vincolo esplicito della proprietà. Le landing vivono su URL separati, il che protegge anche la percezione del prezzo estivo (nessun turista deve vedere un canone mensile e chiedersi perché a luglio paga altro).

---

### 3.1 LANDING 1 — Smart Worker (B2C)

**Promessa:** non un alloggio più economico, ma **la stessa vita a un costo che ti restituisce tempo e potere d'acquisto**.

**Gerarchia dei messaggi:**

1. **Hero** — il gancio del cambio vita, non il prezzo. Il prezzo compare dopo la promessa, mai prima.
2. **Il confronto** — quanto costa davvero vivere a Milano contro San Mauro Mare, con le voci che nessuno conta: condominio, utenze, pulizie, parcheggio, mezzi.
3. **Il calcolatore** — interattivo, con i numeri dell'utente, non i nostri. *(componente già esistente, da ritarare)*
4. **La postazione** — è il prodotto. Connessione dichiarata con numeri veri, scrivania, sedia, ridondanza di rete.
5. **La giornata-tipo invernale** — smonta il pregiudizio della "Riviera morta". *(componente già scritto, da riusare)*
6. **Il territorio** — Santarcangelo, Parco del Mare, ristorazione, servizi, distanze reali.
7. **Formule e prezzi** — tutto incluso senza asterischi.
8. **FAQ estese** — 20–25 domande, con dati strutturati.
9. **Contatto** — WhatsApp come canale primario.

**Tono:** narrativo, concreto, prima persona. Zero linguaggio da brochure turistica.

---

### 3.2 LANDING 2 — Corporate (B2B)

**Promessa:** **alloggio operativo aperto tutto l'anno, a venti minuti dagli stabilimenti, fatturabile, a metà del costo di un hotel.**

Struttura a clessidra: apertura comune → due bracci → nucleo comune → due CTA distinte.

**Apertura (comune)**
- Headline sul problema reale: personale da alloggiare per settimane o mesi, in un territorio che d'inverno chiude.
- **Due porte esplicite:** `Sono un'agenzia` / `Sono un'azienda`. Ancore interne, entrambe tracciate.

**Braccio B — Agenzie / TMC**

Cosa vuole leggere chi lavora in una TMC, nell'ordine:

1. Tipologie, capienza, numero di unità disponibili per periodo
2. **Tariffe nette e trattamento commissionabile**
3. **Allotment e disponibilità garantita** su finestre concordate
4. Contratto quadro, condizioni di cancellazione, termini di pagamento
5. **Cambio ospite senza rinegoziazione** — requisito determinante
6. Referente unico con tempo di risposta dichiarato
7. Scheda struttura scaricabile (PDF, dati tecnici, foto, planimetrie)

**Braccio C — Aziende del territorio**

1. **Minuti dallo stabilimento** — tabella distanze verificate
2. **Confronto costo:** hotel a 80–120 €/notte contro canone mensile, calcolato su un tecnico per 60 giorni
3. Cucina, lavanderia, spazio vero: perché un tecnico in trasferta lunga sta meglio che in albergo
4. **Aperto tutto l'anno**, quando il resto della Riviera è chiuso
5. Fatturazione elettronica, intestazione a società, gestione ordini/CIG se serve
6. Flessibilità sulle date, più persone contemporaneamente, appartamenti adiacenti
7. Referente unico

**Nucleo comune**
- La struttura: unità, dotazioni, standard, foto reali
- **Connessione**: numeri misurati, non aggettivi
- Chi siamo e chi risponde al telefono
- Partner esistenti (Gattinoni, Uvet — **solo se autorizzati per iscritto**)
- FAQ B2B con dati strutturati

**CTA**
- Braccio B: *"Richiedi il contratto quadro e le tariffe nette"* → form + email dedicata
- Braccio C: *"Verifica disponibilità per il tuo personale"* → form + WhatsApp + telefono
- Due destinazioni distinte, due eventi GA4 distinti. È così che in quattro settimane sappiamo quale braccio merita una pagina propria.

**Tono:** asciutto, informativo, verificabile. Nessuna emozione: qui l'emozione è un costo cognitivo. Numeri, condizioni, tempi di risposta.

---

## 4. Presidio LinkedIn

### Il principio

Una pagina aziendale nuova ha reach organica prossima allo zero. Serve come **vetrina di credibilità** e come requisito tecnico per le Ads, ma non genera contatti. Chi risponde a un messaggio risponde **a una persona**.

Il presidio si costruisce quindi su **un profilo personale di un titolare**, con la pagina aziendale a supporto. È l'applicazione del modello "Enrico" descritto nelle fonti: autorità percepita di una persona reale, non di un logo.

### 4.1 Profilo personale del titolare

| Elemento | Impostazione |
|---|---|
| **Headline** | Non "Titolare Residence Veliero". Qualcosa come: *"Alloggi corporate e long stay in Riviera Romagnola — aperti 12 mesi l'anno per aziende e agenzie"*. La headline è il vero motore di ricerca di LinkedIn |
| **Immagine di copertina** | Foto reale della struttura, non stock |
| **Sezione "Informazioni"** | Il problema che risolve, non la storia dell'azienda. Prime due righe decisive: sono le uniche visibili senza clic |
| **In evidenza** | Link diretto alla landing Corporate + scheda struttura PDF |
| **Esperienze** | Voce dedicata al progetto Smart Living, con parole chiave: corporate housing, long stay, business travel, relocation |
| **Contatti** | Email e telefono visibili |

### 4.2 Pagina aziendale

Vetrina + requisito per le Ads. Post ripresi dal profilo personale, non contenuti originali separati: non c'è capacità produttiva per due flussi editoriali.

### 4.3 Chi targettare

| Braccio | Job title | Strumento |
|---|---|---|
| **Agenzie / TMC** | Corporate Account Manager, Hotel Program Manager, Sourcing Manager, Operations Manager business travel, Business Travel Consultant | LinkedIn diretto + Sales Navigator |
| **Aziende territorio** | HR Manager, Facility Manager, Mobility/Travel Manager, Ufficio Acquisti / Procurement, Responsabile Assistenza Tecnica | **Sales Navigator per trovare il nome**, poi email o telefono |

**Distinzione operativa importante:** per le aziende romagnole LinkedIn è uno strumento di *ricerca del nominativo*, non un canale di chiusura. Un ufficio acquisti si chiude al telefono. Investire in messaggistica LinkedIn verso quel segmento è tempo sprecato.

### 4.4 Sequenza di contatto (braccio agenzie)

1. Connessione senza messaggio, con profilo già ottimizzato
2. Dopo l'accettazione: messaggio breve, concreto, una sola domanda — mai un pitch
3. Se risponde: scheda struttura + proposta di call
4. Follow-up unico a 10 giorni, poi stop

Contenuto in parallelo: 1–2 post a settimana dal profilo personale, sui temi che il target riconosce — l'inverno vuoto della Riviera, il costo reale di un tecnico in hotel per 60 giorni, cosa chiede davvero chi alloggia personale in trasferta.

---

## 5. Requisiti operativi B2B da far confermare ai Masini

Il B2B non si vende con una pagina: si vende con **condizioni**. Queste vanno decise prima di scrivere una riga della landing Corporate, perché sono il contenuto della pagina.

1. **Fatturazione elettronica** a società e partita IVA — confermata dal commercialista?
2. **Termini di pagamento**: si accetta il pagamento a 30/60 giorni tipico corporate, o si pretende l'anticipo?
3. **Cambio ospite** in corso di contratto senza rinegoziazione: accettabile?
4. **Allotment**: quante unità si è disposti a bloccare per un'agenzia, e su quali finestre?
5. **Tariffe nette / commissionabili**: quale struttura di margine si lascia all'intermediario?
6. **Tempo di risposta dichiarato** a una richiesta di disponibilità: 24 ore? 4 ore?
7. **Chi è il referente unico** e su quali orari.
8. **Check-in fuori orario** — un tecnico arriva alle 22:00 di domenica. Si gestisce?
9. **Estate**: il segmento C ha bisogno anche a luglio. Si tiene qualche unità fuori dal circuito turistico o si dice no?
10. **Autorizzazione a nominare Gattinoni e Uvet** in pagina.

---

## 6. Sequenza di lavoro

| # | Attività | Dipende da |
|---|---|---|
| 1 | Verifica dei due bloccanti: **speed test in appartamento** e **costo/efficacia riscaldamento invernale** | Masini |
| 2 | Decisioni su prezzo, numero di unità dedicate, modello ibrido vs 12 mesi | Riunione |
| 3 | Risposte ai 10 requisiti operativi B2B (§5) | Riunione |
| 4 | **Piano di misurazione** — eventi, conversioni, audience, UTM | Nulla: si fa subito |
| 5 | Ottimizzazione profilo LinkedIn del titolare | Nulla: si fa subito |
| 6 | **Test sui partner esistenti** — offerta invernale a Gattinoni e Uvet | Punti 2 e 3 |
| 7 | Verifica delle liste generate (entità obsolete) | Ricerca in corso |
| 8 | Landing Corporate | Punti 1, 2, 3, 4 |
| 9 | Landing Smart Worker | Punti 1, 2, 4 |
| 10 | Installazione GA4 + collegamento API | Punto 4 |
| 11 | Campagne Google Ads (intento) + LinkedIn Ads (identità) | Pagine online |
| 12 | Integrazione agentica API GA4 + Google Ads | 3–4 settimane di dati |

**La landing Corporate precede quella B2C.** Motivo: il canale è già aperto, il ciclo di vendita è più corto, la sensibilità al prezzo è minore ed è il segmento che rende difendibile il pricing richiesto dalla proprietà.

---

## 7. Componenti riusabili dalle bozze

Le bozze non sono la base, ma tre parti sono lavoro valido da non rifare:

| Componente | Dove | Uso |
|---|---|---|
| **Calcolatore di risparmio** | `veliero-smart-living-landing.html` §`#calcolo` | Landing B2C, ritarato sui nuovi prezzi. La logica delle voci nascoste (condominio, trasporti, pulizie) è corretta |
| **Impianto responsive mobile-first** | stesso file | Base tecnica per entrambe le pagine |
| **Narrativa della giornata-tipo invernale** | §`#giornata` | Landing B2C, sezione 5. Smonta il pregiudizio della Riviera chiusa |

Tutto il resto — prezzi, promesse di dotazione, struttura dell'offerta — **si riscrive dalle fonti del 26 agosto**.

---

## 8. Vincolo di verità

Regola non negoziabile per entrambe le pagine: **non si scrive una dotazione che non esiste**.

Oggi la landing di prova promette lavastoviglie assenti, lavanderia senza gettoni che è a gettoni, e 100/20 Mbps mai misurati. Sul B2C produce recensioni negative. Sul B2B produce qualcosa di peggio: un'agenzia che verifica una promessa non mantenuta **chiude il rapporto e non lo riapre**, e Gattinoni e Uvet sono relazioni esistenti da proteggere.

O si compra la dotazione, o non si scrive.

---

## 9. Il modello contrattuale (dal documento del 15 giugno 2026)

La proprietà ha già progettato l'impianto contrattuale, nato da una preoccupazione precisa e legittima: **come evitare chi entra e smette di pagare dal secondo mese**.

### L'impianto

| Elemento | Impostazione |
|---|---|
| **Natura del rapporto** | Contratto di **ospitalità temporanea**, non locazione |
| **Inquadramento** | Struttura ricettiva **D/2** — nessun rilascio di residenza |
| **Durata** | **30 giorni rinnovabili**, rinnovo solo previo pagamento |
| **Pagamento** | **Anticipato**, prima dell'ingresso. Nessun acconto, nessun posticipato |
| **Cauzione** | 300 € |
| **Mancato pagamento** | Non si rinnova il soggiorno: alla scadenza l'ospite non è più tale |
| **Verifiche in ingresso** | Documento, busta paga o contratto di lavoro o partita IVA, lettera dell'azienda |

### Perché è un asset, non solo una difesa

Questo impianto **è un argomento di vendita**, soprattutto sul B2B — a patto di raccontarlo dal lato del cliente e non dal lato del rischio.

| Formulazione difensiva (interna) | Formulazione commerciale (in pagina) |
|---|---|
| "Contratto di ospitalità così non maturano diritti" | **"Formula mensile rinnovabile. Nessun contratto di locazione, nessuna burocrazia."** |
| "Pagamento anticipato per non farsi fregare" | **"Prezzo fisso tutto incluso, pagamento mensile. Nessun conguaglio, nessuna sorpresa."** |
| "30 giorni così posso non rinnovare" | **"Si prolunga di mese in mese, si esce con trenta giorni. Nessun vincolo di durata."** |
| "Chiedo la busta paga per filtrare" | **"Struttura riservata a professionisti e aziende."** |

Per una TMC o un ufficio acquisti, la flessibilità mensile senza vincolo di locazione **è esattamente ciò che cercano**: è il motivo per cui esiste il corporate housing. La clausola difensiva e il beneficio commerciale sono la stessa frase, letta dai due lati.

### ⚠️ Da far validare da un legale prima di ogni uso

Il testo del contratto è stato generato da un assistente AI e contiene almeno tre punti da verificare con un avvocato del settore ricettivo:

1. **Clausola sui minori** — il punto 7 vieta *"di introdurre minori senza autorizzazione della struttura"*, mentre lo stesso documento afferma poche righe sopra che escludere i minori è illegale. Contraddizione interna, e rischio concreto di discriminazione familiare se pubblicata.
2. **"Non esiste occupazione abusiva, non serve sfratto né giudice"** — è una semplificazione. Anche in struttura ricettiva, l'allontanamento di un ospite che rifiuti di uscire non è automatico né immediato.
3. **Richiesta di busta paga e documenti reddituali** — prassi commerciale lecita, ma da gestire in conformità GDPR: finalità dichiarata, minimizzazione, tempi di conservazione.

Analogamente, i **costi operativi** riportati nel documento (160–320 €/mese per bilocale, "margine netto" 780–1.020 €) sono stime generate, non contabilità reale, e non includono ammortamento, imposte, gestione, marketing e sfitto: sono margine di contribuzione, non utile. Vanno confrontati con le bollette effettive prima di comparire in qualunque business case.

---

## 10. Il nodo da sciogliere: due modelli opposti allo stesso prezzo

Confronto diretto tra il documento del 15 giugno e le fonti del 26 agosto.

| Voce | **15 giugno** | **26 agosto** |
|---|---|---|
| Pulizie | A carico dell'ospite | Incluse |
| Cambio biancheria | *"non esistono"* | Incluso |
| Lampadine, piccole rotture | A carico dell'ospite | — |
| Manutenzione | Solo impianti principali | Caldaia, rubinetteria incluse |
| Filosofia | **Difensiva, servizio minimo** | **"Zero Sbatti", chiavi in mano** |
| Target implicito | Lavoratori stagionali, persone in transizione | Smart worker e manager alto-spendenti |
| **Prezzo** | **1.100–1.250 €** | **1.100–1.300 €** |

**Il prezzo è identico, il prodotto no.** Le due impostazioni non sono conciliabili: chi paga 1.250 € al mese confrontando con un affitto milanese non si compra le lampadine e non si pulisce l'appartamento. Il modello di giugno regge a 700–800 € su un pubblico diverso; il prezzo richiesto regge solo con il modello di agosto.

**Va deciso prima di scrivere qualunque pagina, perché determina il prodotto.** La formulazione da portare in riunione:

> *A 1.100–1.300 € il cliente si aspetta un servizio alberghiero con l'autonomia di un appartamento. Il modello "l'ospite si gestisce tutto" funziona, ma a 700–800 € e con un altro pubblico. Quale dei due vogliamo?*

### Il punto di equilibrio raccomandato

Servizio incluso su ciò che ha **alto valore percepito e basso costo marginale**, escluso su ciò che è oneroso e poco visibile:

| Incluso nel canone | Escluso / a richiesta |
|---|---|
| Utenze flat, TARI, WiFi | Pulizie extra oltre la frequenza inclusa |
| **Pulizia ogni 15 giorni** (25–30 € a intervento) | Cambio biancheria settimanale |
| **Cambio biancheria mensile** | Stireria |
| Manutenzione impianti **e** piccola manutenzione (lampadine, rubinetteria) | Danni imputabili all'ospite → cauzione |
| Lavanderia comune senza gettoni | — |
| Assistenza con referente e tempo di risposta dichiarato | — |

Costo aggiuntivo stimato rispetto al modello di giugno: **60–80 €/mese per appartamento**. Su un canone di 1.150 € incide meno del 7% ed è ciò che rende il prezzo difendibile. Toglierlo per risparmiare 70 € significa non poter chiedere 1.150 €.

---

## 11. Quarto segmento: personale stagionale delle strutture della Riviera

Emerso dagli annunci del documento di giugno: *"Alloggi per Personale Stagionale — perfetto per hotel, ristoranti, stabilimenti"*.

| | |
|---|---|
| **Chi è** | Alberghi, ristoranti, stabilimenti balneari che devono alloggiare il proprio staff stagionale |
| **Perché funziona** | Fattura, volumi, ricorrenza annuale, ciclo di vendita brevissimo, cliente locale |
| **Perché è delicato** | In alta stagione compete direttamente con il turismo, che rende di più |
| **Finestra giusta** | **Spalle di stagione — aprile-maggio e settembre-ottobre**, quando le unità rendono poco e lo staff stagionale è già o ancora sul posto |

Non merita una landing dedicata in Fase 1: si serve con l'outbound diretto e un blocco nella pagina Corporate, braccio "aziende".

---

## 12. Canale da verificare subito: le piattaforme di corporate housing

Nella coda dell'elenco agenzie compaiono **Homelike** (Colonia) e **Acomodeo** (Francoforte). Non sono agenzie da contattare commercialmente: sono **piattaforme di corporate housing su cui una struttura si candida come fornitore**.

Se le condizioni di onboarding sono accessibili, è **distribuzione, non prospecting** — potenzialmente il canale più rapido di tutti, perché la domanda è già lì e non va costruita.

**Azione:** verificare requisiti di ammissione, commissioni, standard minimi richiesti e durata minima dei soggiorni per Homelike e Acomodeo. Da fare in parallelo, non dopo le landing.

Nota di verifica sulle liste: gli elenchi sono generati da un LLM e contengono entità non più attive con quella ragione sociale (**HRG** assorbita da American Express GBT, **Carlson Wagonlit** ridenominata **CWT**), oltre a società con vicende societarie recenti. Vanno verificate una per una prima dell'outbound.
