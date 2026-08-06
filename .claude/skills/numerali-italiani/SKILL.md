---
name: numerali-italiani
description: >-
  Decodifica il «guasto di numerazione» del repertorio ITALIA NERA (§3.1 del CLAUDE.md) ed
  espande le cifre in parole italiane prima di generare un documento dell'opera. Attivala
  ogni volta che compaiono numerali corrotti (forme come «3150mila», «cento26», «50tré»),
  quando devi scrivere numeri per esteso, o prima di produrre un DOCX dell'opera in cui non
  possono restare cifre arabe. Ricorda la regola ferrea: la seconda classe (invisibile) NON
  è riparabile automaticamente e va letta occorrenza per occorrenza nel contesto.
---

# Numerali italiani — decodifica e scrittura per esteso

Riferimento normativo: `CLAUDE.md` §1 (i numeri si scrivono per esteso in parole italiane,
unica eccezione la citazione diagnostica di una forma corrotta) e §3.1 (il guasto di
numerazione). Foglio del repertorio: `ZZ Residui numerici`.

## Le due classi del guasto

Una corruzione ha sostituito con cifre le parole-numero **dentro** i numerali composti.

### Classe visibile — riparabile
La cifra araba è incastonata in un numerale altrimenti scritto in lettere, quindi è
riconoscibile a vista. Forme note (58 occorrenze censite, 56 decodificate):

| forma corrotta | lettura corretta | valore |
|---|---|---|
| `3150mila` | trecentocinquantamila | 350 000 |
| `cento26` | centoventisei | 126 |
| `50tré` | cinquantatré | 53 |
| `due100.000` | duecentomila | 200 000 |
| `13mila50` | tredicimilacinquanta | 13 050 |
| `MILLEDUECENTO51` | milleduecentocinquantuno | 1 251 |

La regola di decodifica è provata sette volte (quattro riscontri esterni, tre prove
aritmetiche interne). Queste forme si correggono con sicurezza.

### Classe invisibile — NON riparabile automaticamente
La cifra corrotta produce un numero **plausibile**, indistinguibile a occhio da un valore
autentico. Esempi accertati:

- `506` = cinquantasei · `509` = cinquantanove · `505` = cinquantacinque

ma `205`, `208`, `301`, `601`, `904` sono **autentici**.

**Regola ferrea:** nessuno strumento può decidere da solo se un numero a tre o quattro
posizioni appartiene alla classe invisibile. Va letta **ogni occorrenza nel contesto**
(punto 3 della coda di lavoro, §8: «lettura occorrenza per occorrenza delle cifre a 3 e 4
posizioni»). Questo codice non va mai eseguito in blocco su tali cifre per «ripararle».

## Come usare la skill

1. **Forma visibilmente corrotta** → applica la tabella sopra; se la forma è nuova ma dello
   stesso tipo, ricostruisci la parola-numero e registrala anche nel foglio `ZZ Residui
   numerici`, con la prova (riscontro esterno o aritmetico) che ne giustifica la lettura.
2. **Cifra a 3–4 posizioni sospetta** → NON convertire d'ufficio. Segnala l'occorrenza per
   lettura contestuale; decidi solo con un riscontro nel testo o in una fonte.
3. **Preparazione di un documento dell'opera** → dopo aver deciso i valori corretti, espandi
   ogni numero in parole italiane con `numero_in_parole()` (sotto), così che nel DOCX non
   resti alcuna cifra araba (il controllo della skill `docx-italia-nera` deve dare zero).

## Codice — espansione cifre → parole italiane

`scripts/numerali.py` nel repo contiene la funzione autorevole. Testo di riferimento:

```python
# -*- coding: utf-8 -*-
"""Espansione di interi in parole italiane (ortografia standard, 0..999_999_999).
NON usare per «riparare» in blocco la classe invisibile del guasto: quelle cifre
vanno lette occorrenza per occorrenza nel contesto (CLAUDE.md §3.1)."""

_UNITA = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove",
          "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici",
          "diciassette", "diciotto", "diciannove"]
_DECINE = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta",
           "settanta", "ottanta", "novanta"]
# scala per gruppi di mille: singolare (valore == 1) e plurale (valore > 1)
_SING = ["", "mille", "unmilione", "unmiliardo"]
_PLUR = ["", "mila", "milioni", "miliardi"]


def _sotto_cento(x):
    if x < 20:
        return _UNITA[x]
    d, u = divmod(x, 10)
    base = _DECINE[d]
    if u in (1, 8):                 # elisione: ventuno, ventotto, trentuno, trentotto...
        base = base[:-1]
    parola = base + _UNITA[u]
    if u == 3:                      # accento sul «tre» finale: ventitré, cinquantatré
        parola = parola[:-3] + "tré"
    return parola


def _sotto_mille(x):
    c, resto = divmod(x, 100)
    parola = ""
    if c:
        parola = "cento" if c == 1 else _UNITA[c] + "cento"
    if resto:
        coda = _sotto_cento(resto)
        # elisione di «cento» davanti a o- (centotto, centottanta)
        if parola.endswith("cento") and coda[0] == "o":
            parola = parola[:-1]
        parola += coda
    return parola


def numero_in_parole(n):
    if n == 0:
        return "zero"
    if n < 0:
        return "meno " + numero_in_parole(-n)
    gruppi = []
    livello = 0
    while n > 0:
        n, resto = divmod(n, 1000)
        gruppi.append((resto, livello))
        livello += 1
    parti = []
    for valore, liv in reversed(gruppi):
        if valore == 0:
            continue
        if liv == 0:
            parti.append(_sotto_mille(valore))
        elif valore == 1:
            parti.append(_SING[liv])
        else:
            parti.append(_sotto_mille(valore) + _PLUR[liv])
    return "".join(parti)


# prove rapide (le forme note della classe visibile e casi limite)
if __name__ == "__main__":
    attesi = {
        53: "cinquantatré", 126: "centoventisei", 200_000: "duecentomila",
        350_000: "trecentocinquantamila",
        13_050: "tredicimilacinquanta", 1_251: "milleduecentocinquantuno",
        21: "ventuno", 28: "ventotto", 108: "centotto", 180: "centottanta",
        1000: "mille", 2000: "duemila", 1_000_000: "unmilione",
    }
    for n, s in attesi.items():
        got = numero_in_parole(n)
        assert got == s, f"{n}: atteso {s!r}, ottenuto {got!r}"
    print("ok")
```

Nota sull'ambito: la funzione copre `0..999_999_999` con l'ortografia standard italiana
(elisione `ventuno`/`ventotto`, `centotto`/`centottanta`, accento su `-tré`, `mille`/`mila`,
`unmilione`/`unmiliardo`). Per valori oltre il miliardo, estendere `_SING`/`_PLUR`. Verifica
sempre il caso concreto contro il foglio `ZZ Residui numerici` prima di consolidare una
nuova forma.
