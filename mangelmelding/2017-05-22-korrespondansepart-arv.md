Håndtering av arv for korrespondansepart?
=========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  tsodring@oslomet.no
        Dokumentdel  7.2.3.4 (Journalpost)
         Sidenummer  212
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder også delene 7.2.3.7 (KorrespondansepartEnhet) side 227,
7.2.3.8 (KorrespondansepartIntern) side 228 og 7.2.3.9
(KorrespondansepartPerson) side 229.

Det er uklart hvordan spesialiseringene til korrespondansepart
(KorrespondansepartEnhet, KorrespondansepartIntern og
KorrespondansepartPerson) skal implementeres.

Journalpost entiteten har en relasjonsnøkkel

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepart/

men korrespondansepart-entiteten har ingen relasjonsnøkkel for å
utvide entiteten til en av entitetene som arver fra den.

En annen grunn til at dette er uklart fordi konseptet *arv*
implementeres forskjellig i standarden.  Mappe kan enten *utvides* til
Saksmappe eller opprettes direkte tilknyttet en Arkivdel.

Det er mulig at dette kanskje kan løses ved en objektorientert
tilnærming der tjeneren skal selv finne ut hva innkommende objekt er
og tildele riktig entitet for videre prossesering. Da er det verdt å
merke at spesialiseringene til Korrespondansepart har flere
metadatafelter og en mal på disse feltene bør eksponeres til en klient
via en GET forespørsel på feks:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepartperson/

Det er en fornuftig tilnærming hvis HTTP endepunktene til en tjener er 
utvetydelig.

Foreslår at det ikke brukes en *utvid-til* tilnærming, men at det heller
publiseres egne relasjonsnøkkel for de spesialiseringene til korrespondansepart. 
Følgende relasjonsnøkkel foreslås introdusert:

 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartenhet/
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartenhet/
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartperson/
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartperson/
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartintern/
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartintern/

Forventet funksjonalitet blir da at hvis en ønsker å hente alle 
korrespondanseparter knyttet til en journalpost, så kan en for 
eksempel bruke følgende relasjonsnøkkel:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/korrespondansepart/

Dette vil da hente ut alle korrespondanseparter. Det kan også være et
behov for å bare hente ut en bestemt type korrespondansepart. Da kan
følgende brukes:

 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartenhet
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartperson
 * http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartintern

Det er da ikke behov for relasjonsnøkkelen:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepart/

og denne kan fjernes.

KorrespondansepartEnhet og KorrespondansepartPerson bruker begge
*navn* som attributt. Det er kan være uhenldig å bruke en slik
generisk beskrivelse på et felt og er noe Noark 5 ellers unngår.  For
eksempel brukes det *sakspartNavn*, *moetedeltakerNavn*,
*korrespondansepartNavn* og *arkivskaperNavn* ellers i Noark
5-standarden.  For å være mer i tråd med andre felter er det kanskje
bedre med for eksempel "enhetsnavn" og "personnavn".  Hvis en bruker
unike navn blir det enklere å vite hvilket avleveringsfelt verdien
skal legges inn i, da en ikke må sjekke instansens entitet for å vite
det.

Det bør også vurderes om det er et behov for å skille navn i fornavn,
mellomnavn og etternavn. Det er en utbredt praksis i Norge at navn kan
lagres som et felt der navn, fornavn og etternavn skilles med
mellomrom.  Det er ikke automatisk gitt at utenlandske navn vil kunne
tilpasse en slik tilnærming.  Hvis en utenlandsk navn har et mellomrom
kan det skape problemer hvis systemet må lagre navnet lik det er
spesifisert i for eksempel pass.  Det er forøvrig nyttig å lese litt
bakgrunnsinformasjon om personnavn i «[Falsehoods Programmers Believe
About
Names](http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)»
av Patrick McKenzie, for å forstå hvilke utfordringer navn utgjør for
et datasystem.

Ønsket endring
--------------

På side 227 endres navnet på feltet "navn" til "enhetsnavn".

På side 229 endres navnet på feltet "navn" til "personnavn".

Tilsvarende endring gjøres på UML-figurene på side 198 og 199.

Under del 7.2.3.4 (Journalpost) på side 214 legges det inn følgende
relasjoner:

 **Tag**    | **Verdi**                                                                       |
| --------- | ------------------------------------------------------------------------------- |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartperson/      |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartperson/   |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartenhet/       |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartenhet/    |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/korrespondansepartintern/      |
| REST\_REL | http://rel.arkivverket.no/noark5/v4/api/sakarkiv/ny-korrespondansepartintern/   |

I samme tabell fjernes følgende relasjon:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-korrespondansepart/

Merk at nye relasjonsnøkler er foreslått i navnerommet
rel.arkivverket.no, jamfør mangelmelding #55.

FIXME hvordan søke i alle korrespondanseparter?
