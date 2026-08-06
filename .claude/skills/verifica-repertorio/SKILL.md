---
name: verifica-repertorio
description: >-
  Protocollo di verifica di una voce del repertorio ITALIA NERA (§6 del CLAUDE.md). Attivala
  ogni volta che devi verificare una o più voci del repertorio e compilarne l'annotazione,
  chiudere un blocco di verifica, o scrivere un bilancio. Impone la terna di campi (esito,
  data, annotazione), l'ordine dei cinque punti dell'annotazione, la regola per cui non si
  dichiara verificato ciò che non lo è, i gradi del Sistema Savona e i colori di riempimento
  del foglio (verde = confermato, rosso = difetto accertato, giallo = parziale).
---

# Verifica del repertorio — ITALIA NERA

Riferimento normativo: `CLAUDE.md` §6 (protocollo), §2 (Sistema Savona), §3 (difetti noti da
non reintrodurre), §7 (stato) e §8 (coda di lavoro). Repertorio: `repertorio/ITALIA_NERA_REPERTORIO_*.xlsx`.

## La terna di campi (§6)

Per ogni voce si compilano tre campi:

- **esito** — il verdetto della verifica;
- **data** — la data della verifica;
- **annotazione motivata** — il testo che segue l'ordine fisso qui sotto.

## L'annotazione, nell'ordine (§6) — vincolante

1. **Che cosa è confermato**, con la formula esatta della fonte quando è testuale.
2. **Che cosa è errato**, con la correzione.
3. **Che cosa è omesso e disponibile** — i **nomi propri per primi** (§3.2: una voce che
   accerta una condanna senza nominare il condannato non genera un nodo; il reinserimento
   dei nomi ha precedenza, §8 punto 1).
4. **I collegamenti** con altre voci del repertorio.
5. **Che cosa resta da verificare e dove.**

Ogni affermazione dell'annotazione porta inline, in grassetto, il proprio grado Savona
(**A**/**B**/**C**, §2). Un **accertamento negativo** rigorosamente stabilito è un fatto di
grado **A** a pieno titolo e va registrato come tale.

## Regola d'onestà (§6) — vincolante

**Non si scrive «verificato» per ciò che non si è verificato.** Se una tornata chiude due
voci invece delle cinque richieste, **si dichiarano due**. Al termine di ogni blocco si
dichiara quante voci sono state effettivamente chiuse e quante restano (§9).

**Limite dichiarato**, da ripetere in ogni bilancio: il riscontro è su **fonti secondarie
consultabili, non sugli originali**.

## Colori di riempimento del foglio

Nel foglio di verifica del repertorio la cella/riga si colora secondo l'esito:

- **verde** — confermato (voce verificata, nessun difetto);
- **rosso** — difetto accertato (errore di sostanza, omissione, duplicazione, corruzione);
- **giallo** — parziale (verifica avviata ma non conclusa, o riscontro solo su parte della voce).

Il colore va posato solo quando l'esito lo giustifica: il giallo è lo stato onesto di una
voce non ancora chiusa, e non va promosso a verde finché la verifica non è completa.

## Difetti noti da cercare attivamente (§3) — non reintrodurli

- **Guasto di numerazione (§3.1).** Numerali corrotti: classe visibile riparabile, classe
  invisibile (cifre 3-4 posizioni) da leggere occorrenza per occorrenza. Usa la skill
  `numerali-italiani`. Non «riparare» d'ufficio le cifre plausibili.
- **Omissione dei nomi propri (§3.2).** Cerca nelle fonti i nomi taciuti (imputati,
  condannati, magistrati, organi) e reinseriscili: è la precedenza assoluta.
- **Clausola limitativa soppressa (§3.3).** Controlla ogni citazione nella sua **completezza**,
  non solo nella sua esattezza: il repertorio tende a conservare la metà più netta di una
  proposizione e a scartare la clausola che la bilancia nel medesimo atto.
- **Regola dei due atti (§3.4).** Quando due date divergono (pronuncia/deposito,
  approvazione/comunicazione, emissione/notificazione), non si sceglie: si accerta quale
  atto ciascuna registri. Entrambe possono essere vere.

## Come si conduce la verifica (§9, §8)

- Le ricerche si conducono con **`web_search` sequenziali**; non usare ricerca estesa in
  background. Per la verifica di una singola voce è utile delegarla al sottoagente
  **Verificatore di voce**, che tiene fuori dal contesto principale il materiale di ricerca.
- **Scorciatoia per le voci-archivio residue (§8 punto 9).** Non verificare voce per voce:
  collaziona con i tre censimenti già redatti (Rete degli archivi per non dimenticare — guida
  e portale per eventi/persone/processi/documenti/organizzazioni; *Guía de Archivos de Memoria
  y Derechos Humanos en Chile*). Ciò che quegli strumenti recano è già censito; ciò che il
  repertorio reca **in più** va verificato proprio perché lì non compare.
- **Conservazione cumulativa (§2).** L'annotazione si aggiunge, non sostituisce: mai
  abbreviare o riscrivere ciò che c'era. Il versionamento è affidato a git.

## Alla chiusura di un blocco

1. Dichiara quante voci sono state chiuse e quante restano.
2. Aggiorna, se necessario, le sezioni **7** (stato) e **8** (coda) del `CLAUDE.md` — la
   regola del Passo 3 della guida: un `CLAUDE.md` vecchio è peggio di nessuno.
3. Committa con un messaggio che dica **quante voci e quali** (un commit per blocco).
