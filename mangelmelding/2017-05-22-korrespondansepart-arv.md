Håndtering av arv for korrespondansepart?
===================================================

------------------ ---------------------------------
Prosjekt NOARK 5 Tjenestegresesnitt
Kategori Versjon 1.0 beta
Alvorlighet kommentar
Meldingstype trenger klargjøring
Brukerreferanse thomas.sodring@hioa.no
Dokumentdel 7.2.3.6
Sidenummer 223
Linjenummer n/a
Innsendingsdato ikke sendt inn
------------------ ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder også Del 7.2.3.7, 7.2.3.8, 7.2.3.9

Det virker uklart hvordan arv skal håndteres når det gjelder barna til
korrespondansepart. Dette gjelder entitetene korrespondansepartEnhet,
korrespondansepartIntern og korrespondansepartPerson.

Det er to måter arv kan håndteres i grensesnittet. Enten deler entitetene
en felles URL feks

[contextpath][api]/sakarkiv/{systemID}/korrespondansepart

eller entitetene får hver sin URL feks

[contextpath][api]/sakarkiv/{systemID}/korrespondansepartenhet
[contextpath][api]/sakarkiv/{systemID}/korrespondansepartperson
[contextpath][api]/sakarkiv/{systemID}/korrespondansepartintern

Det er delte meninger om hvilken måte som er "riktig". Når det gjelder arv
andre steder i tjeneste grensesnittet har dere valgt metode nummer 2 der
entiteter får egne URL. Dette ser vi blant annet med mappe/saksmappe.

[contextpath][api]/arkivstruktur/mappe/{systemID}
[contextpath][api]/sakarkiv/saksmappe∕{systemID}

Det tolkes utifra tjenestegrensesnittet deler 7.2.3.6 til 7.2.3.9 og
de 7.2.3.4 at med korrespondansepart så ønsker dere en felles URL for
alle korrespondansepart typer. Dette er bekreftet da det kun er en REL
under journalpost for å legge til en korrespondansepart.

http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepart/

Slik vi tolker tjenestegrensesnittet er det umulig å differensiere 
mellom en korrespondansepartperson og en korrespondansepartenhet. 
Begge entiteter har kun multiplisitet 1..1 på feltet navn.
Det vil derfor ikke være mulig å finne ut om innkommende objekt 
skal lagres som en korrespondansepartperson eller som en 
korrespondansepartenhet.

For å løse dette på en generisk måte, ser vi tre muligheter.

1. Differensier mellom feltene korrespondansepartenhet.navn og
korrespondansepartenhet.navn. Feltene kunne hete feks
enhetsnavn og personnavn.

2. Legg til et felt i korrespondansepart som kan brukes til å skille
mellom korrespondansepart typene. Det er et felt der som heter
korrespondanseparttype, men den brukes til å skille mellom Avsender/
mottaker osv.

3. Lage egne URLer for de forskjellige typer korrespondanseparter.

Gitt at arv allerede håndteres med forskjellige URL så kan dere allikevel
 fortsette med den tilnærmingen. Det gjør implementasjon litt enklere.
 Samtidig kunne dere også velge mer beskrivende feltnavn enn "navn". 
Derfor foreslår vi at dere tar i bruk både 1 og 3.

For å eksemplifisere dette, vil det å hente alle korrespondanseparter knyttet
til en journalpost se slik ut:

[contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepart

Dette vil da hente ut alle korrespondanseparter. Det kan også være et behov
for å bare hente ut en bestemt type korrespondansepart. Da kan følgende brukes:

[contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartenhet
[contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartperson
[contextpath][api]/sakarkiv/journalpost/{systemID}/korrespondansepartintern

Vi ser også at i N5v3.1 er det et felt M400 - korrespondansepartNavn. Det er 
kanskje M400 "navn" feltet egentlig er.

Det bør også vurderes om det er et behov for å skille navn i fornavn,
mellomnavn og etternavn.

Ønsket endring
--------------

På side 227 endres navnet på feltet "navn" til "enhetsnavn".

På side 229 endres navnet på feltet "navn" til "personnavn".

På side 214 legges til følgende REL:

http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartenhet/
http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartperson/
http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartintern/
http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartenhet/
http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartperson/
http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepartintern/

og endre teksten til å gjenspeile dette.


