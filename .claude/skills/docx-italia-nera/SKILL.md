---
name: docx-italia-nera
description: >-
  Pipeline di generazione dei documenti dell'opera ITALIA NERA (monografie, schede, registri,
  bilanci) in formato DOCX. Attivala ogni volta che devi produrre o rigenerare un documento
  dell'opera con python-docx. Applica i parametri fissi della §5 del CLAUDE.md (A4, Times New
  Roman 12pt a livello di stile e di run, giustificato, corpo in file *_body.py separato),
  impone i vincoli di lingua e registro della §1, e prima della consegna verifica che non
  restino cifre arabe e che il file sia valido.
---

# Pipeline DOCX — ITALIA NERA

Riferimento normativo: `CLAUDE.md` §5 (parametri fissi), §1 (lingua e registro), §4
(struttura file). I documenti dell'opera vanno in `corpus/opera/` (registri, monografie,
schede, Volume Zero) o `corpus/diagnostica/` (bilanci, stati, certificati, note di verifica).

## Prima di scrivere: vincoli di registro (§1) — valgono per i documenti dell'opera

- Testo **in italiano**, prosa continua e giustificata, registro accademico-narrativo.
- **Vietati:** elenchi puntati, tabelle, sottotitoli interni ai blocchi analitici, linguaggio
  figurato o metaforico, tono didascalico.
- **Nessuna cifra araba nel testo:** i numeri si scrivono per esteso in parole italiane (usa
  la skill `numerali-italiani` / `scripts/numerali.py`). Unica eccezione: la citazione di una
  forma corrotta a scopo diagnostico, che va dichiarata.
- Nomi propri per esteso alla prima occorrenza.
- Ogni **monografia** si chiude con la sezione obbligatoria «Fonti e URL»: elenco a piè di
  pagina di tutti gli URL usati.
- Le affermazioni portano inline, in grassetto, il grado del Sistema Savona (**A**/**B**/**C**,
  §2). Il grassetto inline è reso con la sintassi `**...**` nel testo del corpo.

Nota: questi divieti valgono per i **documenti dell'opera**, non per i file di servizio.

## Architettura a due file (§5)

Il corpo del documento si scrive in un file `*_body.py` **separato**, creato con lo strumento
di scrittura file (**mai con heredoc**: l'heredoc distrugge i diacritici italiani). Uno script
generatore lo importa e costruisce il DOCX.

`corpus/opera/<nome>_body.py` — solo dati, nessuna dipendenza da python-docx:

```python
# -*- coding: utf-8 -*-
TITOLO = "…"
# ogni elemento è un paragrafo di prosa; il grassetto inline usa **...**
PARAGRAFI = [
    "Primo paragrafo… con grado **A** inline…",
    "Secondo paragrafo…",
]
# per una monografia, gli URL della sezione finale «Fonti e URL»
FONTI = [
    "https://…",
]
```

## Parametri fissi del generatore (§5)

- Formato A4: `section.page_width = Cm(21.0)`, `section.page_height = Cm(29.7)`
- Margini: `Cm(2.54)` su tutti i lati
- Times New Roman 12pt, imposto **sia a livello di stile sia a livello di run**, via `w:rFonts`
  con tutti e quattro gli attributi: `ascii`, `hAnsi`, `cs`, `eastAsia`
- Allineamento **giustificato**, rientro prima riga `Cm(0.75)`, interlinea **1.15**,
  `space_before = 0` e `space_after = 0`
- Grassetto inline: dividere la stringa su `**` e applicare il grassetto ai segmenti di
  **indice dispari**
- Zoom: rimuovere gli elementi `w:zoom` esistenti da `doc.settings.element`, poi inserire un
  nuovo `OxmlElement('w:zoom')` con `w:percent="100"` in posizione `insert(0)`

Lo script generatore autorevole è **`scripts/genera_docx.py`** (già presente nel repo,
collaudato): riusabile su ogni `*_body.py`. Uso:

```
python3 scripts/genera_docx.py corpus/opera/<nome>_body.py corpus/opera/<nome>.docx
```

Funzioni chiave (vedi il file per l'implementazione completa):
- `_imposta_rfonts(rpr)` — scrive `w:rFonts` con `ascii`/`hAnsi`/`cs`/`eastAsia` = Times New
  Roman; applicato **sia** all'`rPr` dello stile `Normal` **sia** all'`rPr` di ogni run.
- `_aggiungi_prosa(par, testo)` — divide su `**` e mette in grassetto i segmenti di indice
  dispari (così i gradi Savona **A**/**B**/**C** risultano in grassetto).
- `_paragrafo(doc, testo)` — giustificato, rientro `Cm(0.75)`, interlinea `1.15`, spaziatura
  a zero.
- `_zoom_100(doc)` — rimuove i `w:zoom` esistenti e inserisce `w:percent="100"` a `insert(0)`.
- `_controllo_cifre(paragrafi)` — trova le cifre arabe residue; se presenti, `genera()`
  **si ferma** con errore (a meno di `consenti_cifre=True` per citazioni diagnostiche).
- `genera(body_path, out_path)` — costruisce il documento, aggiunge la sezione «Fonti e URL»
  se il body espone `FONTI`, salva e **riapre** il file per validarlo.

Se il generatore va adattato a un tipo di documento nuovo, si estende questo file senza
alterarne i parametri fissi.

## Controlli obbligatori prima della consegna (§5)

1. **Niente cifre arabe residue** nel testo dell'opera:

   ```python
   import re
   residui = re.findall(r'(?<![A-Za-z])\d+', testo)   # deve essere []
   ```

   Se `residui` non è vuoto, o sono numeri da scrivere per esteso (usa `numerali-italiani`),
   o sono citazioni diagnostiche di forme corrotte, che vanno **dichiarate** come tali.

2. **Validazione del file.** Aprire il DOCX prodotto e verificarne l'integrità:

   ```python
   from docx import Document
   Document(out_path)   # deve aprirsi senza eccezioni
   ```

   Se disponibile, eseguire anche lo script di validazione della skill `docx` pubblica
   (`.../docx/scripts/office/validate.py`), come previsto dalla §5.

3. **Conservazione cumulativa (§2).** Non sovrascrivere una versione precedente cancellandone
   il contenuto: si produce una nuova versione che conserva le precedenti alla lettera. Il
   versionamento è affidato a git (un commit per blocco).
