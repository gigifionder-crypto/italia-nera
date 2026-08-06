# -*- coding: utf-8 -*-
"""Espansione di interi in parole italiane (ortografia standard, 0..999_999_999).

Fa parte della pipeline ITALIA NERA (CLAUDE.md §5, §3.1). Serve a scrivere i numeri
per esteso prima della generazione di un documento dell'opera, dove non possono restare
cifre arabe (§1). NON usare per «riparare» in blocco la classe invisibile del guasto di
numerazione: quelle cifre (3-4 posizioni, valore plausibile) vanno lette occorrenza per
occorrenza nel contesto (§3.1, §8 punto 3)."""

_UNITA = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove",
          "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici",
          "diciassette", "diciotto", "diciannove"]
_DECINE = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta",
           "settanta", "ottanta", "novanta"]
_SING = ["", "mille", "unmilione", "unmiliardo"]
_PLUR = ["", "mila", "milioni", "miliardi"]


def _sotto_cento(x):
    if x < 20:
        return _UNITA[x]
    d, u = divmod(x, 10)
    base = _DECINE[d]
    if u in (1, 8):                 # elisione: ventuno, ventotto, trentuno...
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
        if parola.endswith("cento") and coda[0] == "o":   # centotto, centottanta
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


if __name__ == "__main__":
    attesi = {
        0: "zero", 3: "tre", 16: "sedici", 21: "ventuno", 23: "ventitré",
        28: "ventotto", 53: "cinquantatré", 100: "cento", 108: "centotto",
        126: "centoventisei", 180: "centottanta", 1000: "mille", 2000: "duemila",
        1_251: "milleduecentocinquantuno", 13_050: "tredicimilacinquanta",
        200_000: "duecentomila", 350_000: "trecentocinquantamila",
        1_000_000: "unmilione", 2_000_000: "duemilioni",
    }
    for n, s in sorted(attesi.items()):
        got = numero_in_parole(n)
        assert got == s, f"{n}: atteso {s!r}, ottenuto {got!r}"
    print("ok — {} casi".format(len(attesi)))
