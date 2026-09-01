# 📊 Piano di Misurazione GA4 & Integrazione con il Sito Principale
## Progetto: Residence Veliero & Altamarea — Master Landing Page

---

## 1. 🔑 Accesso Google Analytics 4 per gamatig@gmail.com

Per collegare la nuova landing page e monitorare le conversioni direttamente dal tuo account Google, Paolo e Marco Masini (o chi gestisce l'account Google Analytics dell'hotel) devono seguire questi semplici passaggi:

### Procedura di Delega Accesso:
1. Accedere a **[Google Analytics](https://analytics.google.com/)** con l'account proprietario di *Residence Veliero*.
2. In basso a sinistra, cliccare sull'icona dell'ingranaggio **Amministrazione (Admin)**.
3. Nella colonna **Proprietà (Property)**, cliccare su **Gestione degli accessi alla proprietà (Property Access Management)**.
4. In alto a destra, cliccare sul pulsante **+ blu** e selezionare **Aggiungi utenti (Add users)**.
5. Inserire l'indirizzo email: gamatig@gmail.com.
6. Selezionare il ruolo: **Amministratore (Administrator)** o **Editor**.
7. Spuntare la casella *\"Invia notifica via email ai nuovi utenti\"*.
8. Cliccare su **Aggiungi (Add)** in alto a destra.

---

## 2. 🔗 Strategia di Collegamento tra Vecchio Sito e Nuova Landing Page

La nuova Master Landing Page (eliero-corporate-smart-living.html) può essere integrata con il sito attuale esidenceveliero.it attraverso 3 punti di contatto strategici:

`
                  ┌───────────────────────────────────────────────┐
                  │    Sito Principale: residenceveliero.it       │
                  └───────┬───────────────┬───────────────┬───────┘
                          │               │               │
            Top Bar Banner│               │/business      │Footer Link
                          ▼               ▼               ▼
                  ┌───────────────────────────────────────────────┐
                  │   NUOVA MASTER LANDING PAGE LONG-STAY         │
                  │   (/corporate-smart-living o /long-stay)      │
                  └───────────────────────┬───────────────────────┘
                                          │
                        Telemetry & Custom Events
                                          ▼
                  ┌───────────────────────────────────────────────┐
                  │   GOOGLE ANALYTICS 4 (gamatig@gmail.com)      │
                  └───────────────────────────────────────────────┘
`

### Punto A: Sostituzione/Redirect della Sezione /business
* **Perché:** Il sito ha già una pagina esidenceveliero.it/business che intercettava il traffico aziendale. Sostituire il contenuto o impostare un redirect verso la nuova landing page convertirà immediatamente il traffico business organico.

### Punto B: Sticky Top Banner nel Sito Principale (Stagionale Ottobre–Aprile)
* Inserire una barra discreta in cima a tutte le pagine estive:
  > *\"Cerchi un alloggio per trasferte aziendali, cantieri o smart working? Scopri le nostre tariffe mensili all-inclusive. [Scopri di più]\"*

### Punto C: Footer & Menu Principale
* Aggiungere la voce **\"Corporate & Long Stay\"** nel menu di navigazione e nel footer del sito principale.

---

## 3. 🎯 Matrice dei Custom Events GA4 Implementati

La landing page è già telemetrizzata con i seguenti eventi personalizzati:

| Nome Evento GA4 | Trigger | Parametri Rilevati | Obiettivo / KPI |
|---|---|---|---|
| udience_toggle_click | Clic su Switcher Corporate / Smart | selected_mode: corporate / smart | Interesse per target |
| 	co_calculator_cta_click | Clic su \"Blocca Questa Tariffa\" | simulated_people, simulated_months | Intent acquisto da calcolatore |
| adar_filter_click | Filtro sulla Mappa Cantieri SVG | selected_category: cantieri/infrastrutture/orghi | Validazione interesse logistico |
| partment_card_select | Clic su \"Seleziona\" in una card alloggio | partment_type, partment_name | Preferenza tipologia (mono/bilo/suite) |
| generate_lead_rfp_hero | Invio form rapido in Hero | company_name, people_range, expected_duration | **Conversione Primaria B2B** |
| generate_lead_whatsapp_quote | Clic su \"Invia su WhatsApp ai Masini\" | partment_choice, monthly_price_eur | **Conversione Primaria Lead** |
| copy_quote_clipboard | Clic su \"Copia Dettagli Preventivo\" | partment_choice, monthly_price_eur | Intent preventivo offline |
| speedtest_modal_open | Apertura widget Speed Test Fibra | event_category: 	rust_feature | Rassicurazione tecnica |
| partnership_inquiry_open | Clic su \"Diventa Partner Convenzionato\" | channel: intermediaries | Acquisizione canali B2B (GSH/All In) |

---

## 4. 📈 Dashboard di Monitoraggio Consigliata (Funnel di Conversione)

Una volta attivo l'accesso su gamatig@gmail.com, configureremo un report di esplorazione in GA4 con:

1. **Top of Funnel:** Sessioni totali per canale (LinkedIn Outreach, Ricerca Organica, Referral dal vecchio sito, Campagne Google Ads).
2. **Engagement:** % di utenti che utilizzano il calcolatore TCO o interagiscono con la mappa radar cantieri.
3. **Bottom of Funnel (Conversion Rate):** 
   \text{Conversion Rate} = \frac{\text{Lead WhatsApp} + \text{Form RFP Hero}}{\text{Sessioni Totali}} \times 100
   *Target atteso per questa landing:* **> 4.5% - 7.0%** grazie al calcolo immediato del preventivo e al canale diretto WhatsApp.
