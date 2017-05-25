Håndtering av arv for korrespondansepart?
=========================================

 ------------------  ---------------------------------
   Prosjekt NOARK 5  Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  7.2.3.6
         Sidenummer  223
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder også del 7.2.3.7 side 227, 7.2.3.8 side 228 og 7.2.3.9
side 229.

Det virker uklart hvordan arv skal håndteres når det gjelder
barna/spesialiseringene til korrespondansepart.  Dette gjelder
entiteter med klassene KorrespondansepartEnhet,
KorrespondansepartIntern og KorrespondansepartPerson.

Det er to måter arv kan håndteres i grensesnittet. Enten deler
entitetene en felles URL ala dette:

 * [contextpath][api]/sakarkiv/{systemID}/korrespondansepart

eller entitetene får hver sin URL ala dette:

 * [contextpath][api]/sakarkiv/{systemID}/korrespondansepartenhet
 * [contextpath][api]/sakarkiv/{systemID}/korrespondansepartperson
 * [contextpath][api]/sakarkiv/{systemID}/korrespondansepartintern

Det er delte meninger om hvilken måte som er «riktig».  Når det
gjelder arv andre steder i tjenestegrensesnittet er det valgt metode
nummer 2 der entiteter får egne URL.  Dette ser vi blant annet med
mappe/saksmappe.

 * [contextpath][api]/arkivstruktur/mappe/{systemID}
 * [contextpath][api]/sakarkiv/saksmappe/{systemID}

Det tolkes utifra tjenestegrensesnittet-delene 7.2.3.6 til 7.2.3.9 og
del 7.2.3.4 at med korrespondansepart så ønsker dere en felles URL for
alle korrespondansepart typer. Dette synet styres ved at det kun er en
relasjon under journalpost for å legge til korrespondansepart, ikke
hver korrespondansepartklasse:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepart/

Slik vi tolker beskrivelsen i tjenestegrensesnitt-spesifikasjone er
det ikke alltid mulig å differensiere mellom en
korrespondansepartperson og en korrespondansepartenhet, med mindre
noen av feltene som kun finnes i en av klassene har verdi når
entiteten opprettes.  Begge entiteter har kun multiplisitet 1..1 på
feltet navn.  Det vil dermed ikke være mulig å finne ut om innkommende
objekt skal lagres som en korrespondansepartperson eller som en
korrespondansepartenhet hvis kun navn oppgis.

For å løse dette på en generisk måte, ser vi tre muligheter.

1. Gjør det mulig å se forskjell på feltene
   korrespondansepartenhet.navn og korrespondansepartenhet.navn.
   Feltene kunne for eksempel bytte navn til enhetsnavn og personnavn.

2. Legg til et felt i korrespondansepart som kan brukes til å skille
   mellom korrespondansepartklassene. Det er et felt der som heter
   korrespondanseparttype, men den brukes til å skille mellom
   avsender/mottaker osv.  En ide er å bruke et nytt feltnavn
   'korrespondanseklasse'.

3. Lage egne URLer for å opprette de forskjellige typer
   korrespondanseparter.

Gitt at arv allerede håndteres med forskjellige URL så kan en
fortsette med den tilnærmingen. Det gjør implementasjon litt enklere.
Samtidig kunne en også velge mer beskrivende feltnavn enn "navn".
Derfor foreslår vi at spesifikasjonen endres til å ta i bruk både
metode 1 og 3.

For å eksemplifisere dette, vil det å hente alle korrespondanseparter knyttet
til en journalpost se slik ut:

 * [contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepart

Dette vil da hente ut alle korrespondanseparter. Det kan også være et
behov for å bare hente ut en bestemt type korrespondansepart. Da kan
følgende brukes:

 * [contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartenhet
 * [contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartperson
 * [contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartintern

Vi ser også at i N5v3.1 er det et felt M400 - korrespondansepartNavn.
Det er kanskje M400 "navn" feltet egentlig er.

FIXME hva betyr setningen over?

Det bør også vurderes om det er et behov for å skille navn i fornavn,
mellomnavn og etternavn.

Spesifikasjonen forklarer ikke hvordan en skal kunne skille mellom
enheter og personer.  Dette kan være utfordrende å gjøre maskinelt,
spesielt ved korrespondanse med utlandet.  Det hadde vært nyttig med
beskrivelser, enten direkte i spesifikasjonen eller som referanse til
andre dokumenter der det er beskrevet hvordan dette skal gjøres.

Ønsket endring
--------------

På side 227 endres navnet på feltet "navn" til "enhetsnavn".

På side 229 endres navnet på feltet "navn" til "personnavn".

Tilsvarende endring gjøres på UML-grafene på side 1998 og 199.

På side 214 legges det inn følgende relasjoner:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartenhet/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartperson/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartintern/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartenhet/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartperson/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartintern/
