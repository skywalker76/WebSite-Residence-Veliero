# CLAUDE.md — Residence Veliero & Altamarea (Smart Living)

Landing page e strategia «Smart Living» per il Residence Veliero & Altamarea di San Mauro Mare (titolari Paolo e Marco Masini). Cartella statica HTML/CSS/JS, **repo git locale dal 31/08/2026** (nessun remote; i `.docx` del cliente restano fuori): a fine sessione committare i propri file.

**Fonti di conoscenza, in quest'ordine:**
1. Vault Obsidian `C:\Antigravity\vault\` — memoria condivisa fra i due IDE, versionata con git: `01-Clients/WebSite-Residence-Veliero.md` (**leggere per primo il blocco in testa: dice quale piano vale**), poi l'ultima nota `02-Sessions/*Veliero*` / `*Smart-Living*`, e i dashboard `00-Dashboard/Context-Loader.md` + `Stato-Progetti.md`.
2. `docs/FONTE_01..04` — materiale prodotto dalla proprietà (15/06 e 26/08/2026): per **fatti, vincoli e numeri della struttura** prevalgono su ogni bozza e su ogni analisi.
3. `docs/deep-research-corporate-long-stay.md` (29 prospect ABM con scoring), `docs/ANALISI_GAP_20260826.md`, `docs/ARCHITETTURA_SISTEMA_2026.md`, `docs/ROMAGNA_SMART_VILLAGE_STRATEGIC_PLAN.md`.
4. La memoria persistente di Claude Code — che **Antigravity non vede**: ciò che serve anche all'altro agente va scritto nel vault, nella stessa sessione.

## Il piano che vale (decisione dell'utente del 31/08/2026)

Fa fede la sessione Antigravity del 31/08: **proposta a 3 scenari approvata** — A Smart Worker B2C, B Corporate Workforce B2B, **C ibrido raccomandato** — con **priorità alla landing Corporate Workforce B2B** (cantieri infrastrutturali già attivi in Romagna da settembre 2026: il mercato più promettente è la workforce accommodation, non lo smart worker generico), poi la landing Smart Living B2C come **upgrade della v2** (`veliero-smart-living-landing.html`). Brand estratto dal sito live: `#1875AB` primary, `#F5E082` gold, `#0D5A8A` navy; Raleway + Playfair Display + Montserrat; stile «Riviera Chic & Family Warmth». Le landing si realizzano **dopo le risposte dei Masini** alle 9 domande operative del meeting. Poi la registrazione di `romagnasmartvillage.it`.

Il 27/08 Claude Code aveva registrato una linea diversa (le tre landing HTML come bozze decadute, nessuna pagina prima di sciogliere il nodo prezzo): **superata dalla decisione del 31/08**. Non riproporla.

## Vincoli che restano veri (sono fatti, non piani)

- **Nodo servizio → prezzo ancora aperto**: le fonti descrivono due modelli opposti (servizio minimo a carico dell'ospite vs «Zero Sbatti» tutto incluso) allo stesso prezzo di 1.100–1.300 €. Si chiude al meeting con i Masini; fino ad allora **prezzi e claim in pagina solo se confermati dalla proprietà**.
- **Mai scrivere in pagina dotazioni che non esistono** (`ARCHITETTURA_SISTEMA_2026.md` §8).
- **Foto**: la libreria reale si ferma a 1400×900 e c'è **un solo interno** adatto allo smart working (`interno1.jpg`); `interno2.jpg` contraddice il posizionamento. Non cercare sostituti: non esistono. Il servizio fotografico è un prerequisito del lancio.
- **Scadenza dichiarata**: pronti al primo contatto entro il **30/09/2026**. Le due verifiche a più alto impatto da chiedere alla proprietà: **bollette invernali** e **speed test dell'upload dentro un appartamento**.
- Numeri di mercato e di ricavo (Deep Research, piano RSV): citarli con la fonte, mai arrotondarli verso l'alto.

## Coordinamento con Antigravity

Su questa cartella lavora anche Antigravity/Gemini, che ha scritto tutte le note Veliero nel vault fino al 31/08. Quel giorno i due registri divergevano perché le decisioni del 27/08 stavano solo nella memoria di Claude Code: l'utente ha risolto scegliendo il piano del 31/08. Da qui in poi ogni decisione presa con l'utente va nel vault **nella stessa sessione**. Le regole globali di Antigravity stanno in `~/.gemini/GEMINI.md`; qui non esiste un `GEMINI.md` di progetto.

## Come lavorare con l'utente

Italiano; diretto, con controindicazioni; report punto per punto. Regole trasversali in `~/.claude/CLAUDE.md`. Chiusura sessione: nota in `vault/02-Sessions/`, aggiornamento della scheda cliente e dei due dashboard, poi commit dei propri file nel vault (`git -C C:\Antigravity\vault`) e in questo repo.
