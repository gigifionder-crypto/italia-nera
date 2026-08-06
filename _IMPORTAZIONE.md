# Importazione — cosa resta da caricare

> File temporaneo di onboarding. Va **rimosso** quando i dati sono in posto e la prima
> tornata di verifica è chiusa.

L'impalcatura del progetto **ITALIA NERA** su Claude Code è montata e collaudata. Sono già
presenti e versionati:

- `CLAUDE.md` (radice) — le istruzioni permanenti, verbatim.
- `.claude/skills/` — le tre skill: `docx-italia-nera`, `verifica-repertorio`, `numerali-italiani`.
- `.claude/agents/` — i due sottoagenti: `verificatore-di-voce`, `lettore-di-fondo`.
- `scripts/` — `numerali.py` (espansione cifre→parole, con self-test) e `genera_docx.py`
  (pipeline DOCX della §5, collaudata: A4, Times New Roman 12pt, giustificato, guardiano
  delle cifre arabe, validazione finale).

## Cosa manca — i dati, da caricare a mano

Non erano trasferibili dalla «project knowledge» di Claude.ai. Vanno messi nelle cartelle
corrispondenti (che per ora contengono solo un `.gitkeep`):

| Da collocare | Destinazione |
|---|---|
| `ITALIA_NERA_REPERTORIO_RIPARATO_E_FOGLIO_DI_VERIFICA.xlsx` | `repertorio/` |
| Registri, monografie, schede, Volume Zero (DOCX) | `corpus/opera/` |
| Bilanci, stati, certificati, note di verifica (DOCX) | `corpus/diagnostica/` |
| PDF, trascrizioni, atti acquisiti da terzi (testo UTF-8, §4) | `fonti/` |

Nota (§4): i file ereditati con estensione `.docx`/`.pdf` sono **testo UTF-8 in chiaro**;
vanno letti con `open(path, encoding='utf-8')`, non con `python-docx` né con un parser PDF.
Il sottoagente `lettore-di-fondo` lo fa già correttamente.

## Due avvertenze d'uso del CLAUDE.md (Passo 3 della guida)

1. **Tienilo aggiornato.** Alla chiusura di ogni blocco di verifica, aggiorna la §7 (stato)
   e la §8 (coda). Un `CLAUDE.md` vecchio è peggio di nessuno.
2. **Non gonfiarlo.** Solo regole stabili; le annotazioni restano nel repertorio, i
   ragionamenti nei documenti.

## Primo comando operativo (dopo aver caricato il repertorio)

> Leggi CLAUDE.md e il foglio `01 Archivi` del repertorio. Dimmi quante voci-archivio
> risultano non ancora verificate e proponimi un ordine di blocchi per completarle,
> distinguendo quelle verificabili per riscontro esterno da quelle che vanno chiuse per
> collazione con i tre censimenti indicati nella sezione 8.
