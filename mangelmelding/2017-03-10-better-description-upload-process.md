Forbedre beskivelse av filopplastingsprossesen
==============================================

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

Beskrivelse
-----------

Gjelder også 7.2.1.7 side 99.

Det er uklarheter rundt filopplasting og angivelse av metadata til
dokumentobjekt og dokumentbesrkivelse. Man må lese gjennon linjene for
å forstå hvordan dette henger sammen.

Opprettelse av Noark objekter (arkiv, mappe osv) er ganske enkel da
avhengigheten mellom entiter angies i HTTP-requesten. Når det gjelder
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
og hvis det ikke stemmer kan klienten få tilbakemelding at noe er
galt.  Det samme kan skje kjernen returnerer tilhørende dokumentobjekt
som svar til en filopplasting.  Da kan klienten sjekke at filen som er
lagret er det samme som den som ble lastet opp.

Ønsket endring
--------------

I del 6.1.1.9, legg inn nytt avsnitt etter setning «For å overføre en
ny fil brukes POST til href til
rel=http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil med header for
content-type og content-length.» på side 25.

> «Et dokumentopbjekt opprettes før opplasting, og først når en fil er
> klar for opplasting, og feltene format, mimeType, filnavn, sjekksum,
> sjekksumAlgoritme og filstørrelse fylles inn.  Tjenestegrensesnittet
> sjekker så ved opplasting av mimeType er identisk med Content-Type,
> filstørrelse er identisk med Content-Length (for complett POST)
> eller X-Upload-Content-Length (for overføring i bolker med PUT) og
> at sjekksum stemmer overens med den overførte filen.  Hvis en av
> disse verdiene fra opplastingen ikke stemmer overens med verdiene i
> dokumentobjekt, så returneres statuskode 400 BadRequest.»

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
