# ITALIA NERA — istruzioni permanenti di progetto

Opera storico-investigativa di Luigi De Michele sulle reti informali transnazionali
nella storia italiana ed europea dal 1943 a oggi. Sezioni: ITALIA NERA (Italia),
MONDO NERO (dimensione internazionale), STORIA NERA (dimensione pre-1943).

---

## 1. Lingua e registro — vincolanti

- **Tutti i documenti dell'opera sono in italiano.** Nessuna eccezione.
- Registro accademico-narrativo, prosa continua e giustificata.
- **Vietati nei documenti dell'opera:** elenchi puntati, tabelle, sottotitoli interni
  ai blocchi analitici, linguaggio figurato o metaforico, tono didascalico.
- **I numeri si scrivono per esteso in parole italiane** («settantatré», non «73»).
  Unica eccezione ammessa: la citazione di una forma corrotta a scopo diagnostico.
- Nomi propri sempre per esteso alla prima occorrenza.
- Le monografie si chiudono con una sezione obbligatoria «Fonti e URL», in forma
  di elenco a piè di pagina di tutti gli URL usati.

Questi vincoli valgono per i **documenti dell'opera**. Non valgono per note di lavoro,
messaggi in chat, commenti nel codice o file di servizio.

---

## 2. Metodo probatorio — Sistema Savona

Ogni affermazione porta inline, in grassetto, il proprio grado:

- **A** — convergenza di almeno tre fonti indipendenti di natura diversa.
- **B** — due fonti indipendenti, oppure una sola di alta affidabilità.
- **C** — fonte singola o convergenza di indizi circostanziali.

Regole collegate, tutte vincolanti:

- **Indipendenza genealogica.** Un solo evento di sequestro e tutti i suoi derivati
  contano come *una* catena, non come più fonti. Se tre autori rimandano allo stesso
  autore, sono un anello e i suoi derivati.
- **Pollo di Popper.** Vietato organizzare le prove concentricamente attorno a una
  conclusione predeterminata. Il movente non si inferisce dalla condotta convergente
  senza prova documentale diretta.
- **Regola di ferro dei tre piani.** Piano dell'esecutore, piano dell'apparato, piano
  del mandato. Vietato passare dall'occultamento accertato al mandato asserito.
- **Divieto dell'attore monolitico.** Nessuna organizzazione (BR, CIA, P2, servizi)
  può essere trattata come attore unitario.
- **Accertamenti negativi.** L'assenza di prova, quando rigorosamente stabilita, è un
  fatto di grado A a pieno titolo e va registrata come tale.
- **I prodotti del lavoro non sono fonti del lavoro.** I registri, i bilanci e le note
  diagnostiche del corpus non possono essere citati a sostegno delle proprie affermazioni.
- **Effetto lampione.** La densità documentaria misura l'attenzione e l'accessibilità,
  non l'intensità storica.
- **Conservazione cumulativa.** Ogni versione conserva le precedenti alla lettera:
  mai sostituire, abbreviare o riscrivere ciò che c'era.

---

## 3. Difetti noti del repertorio — da non reintrodurre

### 3.1 Guasto di numerazione (due classi)

Una corruzione ha sostituito con cifre le parole-numero **dentro** i numerali composti.

**Classe visibile** (58 occorrenze censite, 56 decodificate):
`3150mila` = trecentocinquantamila · `cento26` = centoventisei · `50tré` = cinquantatré
`due100.000` = duecentomila · `13mila50` = tredicimilacinquanta · `MILLEDUECENTO51` = 1251

**Classe invisibile** (produce numeri plausibili — NON riparabile per regola):
`506` = cinquantasei · `509` = cinquantanove · `505` = cinquantacinque
Ma `205`, `208`, `301`, `601`, `904` sono **autentici**. Va letta ogni occorrenza nel contesto.

La regola di decodifica è provata sette volte (quattro riscontri esterni, tre prove
aritmetiche interne). Vedi il foglio `ZZ Residui numerici` del repertorio.

### 3.2 Omissione dei nomi propri

Oltre 120 nomi disponibili nelle fonti e assenti dalle voci. Il repertorio nomina di
regola le vittime e tace imputati, condannati, magistrati e organi.
**Una voce che accerta una condanna senza nominare il condannato non genera un nodo.**
Al reinserimento dei nomi va data precedenza su ogni altro intervento.

### 3.3 Clausola limitativa soppressa

Il repertorio conserva la metà più netta di una proposizione e scarta la clausola che
la bilancia nel medesimo atto. Accertato tre volte. **Ogni citazione va controllata
nella sua completezza**, non solo nella sua esattezza.

### 3.4 Regola dei due atti

Pronuncia e deposito, approvazione e comunicazione, completamento e pubblicazione,
emissione e notificazione sono **due date entrambe vere**. Quando due date divergono,
non si sceglie: si accerta quale atto ciascuna registri.

---

## 4. Struttura dei file

```
repertorio/          ITALIA_NERA_REPERTORIO_*.xlsx — il repertorio delle fonti
corpus/opera/        registri, monografie, schede, Volume Zero (DOCX)
corpus/diagnostica/  bilanci, stati, certificati, note di verifica (DOCX)
fonti/               PDF, trascrizioni, atti acquisiti da terzi
scripts/             pipeline DOCX/XLSX, decodificatore numerali
```

**I file di progetto ereditati** (già `/mnt/project/`) sono testo UTF-8 in chiaro con
estensione `.docx` o `.pdf`. Vanno letti con `open(path, encoding='utf-8')`,
**non** con `python-docx` né con un parser PDF.

---

## 5. Pipeline DOCX — parametri fissi

Libreria: `python-docx`. Il corpo del documento si scrive con un file `*_body.py`
separato (creato con lo strumento di creazione file, mai con heredoc: l'heredoc
distrugge i diacritici italiani), poi eseguito da uno script generatore.

- Formato A4: `Cm(21.0)` × `Cm(29.7)`
- Margini: `Cm(2.54)` su tutti i lati
- Times New Roman 12pt, imposto **sia a livello di stile sia a livello di run**
  via `w:rFonts` con tutti e quattro gli attributi (`ascii`, `hAnsi`, `cs`, `eastAsia`)
- Allineamento giustificato, rientro prima riga `Cm(0.75)`, interlinea 1.15,
  `space_before` e `space_after` a zero
- Grassetto inline: si divide la stringa su `**` e si applica il grassetto ai
  segmenti di indice dispari
- Zoom: rimuovere gli elementi `w:zoom` esistenti da `doc.settings.element`, poi
  inserire un nuovo `OxmlElement('w:zoom')` con `w:percent="100"` in posizione `insert(0)`

Validazione obbligatoria prima della consegna:
`python3 /mnt/skills/public/docx/scripts/office/validate.py <file>`
(in Claude Code: usare lo script equivalente o un controllo di apertura con python-docx)

Controllo aggiuntivo da eseguire sempre su un documento dell'opera:

```python
import re
# deve restituire zero, salvo citazioni diagnostiche dichiarate
len(re.findall(r'(?<![A-Za-z])\d+', testo))
```

---

## 6. Protocollo di verifica del repertorio

Per ogni voce si compilano tre campi: **esito**, **data**, **annotazione motivata**.

L'annotazione registra, nell'ordine:
1. che cosa è confermato, con la formula esatta della fonte quando è testuale;
2. che cosa è errato, con la correzione;
3. che cosa è omesso e disponibile (nomi propri per primi);
4. i collegamenti con altre voci del repertorio;
5. che cosa resta da verificare e dove.

**Non si scrive «verificato» per ciò che non si è verificato.** Se una tornata chiude
due voci invece delle cinque richieste, si dichiarano due.

Limite dichiarato di tutta la verifica condotta finora: il riscontro è su fonti
secondarie consultabili, non sugli originali. Va ripetuto in ogni bilancio.

---

## 7. Stato al 6 agosto 2026

Repertorio: **303 voci su 8 fogli — 177 verificate, 126 residue.**

| foglio | totale | verificate |
|---|---|---|
| 01 Archivi | 82 | 44 |
| Registro analitico-diagnostico (nuovo) | 60 | — (non soggette a verifica d'archivio) |
| 01B Archivi integrativi | 28 | 28 |
| 02 Fonti seriali | 9 | 8 |
| 03 Atti giudiziari e normativi | 73 | 73 |
| 04 Atti parlamentari | 5 | 4 |
| 05 Bibliografia | 30 | 30 |
| 06 Archivi desecretati | 9 | 9 |
| 07 Archivi sudamericani | 5 | 4 |

*(questa tabella è un file di servizio, non un documento dell'opera: qui le tabelle sono ammesse)*

**Foglio 01 — scissione eseguita (6 agosto 2026).** Il vecchio foglio «01 Archivi» (142
voci) mescolava archivi e note analitiche prodotte dal lavoro. È stato scisso, per
contenuto e con la regola per cui atti giudiziari e norme contano come archivi (fonti
consultabili), in due fogli: **«01 Archivi»** con le **82 voci-archivio** (22 verificate,
**60 da verificare**) e **«Registro analitico-diagnostico»** con le **60 note** (verifiche,
rettifiche, chiusure di discrepanza, censimenti/atlanti/ricostruzioni prodotti dal lavoro),
non soggette a verifica d'archivio. Il nome del nuovo foglio è accorciato a 30 caratteri
per il limite Excel di 31 (intento: «Registro analitico e diagnostico»). Nessun contenuto
perduto; valori e colori conservati; il file pre-scissione resta nella storia git.

### Risultato principale

**Nessun atto inesistente su 303 voci.** Nessuna sentenza inventata, nessuna legge mai
promulgata, nessun archivio mai istituito.

### Regolarità metodologica accertata (15 ordinamenti)

Nessuno degli archivi censiti ha aperto i propri fondi spontaneamente. Le aperture
risultano ottenute per causa giudiziaria (Stati Uniti, Regno Unito), incostituzionalità
e poi scandalo (Ungheria), veto presidenziale superato (Slovacchia), contestazione
pubblica delle cifre (Romania), crollo di regime (Portogallo, Grecia, Cono Sud, blocco
orientale), legge ottenuta dalle organizzazioni delle vittime (Bolivia, Uruguay),
decisione pontificia anticipata (Santa Sede), interruzione materiale di una distruzione
in corso (Germania orientale), divulgazione anonima di provenienza ignota (Uruguay).

**Corollario operativo:** la data di apertura di un archivio è un dato storico e va
registrata accanto al contenuto.

---

## 8. Lavoro in coda, in ordine di precedenza

1. Reinserimento dei nomi propri (condizione di possibilità della rete)
2. Controllo di completezza delle proposizioni citate (non automatizzabile)
3. Lettura occorrenza per occorrenza delle cifre a 3 e 4 posizioni
4. Eliminazione delle 5 duplicazioni accertate (1 interna al foglio 03, 1 interna al
   foglio 01, 3 fra fogli)
5. Compilazione della voce vuota sul processo Bellini (foglio 03)
6. Riallineamento della riga difettosa nel foglio 07
7. Correzione dei 6 errori di sostanza accertati
8. ~~Scissione del foglio 01 in due fogli~~ — **fatto (6 agosto 2026)**: 82 archivi in
   «01 Archivi», 60 note in «Registro analitico-diagnostico» (v. §7)
9. Verifica delle voci-archivio residue del foglio 01 — **in corso**. Fronte italiano
   **completato** (6.8.2026): 22 voci verificate — 20 confermate (verde) più 2 difetti
   (rosso): dominio errato riga 11 (`fontitaliarepubblicana.it` → CNR), duplicato riga 15
   (= riga 14). Restano **38 archivi esteri** (a blocchi per ente: Bundesarchiv/Stasi,
   NARA/TNA anglo-americani, ecc.). Nomi propri recuperati da reinserire (§8 punto 1):
   Salvini, Fioroni, Anselmi, Spadolini, Urso, Bindi, Laganà, i Grande Aracri, Caruso,
   Carboni, Martino, Verdini, Cappellacci
10. Acquisizione delle due opere mancanti: *Lettere dalla prigionia* a cura di Miguel
    Gotor (Einaudi) e l'Edizione nazionale delle opere di Aldo Moro (Università di
    Bologna, 8 volumi in 11 tomi, digitale e gratuita)

### Scorciatoia raccomandata per il punto 9

Non verificare voce per voce. Collazionare con tre censimenti già redatti da personale
archivistico e gratuiti:

- *Guida alle fonti per una storia ancora da scrivere* (Rete degli archivi per non dimenticare)
- il portale della medesima Rete, la cui ricerca è già articolata per **eventi, persone,
  indagini e processi, documenti, organizzazioni** — è una banca dati nodale già costruita
  sul dominio dell'opera
- *Guía de Archivos de Memoria y Derechos Humanos en Chile* (Universidad Alberto Hurtado)

Ciò che quegli strumenti recano è già censito; ciò che il repertorio reca in più va
verificato **proprio perché lì non compare**.

---

## 9. Modo di lavorare

- Un comando di una parola («Continua», «Procedi») autorizza a proseguire senza chiedere
  conferma.
- Errori fonetici da trascrizione vocale si risolvono in silenzio, senza segnalarli.
- Si lavora a blocchi, dichiarando ogni volta quante voci sono state effettivamente
  chiuse e quante restano.
- Le ricerche si conducono con `web_search` sequenziali. Non usare strumenti di ricerca
  estesa in background.
