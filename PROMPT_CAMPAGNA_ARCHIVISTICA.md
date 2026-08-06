# PROMPT PER CLAUDE CODE — Campagna archivistica ITALIA NERA

> **Avvertenza sulla premessa, da leggere prima di usare il prompt.**
> I documenti prodotti nella sessione del cinque e sei agosto duemilaventisei **non
> contengono URL**: nessuna delle centosettantanove annotazioni di verifica, e nessuno
> dei documenti generati, reca collegamenti a piè di pagina. La convenzione «Fonti e URL»
> appartiene alle monografie prodotte in sessioni anteriori, non a questa.
> Ciò che quelle annotazioni recano — e che vale molto di più di un elenco di collegamenti —
> sono **gli estremi identificativi completi di ciascun archivio**: denominazione ufficiale,
> sede, base normativa, consistenza, procedura d'accesso e limiti dichiarati. Sono riportati
> qui sotto.
> Gli URL veri del corpus esistono, ma stanno **nei documenti di progetto**: novecentodieci
> collegamenti distinti su quattrocentosessantanove domini, distribuiti in trenta file.
> La Fase Zero del prompt li fa raccogliere a Claude Code direttamente dalle fonti, che è
> il solo modo corretto di ottenerli.

---

## PROMPT DA INCOLLARE

Sei l'assistente di ricerca del progetto ITALIA NERA. Leggi `CLAUDE.md` prima di
qualunque operazione: ne governano lingua, registro, metodo probatorio e vincoli di
formato. Il compito di oggi è la **campagna archivistica**: costruire il quadro operativo
completo delle sedi da consultare e delle vie d'accesso disponibili.

Procedi in cinque fasi. Al termine di ciascuna, fermati e dichiara che cosa hai prodotto
e che cosa resta.

---

### FASE ZERO — raccolta degli URL dal corpus

Nel corpus esistono novecentodieci URL distinti su quattrocentosessantanove domini,
distribuiti in trenta file. Non sono censiti da nessuna parte. Raccoglili tu.

Scrivi ed esegui uno script che:

1. percorra `fonti/` e `corpus/`, leggendo i file di testo con
   `open(path, encoding='utf-8', errors='ignore')` — **i .docx del corpus ereditato sono
   testo semplice con estensione impropria, non aprirli con python-docx**; per i .docx veri
   usa python-docx; salta i PDF in questa passata;
2. estragga ogni URL con `re.compile(r'https?://[^\s,;)\]<>"]+')`;
3. escluda i falsi positivi tecnici, in particolare `schemas.openxmlformats.org` e gli altri
   namespace XML;
4. per ciascun URL registri: URL, dominio, file di provenienza, e il contesto testuale di
   duecento caratteri che lo precede, perché il contesto dice a che cosa l'URL serviva;
5. classifichi il dominio in una delle sette categorie: archivio o istituzione pubblica;
   organo giudiziario o parlamentare; editoria accademica; enciclopedia collaborativa;
   stampa; sito militante o di parte; altro;
6. scriva l'esito in `repertorio/URL_CENSITI.xlsx`, un foglio per categoria, ordinato per
   frequenza del dominio.

Poi **verifica lo stato di ciascun URL** con richieste HTTP, con un ritardo fra l'una e
l'altra, registrando codice di risposta e data del controllo. Gli URL morti non vanno
cancellati: vanno marcati, perché un collegamento morto è esso stesso un dato — dice che
la fonte fu consultabile e non lo è più, ed è materia del principio per cui la data di
accessibilità è un dato storico.

Segnala infine, con evidenza, quanti URL provengano da enciclopedie collaborative e da
siti di parte: sono i due insiemi il cui grado probatorio non supera il **Livello C** e
che, se numerosi, indicano una fragilità dell'apparato che va dichiarata.

---

### FASE UNO — costruzione del quadro archivistico

Costruisci `repertorio/ARCHIVI_OPERATIVO.xlsx` con una riga per sede e queste colonne:
denominazione ufficiale nella lingua originale e in italiano; Stato; città e indirizzo;
base normativa istitutiva; consistenza misurata; ambito cronologico; procedura d'accesso;
limiti e vincoli dichiarati; disponibilità di consultazione remota; strumenti di corredo;
rilevanza per l'opera; dominio del sito ufficiale; stato di verifica; data.

Popolala con le sedi elencate nella sezione «SEDI ACCERTATE» in fondo a questo prompt,
che sono già verificate e non vanno riverificate. Per ciascuna, **cerca e registra l'URL
ufficiale**: è il dato che manca e che devi produrre tu.

---

### FASE DUE — le sedi con accesso remoto

Isola le sedi che consentono la consultazione a distanza. Sono le sole immediatamente
sfruttabili senza viaggio, e vanno affrontate per prime:

- l'archivio ceco dei servizi di sicurezza, che dal duemilasedici consente ai ricercatori
  pienamente registrati la consultazione remota dei materiali digitalizzati;
- l'archivio lettone, che ha pubblicato in rete schedari alfabetici, fascicoli degli agenti
  reclutati ed elenchi telefonici dei funzionari, con registrazione obbligatoria;
- l'archivio storico della Segreteria di Stato vaticana, integralmente digitalizzato per il
  pontificato aperto, con consultazione simultanea dello stesso documento;
- la direzione turca degli archivi di Stato, con catalogo remoto e ammissione esplicita
  degli stranieri;
- l'archivio dell'Alleanza atlantica, con oltre quarantamila documenti digitalizzati in rete;
- il sistema di ricerca dell'agenzia informativa statunitense e i progetti di desecretazione
  del Dipartimento di Stato;
- il portale della Rete italiana degli archivi, gratuito e senza registrazione obbligatoria.

Per ciascuna produci una scheda operativa: che cosa si ottiene senza muoversi, che cosa
richiede la presenza, quale registrazione serve e con quali tempi.

---

### FASE TRE — le condizioni d'accesso da accertare prima di programmare

Tre sedi pongono condizioni che vanno risolte prima di qualunque viaggio, e la risposta
non è deducibile: va cercata.

Primo, l'istituto polacco concede l'accesso agli stranieri **su base di reciprocità**.
Accerta che cosa significhi per un ricercatore italiano e quale documentazione occorra.

Secondo, il dicastero dottrinale vaticano richiede una domanda che specifichi tema e
ragioni della ricerca, con **commendatizia di un'autorità ecclesiastica o accademica**, e
il permesso scade il quindici luglio di ogni anno. Accerta la procedura corrente e i tempi.

Terzo, l'archivio storico diplomatico italiano consente **due sole buste al giorno**, tre
una tantum per chi viene da fuori Roma, da richiedere entro le undici del giorno precedente;
e la sala studio risulta chiusa dal ventitré febbraio duemilaventisei al trentuno ottobre,
con servizio ridotto. Verifica lo stato corrente prima di ogni pianificazione.

---

### FASE QUATTRO — collazione con i censimenti esistenti

Non verificare le sedi una per una. Esistono tre censimenti redatti da personale
archivistico, gratuiti, che coprono gran parte del terreno:

- *Guida alle fonti per una storia ancora da scrivere*, primo censimento delle fonti
  conservate presso gli aderenti alla Rete italiana degli archivi;
- il portale della medesima Rete, la cui ricerca è già articolata per **eventi, persone,
  indagini e processi, documenti, organizzazioni e uffici** — è una banca dati nodale già
  costruita sul dominio dell'opera;
- *Guía de Archivos de Memoria y Derechos Humanos en Chile*, del Centro de Derechos Humanos
  dell'Universidad Alberto Hurtado.

Collaziona il quadro con questi tre. Ciò che essi recano è già censito; ciò che il
repertorio reca in più va verificato **proprio perché lì non compare**. Produci l'elenco
delle sedi presenti nei censimenti e assenti dal repertorio, che è la vera lacuna.

---

### VINCOLI

- Ogni affermazione porta il proprio grado **Livello A**, **Livello B** o **Livello C**.
- Non dichiarare verificato ciò che non hai verificato: se una fase chiude tre voci invece
  di dieci, dichiara tre.
- La data di apertura di un archivio e la data del tuo controllo vanno sempre registrate.
- Nessuna tabella e nessun elenco puntato nei documenti dell'opera; i file di servizio come
  gli xlsx sono esenti.
- Numeri per esteso in parole italiane nei documenti dell'opera.

---

## SEDI ACCERTATE — da riportare in Fase Uno senza riverificare

### Italia

**Archivio centrale dello Stato.** Roma, piazzale degli Archivi ventisette, EUR. Autonomia
speciale, erede dell'Archivio del Regno del milleottocentosettantacinque, autonomo dal
millenovecentocinquantatré, aperto al pubblico nel millenovecentosessanta. Centosessanta
chilometri lineari. Consultazione libera ex articolo centoventidue del Codice dei beni
culturali. Teca digitale dal duemilaventidue. *Fondo pertinente non censito dal repertorio:*
«Archivi fascisti», con le carte della segreteria particolare del capo del governo, del
Partito nazionale fascista, della Milizia, delle Brigate Nere, della Guardia nazionale
repubblicana e del Partito fascista repubblicano, più l'archivio del Comitato centrale di
liberazione nazionale.

**Archivio storico del Senato della Repubblica.** Roma, via della Dogana Vecchia
ventinove. Istituito nel duemilauno, aperto nel duemilatré. Acquisisce gli archivi privati
dei parlamentari. Conserva il fondo della Commissione stragi, ordinato per subfondi: Alto
Adige, Argo sedici, Bologna, Calabresi, Cirillo, eversione di destra, Gladio. Consultabili i
fascicoli personali dei senatori dalla prima alla sesta legislatura. Forma canonica di
citazione: *Commissione stragi, [legislatura], Processi verbali sedute della Commissione,
Seduta n. [n] ([data]), pp. [x-y], in ASSR, Terrorismo e stragi (X-XIII leg.), 2.3*.

**Archivio storico della Camera dei deputati.** Roma, piazza San Macuto cinquantasette,
primo piano del Palazzo del Seminario; dal secondo al sesto piano hanno sede le Commissioni
bicamerali e d'inchiesta. Aperto al pubblico dal millenovecentonovantuno. Vi sono versati,
alla conclusione dei lavori, i documenti delle Commissioni d'inchiesta che si concludano
alla Camera. Fondi personali fra cui Cossiga, Pacciardi, Seniga. Massimo cinque buste per
richiesta, quattro richieste al giorno. **Il testo può essere trascritto e pubblicato solo
parzialmente**; la pubblicazione integrale richiede autorizzazione del Sovrintendente. **Il
segreto funzionale è derogabile**: il Presidente della Camera può eccezionalmente consentire
la consultazione a componenti di Commissioni d'inchiesta su richiesta della Commissione, o a
magistrati su loro istanza.

**Archivio storico diplomatico del Ministero degli Affari esteri.** Roma, Farnesina.
Istituito nel millenovecentodue. Circa trenta chilometri lineari. **Il ministero non versa
la propria documentazione all'Archivio centrale dello Stato**: chi vi cerchi documentazione
diplomatica non la trova perché non c'è, non perché sia stata sottratta. Fondi pertinenti:
archivi del ministero degli Esteri della Repubblica sociale millenovecentoquarantatré-
quarantacinque; ministero dell'Africa italiana; fondo del ministero della Cultura popolare;
Gabinetto Archivio riservato. Consultabili i documenti anteriori al cinquantennio; fra i
trenta e i cinquanta anni con procedura speciale ex decreto ministeriale del ventidue
dicembre duemilaquindici; **le situazioni puramente private solo dopo settant'anni**.
Strumento pertinente: *Guida alle fonti diplomatiche italiane sulla cooperazione europea*,
millenovecentoquarantasette-cinquantasette, con banca dati.

**Centro di documentazione Cultura della Legalità Democratica, Regione Toscana.** Firenze.
Conserva copia di **cinquecentoquarantuno fascicoli per ottomilaottocentoquarantacinque
documenti** della Commissione stragi. Via d'accesso alternativa a un fondo altrimenti
consultabile solo a Roma. Non censita dal repertorio.

**Centro documentazione Archivio Flamigni.** Oriolo Romano, provincia di Viterbo. Istituto
culturale nato nel duemilacinque. Il titolare del fondo è morto nel dicembre
duemilaventicinque: accertare le conseguenze su titolarità e accesso.

**Rete degli archivi per non dimenticare.** Portale inaugurato il nove maggio
duemilaundici dal Presidente della Repubblica. Ricerca filtrabile per **eventi, persone,
indagini e processi, documenti, organizzazioni e uffici**. Accesso gratuito, registrazione
facoltativa. Sezione «Muro della Memoria», registro nominale delle vittime.

**Centro siciliano di documentazione Giuseppe Impastato.** Palermo, via Villa Sperlinga
quindici. Fondato nel millenovecentosettantasette — l'anno *precedente* l'omicidio da cui
prende il nome per intitolazione successiva.

**Archivi storici dell'Unione europea.** Firenze, Villa Salviati, via Bolognese. Operativi
dal duemiladodici. Oltre ai fondi delle istituzioni, **i documenti privati di circa
centocinquanta fra persone, movimenti e organizzazioni dell'integrazione europea**. Regola
dei trent'anni: consultabile fino al millenovecentonovantasei circa. **I fondi riservati
restano a Lussemburgo**, edificio Konrad Adenauer: ciò che non è a Firenze non è distrutto.

### Europa centro-orientale — rete costituita a Berlino il sedici dicembre duemilaotto

**Istituto polacco della memoria nazionale.** Varsavia, via Postępu diciotto, più undici
sedi distaccate. Legge del diciotto dicembre millenovecentonovantotto, operativo dal primo
luglio duemila. Atti degli organi di sicurezza dal ventidue luglio millenovecentoquarantaquattro
al trentuno dicembre millenovecentottantanove, **compresi intelligence e controintelligence
civile e militare**. Accesso agli stranieri **su base di reciprocità**.

**Consiglio romeno per lo studio degli archivi della Securitate.** Bucarest. Fondato nel
duemila, legge del dicembre millenovecentonovantanove. Venticinque chilometri lineari, oltre
due milioni di volumi. **Ordinato secondo la logica della Securitate stessa.** Ogni metro
contiene circa cinquemila documenti; ogni fascicolo circa duecento pagine. Limite legale: è
pubblica solo la parte che **non riguarda la sicurezza nazionale, termine mai definito**.

**Archivio ceco dei servizi di sicurezza.** Praga, Branické náměstí e Na Struze; Kanice
presso Brno. Settecentoquarantotto fondi per quasi ventimila metri lineari al primo gennaio
duemiladiciassette. **Consultazione remota dal duemilasedici** per ricercatori registrati.
I fascicoli d'indagine dell'ex Sicurezza pubblica non rientrano nei sistemi di registrazione
e vanno richiesti al terzo dipartimento.

**Archivio storico della sicurezza di Stato ungherese.** Budapest, Eötvös utca sette. Legge
del duemilatré, preceduta dall'ufficio storico del millenovecentonovantasette. Due vie di
ricerca distinte: accademica e privata. Contiene fra l'altro **trascrizioni di conversazioni
intercettate**, verbali di interrogatorio, materiali sequestrati.

**Comitato bulgaro per la divulgazione dei documenti.** Sofia. Documenti della Sicurezza di
Stato **e dei servizi informativi dell'Esercito popolare**.

**Istituto slovacco della memoria della nazione.** Bratislava. Legge del duemiladue
approvata **superando il veto del capo dello Stato**.

**Autorità albanese sui documenti dell'ex Sicurezza di Stato.** Tirana. Documenti del
Sigurimi **dal millenovecentoquarantaquattro al millenovecentonovantuno**, accessibili dal
duemiladiciassette.

**Archivio speciale lituano.** Vilnius, Gedimino quaranta barra uno, **nell'ex quartier
generale del KGB**. Oltre un milione trecentocinquantamila fascicoli, più di diciassettemila
metri lineari, tre fondi. *Avvertenza:* le copie microfilmate inviate a un istituto estero
recano espunzioni, **e i fascicoli rimossi sono indicati nell'elenco del contenuto di ciascuna
bobina**.

**Archivi nazionali lettoni.** Riga. Pubblicati in rete **schedari alfabetici, fascicoli
degli agenti reclutati ed elenchi telefonici dei funzionari** del servizio sovietico, più
materiali del Comitato centrale. Registrazione obbligatoria.

### Penisola iberica

**Arquivo Nacional Torre do Tombo.** Lisbona, Alameda da Universidade. Istituito nel
milletrecentosettantotto. Centoquaranta chilometri lineari. **Oltre duemilacentoquaranta
fondi**: il repertorio ne censiva uno. Accesso libero sopra i sedici anni, ma **il fondo
della polizia politica è soggetto a regolamento proprio**. *Fondi pertinenti non censiti:*
servizi di centralizzazione delle informazioni di Mozambico e Angola; archivio personale del
capo del governo; **servizi di coordinamento dell'estinzione della polizia politica**;
**cooperativa dei funzionari della polizia politica sciolta**; Legione Portoghese; ministero
dell'Interno.

**Centro Documental de la Memoria Histórica.** Salamanca. Regio decreto del primo giugno
duemilasette. Periodo millenovecentotrentasei-millenovecentosettantotto. **Custodisce il
fondo del Tribunale speciale per la repressione della massoneria e del comunismo**, con
censimenti, credenziali, certificati e corrispondenza delle logge. *Avvertenze dichiarate:*
molte scatole non sono catalogate né descritte; **la documentazione non è digitalizzata**.

### Francia e Germania

**Archives nationales.** Pierrefitte-sur-Seine per tutto lo Stato francese dalla Rivoluzione
in poi e per gli archivi privati. Trecentottantatré chilometri lineari.

**Service historique de la Défense.** Vincennes. Oltre quattrocentocinquanta chilometri su
nove sedi. Fondi pertinenti: Segretariato generale della Difesa e della Sicurezza nazionale;
Gabinetto del ministro; Stato maggiore interforze; amministrazione militare d'oltremare dal
millenovecentoquaranta; **Gendarmerie nationale, comprese le gendarmerie specializzate**.
*Accertamento di distruzione dichiarato dal conservatore:* gli archivi della gendarmeria, «en
raison d'importantes destructions», non risalgono oltre la seconda metà dell'Ottocento.
*Regime d'accesso:* la legge del duemilaotto afferma la comunicabilità di pieno diritto, ma
**un'istruzione interministeriale del diciannove maggio millenovecentocinquantadue impone la
declassificazione preventiva**, e il termine di due mesi è raramente rispettato.

**Bundesarchiv.** Coblenza, Potsdamer Straße uno, e ventitré sedi in quattordici
dipartimenti. Ogni persona ha diritto di utilizzare gli atti su domanda.

**Archivio degli atti della sicurezza di Stato della Repubblica democratica.** Confluito nel
Bundesarchiv **dal diciassette giugno duemilaventuno senza spostamento fisico**. Circa
centoundici chilometri di atti. **Si applica la legge speciale, non la disciplina generale**:
modulo di domanda distinto. L'apertura fu resa possibile dall'occupazione delle sedi
nell'inverno millenovecentottantanove-novanta, **che pose fine alla distruzione in corso**.

### Grecia e Turchia

**Archivi generali dello Stato greco.** Atene, via Dafnis sessantuno, più trentasette sedi.
Creati nel millenovecentoquattordici. Fondi ministeriali fra cui il **militare**. Le
postazioni interne consentono la consultazione di materiale non accessibile dall'esterno.

**Direzione degli archivi di Stato della Turchia.** Ankara e Istanbul. Decreto presidenziale
del sedici luglio duemiladiciotto, in successione alla direzione generale del
millenovecentottantaquattro. **Ricercatori turchi e stranieri accedono gratuitamente** per
scopi non commerciali, con iscrizione in sede o attraverso il portale nazionale. Dipende
direttamente dalla Presidenza della Repubblica.

### Regno Unito

**The National Archives.** Kew. Serie FCO centoquarantuno, «archivi migrati»: circa
ottomilaottocento fascicoli da trentasette territori, ammessi il sette aprile duemilaundici.
Programma noto come *Operation Legacy*. Quasi ventimila fascicoli trasferiti dal
duemiladodici; **ottantottomila documenti di Hong Kong restano a Hanslope Park, in parte
vincolati fino al duemilaquarantasette**. *Marcatore di spoliazione:* il ministero non ha
reso pubblici né l'inventario del materiale detenuto al momento della scoperta né gli
elenchi dei fascicoli distrutti.

**Churchill Archives Centre.** Cambridge. Carte dell'ufficiale sovietico transfugo.

### Santa Sede

**Archivio Apostolico Vaticano.** Ottantacinque chilometri di scaffalature, oltre seicento
fondi su circa dodici secoli. **Consultazione consentita fino al nove ottobre
millenovecentocinquantotto e non oltre**: l'Archivio non è consultabile per il periodo su cui
l'opera lavora, e ciò va dichiarato accanto a ogni rinvio. Requisiti: laurea magistrale,
lettera di presentazione, certificato del titolo. Chiusura annuale il quindici luglio.

**Archivio storico della Sezione per i Rapporti con gli Stati.** Corrispondenza diplomatica.
**Integralmente digitalizzato** per il pontificato aperto, con consultazione simultanea dello
stesso documento da parte di più ricercatori.

**Archivio del Dicastero per la Dottrina della Fede.** Sede propria della posizione
dottrinale sulla massoneria. **Domanda con commendatizia di autorità ecclesiastica o
accademica**; consultazione senza restrizioni ma previa prenotazione, in ordine di arrivo.

### Organismi internazionali

**Archivio dell'Organizzazione del Trattato dell'Atlantico del Nord.** Bruxelles,
`archives.nato.int`. Inaugurato il diciannove maggio millenovecentonovantanove con circa
trentatremila documenti declassificati. Oltre quarantamila documenti in rete; **collezione
completa per il decennio millenovecentoquarantanove-cinquantanove**, serie ulteriori fino
agli anni Novanta. *Politica di divulgazione:* trent'anni e declassificazione secondo
C-M(55)15(Final), **salvo riservatezza personale, per la quale il vincolo dura cento anni
dalla data di nascita dell'interessato**. Deroga possibile per decisione del Consiglio.
*Avvertenza:* l'assenza di un documento dalla piattaforma non equivale né alla sua
inesistenza né a un diniego, ma alla condizione di **non ancora esaminato**.

**Archivi storici del Parlamento europeo.** Oltre cinque milioni di registrazioni,
**risalenti al millenovecentocinquantadue**, comprese le interrogazioni parlamentari.

**Servizio degli archivi storici della Commissione europea.** Bruxelles. **È il soggetto che
seleziona** ciò che sarà depositato a Firenze: chi voglia sapere che cosa non è stato
trasferito deve rivolgersi qui.

### Stati Uniti

**Sistema di ricerca dell'agenzia informativa presso gli Archivi nazionali.** College Park.
Oltre undici milioni di pagine. **La messa in rete è il risultato di una causa**: prima, il
sistema era accessibile solo dal lunedì al venerdì in orario d'ufficio. Avvertenza dell'ente:
alcuni documenti non appartengono ad alcuna raccolta e sfuggono a ricerche limitate per
raccolta.

**Sala di lettura del Dipartimento di Stato.** Progetti di desecretazione su Cile — **oltre
ventitremila documenti, millenovecentosessantotto-novantuno** — Argentina — quasi vent'anni
di lavoro sul periodo millenovecentosettantacinque-ottantatré — El Salvador e Guatemala; più
le trascrizioni telefoniche del segretario di Stato, settembre millenovecentosettantatré-
dicembre millenovecentosettantasei, riesaminate secondo la legge del millenovecentosettantaquattro
sulla conservazione dei materiali presidenziali.

**National Security Archive.** George Washington University, Gelman Library. Fondato nel
millenovecentottantacinque, **senza finanziamenti governativi**. Oltre quindici milioni di
pagine desecretate, più di settantamila istanze, oltre cinquanta cause. *Reperto
metodologico:* due versioni del medesimo scambio del millenovecentottantasette, esaminate a
dieci giorni di distanza dal medesimo revisore, **recano espunzioni diverse**.

### America latina

**Archivos del Terror.** Museo de la Justicia, Palazzo di giustizia, Asunción. Circa
settecentomila pagine rinvenute il ventidue dicembre millenovecentonovantadue. Registro
Memoria del Mondo dal duemilanove.

**Museo de las Memorias.** Asunción, calle Chile millesettantadue fra Manduvirá e Jejuí.
**Ex sede della Dirección Nacional de Asuntos Técnicos**, centro di detenzione e tortura per
oltre trent'anni. Nel maggio millenovecentocinquantasei vi stabilì il proprio ufficio un
colonnello inviato dal governo statunitense per addestrare i funzionari alla
controinsurrezione. Lunedì-venerdì otto-sedici, ingresso gratuito.

**Archivo Nacional de la Memoria.** Buenos Aires. Decreto del sedici dicembre duemilatré.
Sede dal novembre duemilasette negli edifici di un ex centro clandestino. **Trasformato in
unità organizzativa di un centro internazionale con decreto del ventuno maggio
duemilaventicinque.** *Dichiarazione dell'ente su di sé:* fondo aperto, classificazione
parziale e preliminare, **accesso parziale**, inventari ancora in elaborazione.

**Memoria Abierta.** Buenos Aires, Avenida Libertador ottomilacentocinquantuno. **Alleanza
di otto organizzazioni**, costituita nel millenovecentonovantanove. Tesauro specializzato sui
diritti umani. **Indice dei sopravvissuti ai centri clandestini con i luoghi di detenzione
dettagliati per ciascuna persona.**

**Museo de la Memoria y los Derechos Humanos.** Santiago del Cile, Avenida Matucana
cinquecentouno. Inaugurato l'undici gennaio duemiladieci. **Decreti, bandi militari, elenchi
nominativi e fascicoli di polizia**, settembre millenovecentosettantatré-marzo
millenovecentonovanta. Archivio digitale su `archivommdh.cl`.

**Archivo Nacional de la Memoria cileno**, presso l'Archivio nazionale. *Avvertenza
dichiarata:* incorporati solo i fondi con qualche livello di descrizione; **solo una
proporzione minore è digitalizzata**.

**Archivo General de la Nación uruguaiano.** Montevideo. Documentazione trasferita dal
ministero della Difesa nel duemiladiciannove; legge del maggio duemilaventiquattro. Fondo
recuperato: milleduecentodiciotto rulli di microfilm, oltre tre milioni di immagini —
schede personali, rapporti di intelligence, elenchi di sospetti, registri di sorveglianza
politica. *Caso da registrare:* nel duemilaventitré un anonimo caricò in rete **oltre
millecinquecento rulli digitalizzati, più di quanti ne custodisse l'archivio nazionale**.

**Commissione boliviana per la verità.** La Paz. Legge del ventuno agosto duemiladiciassette,
il cui articolo settimo dispone la desecretazione dei documenti militari e di polizia.
Relazione finale marzo duemilaventuno, undici tomi. *Dichiarazione della presidente:*
«fummo l'unica Commissione per la verità del continente che accedette alla documentazione
classificata delle Forze Armate… **le Forze Armate dovranno desecretare l'enorme
documentazione che è rimasta**».

**Archivio storico della Polizia Nazionale.** Guatemala, avenida La Pedrera. Rinvenuto nel
luglio duemilacinque; sala di lettura pubblica dal duemilanove.

**Memórias Reveladas.** Brasile, presso l'Archivio nazionale. Istituito nel maggio
duemilanove. Esclusi i documenti rivelatori dell'intimità della vita privata.

### Africa australe

**South African History Archive.** Università del Witwatersrand dal duemilaventidue. Fondato
nel millenovecentottantotto. Oltre ottocento metri lineari. Progetto *Traces of Truth* con
Historical Papers dal duemilatré.

---

## DOMINI GIÀ NOMINATI NELLE ANNOTAZIONI

Questi diciotto domini compaiono testualmente nelle annotazioni di verifica. Non sono URL
completi e vanno risolti: `abtl.hu` · `aldomoro.eu` · `archives.nato.int` · `archivio900.it` ·
`archivioantimafia.org` · `archivommdh.cl` · `archivonacional.cl` · `arxeiomnimon.gak.gr` ·
`fontitaliarepubblicana.it` · `inwentarz.ipn.gov.pl` · `katalog.devletarsivleri.gov.tr` ·
`kgb.arhivi.lv` · `mappedimemoria.it` · `memoria.cultura.gov.it` ·
`memoria.san.beniculturali.it` · `securityarchives.eu` · `stragi.it` · `todesnacht.com`
