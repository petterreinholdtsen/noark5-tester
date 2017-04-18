Forbedre beskrivelse av filopplastingsprossesen
===============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også side 26 samt del 6.1.1.7 (Slette objekter (Delete)) på
side 22, del 7.2.1.6 (Dokumentbeskrivelse) på side 89-98 og 7.2.1.7
(Dokumentobjekt) på side 99-105.

Det er uklarheter rundt filopplasting og angivelse av metadata til
dokumentobjekt og dokumentbesrkivelse. Man må lese gjennon linjene for
å forstå hvordan dette henger sammen.

Opprettelse av Noark objekter (arkiv, mappe osv) er ganske enkel da
avhengigheten mellom entiter angis i HTTP-requesten. Når det gjelder
filopplasting så er det en slags transaksjon som må skje.

En mulig tolkning er at først oppretter man dokumentobjekt og angir
filnavn, filstørrelse, mimeType.  Etter at filen er lastet opp
beregner man sjekksum og oppdaterer dokumentobjekt med sjekksumverdi
og algoritme.  Det er da en to-trinns prossess for å få en endelig
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
når filoverføringen er fullført (dvs. POST uten Content-Length satt
til 0 eller bulkopplasting med PUT som returnerer 201 Created).

Når det gjelder håndtering av sjekksum og filstørrelse så ser vi en
interessant bi-effekt.  Hvis klienten angir sin sjekksum og
filstørrelse i innkommende dokumentobjekt så kan serveren sjekke dette
og hvis en av dem ikke stemmer kan opplastingen avvises og klienten få
tilbakemelding at noe er galt.

Klienten kan tilsvarede oppdage at noe er galt hvis kjernen
returnerer tilhørende dokumentobjekt som svar til en filopplasting.
Responsen kan klienten sammenligne med sin kopi av dokumentobjekt for
å sikre at resultatet tilsvarer den som ble laget før filopplastingen.

Skal det være tillatt å laste opp en tom fil, dvs. en med filstørrelse
satt til 0?  Det virker ikke å gi mening å laste opp en slik fil til
arkivet, og det mest fornuftige er antagelig å avvise oppretting av
dokumentobjekt hvis fillengden er null.

### Filopplasting som del av dokumentobjekt-transaksjon

En annen særlig utfordring er klienthåndtering av feil på
mottakersiden av tjenestegrensesnittet.  Prosessen med å laste opp en
fil kan ses på som en transaksjon som inkluderer opprettelsen av
dokumentbeskrivelse, dokumentobjekt og selve filen.  Hvis det skulle
skje at det er problemer med lagringssystemet til
tjenestegrensesnittet, for eksempel hvis filsystemet er fullt eller
tjenesten opplever en annen forstyrrelse, så kan det hende at
dokumentobjekt opprettes og lagres til persistent lager, men selve
filopplastingen blir avvist.  Dette vil returnere først 200 OK for
dokumentbeskrivlese og dokumentobjekt og deretter en 50X Error ved
opplastingen.

Det er uklart fra spesifikasjonen hva som skal gjøres i et slikt
tilfelle, og det er ingen dokumentert mekanisme for klienten å be om
at det filløse dokumentobjekt-instansen slettes når det skjer.  Det er
dermed ikke mulig for klienten å rydde opp etter seg når feilen
oppstår.  Den eneste muligheten for klienten er å forsøkte opplasting
på nytt og på nytt frem til den lykkes, og det er ikke alltid mulig
for en klient å fortsette til evig tid.  Det er bedre om klienten kan
fjerne de "ubrukelige" dokumentbeskrivelse og
dokumentobjekt-oppføringene, gi en feilmelding til brukeren som
forsøker å arkivere en fil og forsøke på nytt senere når det passer.

Ønsket endring
--------------

I del 6.1.1.9, legg inn nytt avsnitt etter setning «For å overføre en
ny fil brukes POST til href til
rel=http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil med header for
content-type og content-length.» på side 25.

> «Et dokumentopbjekt opprettes før opplasting, og først når en fil er
> klar for opplasting, og feltene «format», «mimeType», «filnavn»,
> «sjekksum», «sjekksumAlgoritme» og «filstørrelse» fylles inn.
> Tjenestegrensesnittet sjekker så ved opplasting av mimeType er
> identisk med Content-Type, filstørrelse er identisk med
> Content-Length (for complett POST) eller X-Upload-Content-Length
> (for overføring i bolker med PUT) og at sjekksum stemmer overens med
> den overførte filen.  Hvis en av disse verdiene fra opplastingen
> ikke stemmer overens med verdiene i dokumentobjekt, så returneres
> statuskode 400 BadRequest.»

Legg inn nytt avsnitt på side 26 før tabell over resultatkoder og
etter setning «Når siste overføring er gjort så returneres statuskode
201 Created.»

> Når en filopplasting er vellykket, så returneres tilhørende
> dokumentobjekt som respons på avsluttende 200 OK / 201 Created.

I del 7.2.1.7 på side 102-205, endre «Multipl.»-verdi for feltene
«format», «filnavn», «sjekksum», «sjekksumAlgoritme», «mimeType» og
«filstørrelse» fra «[0..1]» til «[1..1]» for å gjøre det klart at
disse verdiene alltid skal fylles inn ved oppretting av et
dokumentobjekt.

På side 105 endres definisjonen av filstørrelse fra «Definisjon:
Størrelsen på fila i antall bytes oppgitt med desimaltall» til

> «Definisjon: Størrelsen på fila i antall bytes oppgitt med
> desimaltall.  Filstørrelse skal være et positivt heltall større enn
> 0.»

### Filopplasting som del av dokumentobjekt-transaksjon

FIXME foreslå konkret forslag til endring for å beskrive hvordan feil
på tjenersiden ved filopplasting bør håndteres?

Dette tilfellet trenger en avklaring.  En mulig løsning er å bytte ut
de tre API-kallene med ett API-kall til kjernen der
dokumentbeskrivelse, dokumentobjekt og selve filen lastes opp sammen.
En slik løsning gjør det mulig for kjernen å behandle opprettelsen som
en transaksjon og la alle tre stegene feile hvis en av dem feiler.
Dermed kan klienten vite om hele transaksjonen var vellykket og filen
er lagret slik den skal.

En annen mulig løsning er å tillate sletting av egenproduserte
dokumentobjekt- og dokumentbeskrivelse-oppføringer frem til de er
knyttet til en opplastet fil, eller når de har fått satt variantformat
til arkivformat.  Det er uklart fra del 6.1.1.7 (Slette objekter
(Delete)) om dette er tillatt eller ikke.
