Forbedre beskrivelse av filopplastingsprossesen
===============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  2018-11-20 (github issue #25)
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også side 26 samt del 6.1.1.7 (Slette objekter (Delete)) på
side 22, del 7.2.1.6 (Dokumentbeskrivelse) på side 89-98 og 7.2.1.7
(Dokumentobjekt) på side 99-105.

Det er uklarheter rundt filopplasting og angivelse av metadata til
dokumentobjekt og dokumentbeskrivelse. Man må lese gjennom linjene for
å forstå hvordan dette henger sammen.

Opprettelse av Noark objekter (arkiv, mappe osv) er ganske enkel da
avhengigheten mellom entiter angis i HTTP-requesten. Når det gjelder
filopplasting så er det en flerstegs transaksjon som gjøres.

En mulig tolkning er at først oppretter man dokumentobjekt og angir
filnavn, filstørrelse, mimeType.  Etter at filen er lastet opp
beregner man sjekksum og oppdaterer dokumentobjekt med sjekksumverdi
og algoritme.  Det er da en to-trinns prossess for å få den endelige
dokumentobjektet i databasen.

En annen mulig tolkning er at sjekksum registreres idet dokumentobjekt
opprettes.

Det er uklart fra spesifikasjonen hva klienten skal gjøre og hva
API-tjenerimplementasjonen skal gjøre.  Hvem av dem skal angi
mimeType, filstørelse, format og sjekksum?  Når skal det skje?  Hva
skal skje hvis disse ikke samsvarer med filen som lastes opp?

Spesifikasjonen sier heller ingen ting om hva slags innhold en
filopplasting skal returnere.  Hvis det ikke skal returneres noe annet
enn en HTTP returkode, så bør det nevnes eksplisitt.  Et annet
alternativ som kan gi mening er å returnere tilhørende dokumentobjekt
når filoverføringen er fullført (det vil si ved POST uten
Content-Length satt til 0 og når siste bolk lastes opp med PUT som
returnerer 201 Created).

Når det gjelder håndtering av sjekksum og filstørrelse så ser vi en
interessant bi-effekt.  Hvis klienten angir sin sjekksum og
filstørrelse i innkommende dokumentobjekt så kan serveren sjekke dette
og hvis en av dem ikke stemmer kan opplastingen avvises og klienten få
tilbakemelding at noe er galt.

Klienten kan tilsvarede oppdage at noe er galt hvis kjernen
returnerer tilhørende dokumentobjekt som svar til en filopplasting.
Responsen kan klienten sammenligne med sin kopi av dokumentobjekt for
å sikre at resultatet tilsvarer den som ble laget før filopplastingen.

Videre kan det problematiseres hvorvidt det skal det være tillatt å
laste opp en tom fil, dvs. en med filstørrelse satt til 0?  Det virker
ikke å gi mening å laste opp en slik fil til arkivet, da den jo er
formatløs (hvilket format og mimeType skal settes for en tom fil, og
hvorfor skal den lagres?), og det mest fornuftige er antagelig å
avvise oppretting av dokumentobjekt hvis fillengden er null.

### Kan en fil knyttet til dokumentobjekt byttes ut?

Spesifikasjonen sier ingenting om hva som skal skje hvis en API-klient
oppretter en dokumentobjekt-entitet, laster opp en fil, og så laster
opp en annen fil.  Det vil si at klienten ønsker å utføre en
PUT-forespøsel og overskrive filen som ble lastet opp.  Skal det være
mulig?  Hvis eksisterende sjekksum i dokumentobjekt kontrolleres etter
opplasting, så vil filen antagelig bli avvist på grunn av ny sjekksum.
Skal det være mulig å endre sjekksum i dokumentobjekt-entiteten uten å
endre allerede opplastet fil?  Det vil vel fjerne poenget med
sjekksummen.  Det mest fornuftige er kanskje å kreve at en
dokumentobjekt-entiet med tilknyttet fil må slettes og ny opprettes
hvis det skal lastes opp en ny fil.

Ønsket endring
--------------

I del 6.1.1.9, legg inn nytt avsnitt etter setning «Når siste
overføring er gjort så returneres statuskode 201 Created» på side 26:

> «Det er ikke mulig å overskrive en eksisterende fil med en POST
> eller en PUT-forespørsel. Hvis en fil må erstattes så skal filen
> slettes og en ny POST utføres mot href til
> rel=http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil»

### Filopplasting som del av dokumentobjekt-transaksjon

En annen særlig utfordring er klienthåndtering av feil på
mottakersiden av tjenestegrensesnittet.  Prosessen med å laste opp en
fil kan ses på som en transaksjon som inkluderer opprettelsen av
dokumentbeskrivelse, dokumentobjekt og opplasting av selve filen.
Hvis det skulle skje at det er problemer med lagringssystemet til
tjenestegrensesnittet, for eksempel hvis filsystemet er fullt eller
tjenesten opplever en annen forstyrrelse, så kan det hende at
dokumentobjekt opprettes og lagres til persistent lager, men selve
filopplastingen blir avvist.  Dette vil returnere først 200 OK for
dokumentbeskrivlese og dokumentobjekt og deretter en 50X Error ved
opplastingen.

Det er uklart fra spesifikasjonen hva som skal gjøres i et slikt
tilfelle.  Skal klienten forsøke å rulle tilbake opprettingen av
entitetene for dokumentobjekt og dokumentbeskrivelse ved hjelp av
DELETE, eller fortsette å forsøke å laste opp dokumentet, potensielt
til evig tid?  Det blir uansett vanskelig for klienten å rydde opp
etter seg, og helt umulig hvis det som skjedde var at serveren krasjet
ved opplasting og dermed ble utilgjengelig når klienten forsøker å
slette dokumentobjekt og dokumentbeskrivelse.  Det er bedre om
klienten kan fjerne de "ubrukte" dokumentbeskrivelse og
dokumentobjekt-oppføringene, gi en feilmelding til brukeren som
forsøker å arkivere en fil og forsøke på nytt senere når det passer,
men det vil ikke være mulig i enkelte feilsituasjoner.

Ønsket endring
--------------

I del 6.1.1.9, legg inn nytt avsnitt etter setning «For å overføre en
ny fil brukes POST til href til
rel=http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil med header for
content-type og content-length.» på side 25.

> «Et dokumentobjekt opprettes før opplasting. Hvis noen av feltene
> «format», «mimeType», «filnavn», «sjekksum», «sjekksumAlgoritme» og
> «filstørrelse» er fyllt inn ved opprettelsen skal tjeneren
> verifisere at verdiene i de angitte feltene stemmer når filen lastes
> opp.  Tjeneren sjekker ved opplasting i dette tilfellet også at
> mimeType er identisk med Content-Type, filstørrelse er identisk med
> Content-Length (for komplett POST) eller X-Upload-Content-Length
> (for overføring i bolker med PUT) og at sjekksum stemmer overens med
> den overførte filen.  Hvis tjeneren etter opplasting ser at noen av
> verdiene avleded fra opplastet fil ikke stemmer overens med verdiene
> i dokumentobjekt-entiteten, så returneres statuskode 400 Bad
> Request.  Hvis den opplastede filen har et format tjeneren ikke
> kjenner igjen, så settes format til 'UNKNOWN'.  Når filopplasting er
> fullført setter tjeneren de feltene i dokumentobjekt som ikke var
> satt, dvs. utleder «format», «mimeType», «filnavn», «sjekksum», og
> «filstørrelse» basert på filens innhold samt, samt gir
> «sjekksumAlgoritme» aktuell verdi.»

Legg inn nytt avsnitt på side 26 før tabell over resultatkoder og
etter setning «Når siste overføring er gjort så returneres statuskode
201 Created»:

> Når en filopplasting er vellykket, så returneres tilhørende
> dokumentobjekt som respons på avsluttende 200 OK / 201 Created.

På side 105 endres definisjonen av filstørrelse fra «Definisjon:
Størrelsen på fila i antall bytes oppgitt med desimaltall» til

> «Definisjon: Størrelsen på fila i antall bytes oppgitt med
> desimaltall.  Filstørrelse skal være et positivt heltall større enn
> 0.»

### Filopplasting som del av dokumentobjekt-transaksjon

Problemstillingen om hvordan tjenestegrensesnittet skal håndtere feil
i komboen dokumentbeskrivelse, dokumentobjekt og fil opplasting kan
også sees på fra server-siden. Hvis opplasting av filen blir avbrutt
eller en feil skjer med lagring til disk bør det være spesifisert
hvordan tjeneren skal håndtere feilen. Dette tilfellet trenger en
avklaring.

En mulig og kanskje bedre løsning er å bytte ut de tre API-kallene med
ett API-kall til kjernen der dokumentbeskrivelse, dokumentobjekt og
selve filen lastes opp sammen. En slik løsning gjør det mulig for
kjernen å behandle opprettelsen som en transaksjon og la alle tre
stegene feile hvis et av dem feiler.  Dermed kan klienten vite om hele
transaksjonen var vellykket og filen er lagret slik den skal.  En
annen fordel ved en slik samlet registrering/opplasting er at serveren
kan forsøke å hente ut metadata fra dokumentet (f.eks. tittel,
forfatter, dato etc) og slik gjøre det enklere å arkivere dokumenter.

En annen mulig løsning er å tillate sletting av egenproduserte
dokumentobjekt- og dokumentbeskrivelse-oppføringer frem til de er
knyttet til en opplastet fil, eller når de har fått satt variantformat
til arkivformat.  Det er uklart fra del 6.1.1.7 (Slette objekter
(Delete)) om dette er tillatt eller ikke.

Foreslår en enkel endring i første omgang, så kan en vurdere løsninger
med opplasting og registrering som en transaksjon på sikt.

Ønsket endring
--------------

I del 6.1.1.9 legges følgende avsnitt inn på side 26 etter setning «Når
siste overføring er gjort så returneres statuskode 201 Created»:

> «Dersom det skjer en feil under opplasting eller lagringsprossesen
> skal tjeneren returnere en 422 Unprocessable Entity svar. Det er
> klientens ansvar da å slette eventuelle dokumentbeskrivelse og
> dokumentobjet entiteter ved hjelp av DELETE på entitetenes
> self-relasjon.»

I tillegg legges 422-koden inn i tabellen på side 26-27 over mulige
feilkoder fra opplastingen.

Respons
-------

Rapportert til
[https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/25].
Ingen respons fra arkivverket så langt.
