# CLAUDE.md — Residence Veliero & Altamarea (Smart Living)

Landing page e strategia «Smart Living» per il Residence Veliero & Altamarea di San Mauro Mare (titolari Paolo e Marco Masini). Cartella statica HTML/CSS/JS, **non è un repo git**: nessuna cronologia, ogni sovrascrittura è definitiva. Prima di modificare un file, copiarlo nello scratchpad.

**Fonti di conoscenza, in quest'ordine:**
1. `docs/FONTE_01..04` — materiale prodotto dalla proprietà (26/08/2026 e 15/06/2026). **Prevalgono su tutto il resto.**
2. `docs/ANALISI_GAP_20260826.md` e `docs/ARCHITETTURA_SISTEMA_2026.md` — analisi sulle fonti; le 8 domande aperte ai Masini sono in fondo alla prima.
3. Vault Obsidian `C:\Antigravity\vault\` — memoria condivisa fra i due IDE, versionata con git: `01-Clients/WebSite-Residence-Veliero.md` (**leggere per primo il blocco `[!danger]` in testa**), poi le note `02-Sessions/*Veliero*` e `*Smart-Living*`, e i dashboard `00-Dashboard/Context-Loader.md` + `Stato-Progetti.md`.
4. La memoria persistente di Claude Code — che **Antigravity non vede**: ciò che serve anche all'altro agente va scritto nel vault, nella stessa sessione.

## Regole di questo progetto

- **Le tre landing HTML (`veliero-smart-living-landing.html`, `smart-living.html`, `veliero-smart-living.html`) sono bozze decadute** — decisione del committente del 27/08/2026 — costruite prima di conoscere obiettivi e vincoli dei titolari, con un modello economico (690–890 €) smentito dalle fonti. Da esse si recuperano solo il calcolatore di risparmio, l'impianto responsive mobile-first e la narrativa della giornata-tipo invernale. Il resto si riscrive dalle fonti.
- **Il nodo che decide il prodotto: livello di servizio → prezzo.** Le fonti descrivono due modelli opposti (servizio minimo a carico dell'ospite vs «Zero Sbatti» tutto incluso) **allo stesso prezzo di 1.100–1.300 €**. Non scrivere pagine finché i Masini non hanno scelto: il prezzo discende dalla risposta, non viceversa.
- **Mai scrivere in pagina dotazioni che non esistono** (`ARCHITETTURA_SISTEMA_2026.md` §8).
- **Foto**: la libreria reale si ferma a 1400×900 e c'è **un solo interno** adatto allo smart working (`interno1.jpg`); `interno2.jpg` contraddice il posizionamento. Non cercare sostituti: non esistono. Il servizio fotografico è un prerequisito del lancio.
- **Scadenza dichiarata**: pronti al primo contatto entro il **30/09/2026**. Le due verifiche a più alto impatto da chiedere alla proprietà: **bollette invernali** (pareggio del primo anno) e **speed test dell'upload dentro un appartamento**.
- `STRATEGIA_SMART_LIVING_VELIERO.md` vale come analisi di mercato, **non** come definizione di prodotto e prezzo.
- Prezzi e claim in pagina solo se confermati dalla proprietà.

## Coordinamento con Antigravity

Su questa cartella lavora anche Antigravity/Gemini: fino al 31/08/2026 tutte le note Veliero nel vault sono sue (proposta a 3 scenari, brand estratto dal sito, Deep Research corporate). Il 31/08 il suo registro e quello di Claude Code **non coincidevano** (meeting del 26/08, stato delle landing): la rettifica sta in testa alla scheda cliente nel vault. Nessun `GEMINI.md` esiste qui: Antigravity non ha regole scritte su questo progetto.

## Come lavorare con l'utente

Italiano; diretto, con controindicazioni; report punto per punto. Regole trasversali in `~/.claude/CLAUDE.md`. Chiusura sessione: nota in `vault/02-Sessions/`, aggiornamento della scheda cliente e dei due dashboard, poi `git -C C:\Antigravity\vault add <file miei>` e commit in inglese.
