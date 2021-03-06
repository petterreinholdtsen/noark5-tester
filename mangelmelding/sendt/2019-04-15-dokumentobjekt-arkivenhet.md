La Dokumentobjekt arve fra Arkivenhet?
======================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.7 (Dokumentobjekt)
         Sidenummer  99
        Linjenummer  n/a
    Innsendingsdato  2019-04-15
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Jeg er fortalt av Arkivverket at en planlegger å la entiteten
Dokumentobjekt i tjenestegrensesnittet arve fra Arkivenhet.  Det betyr
slik jeg forstår det at følgende attributter tas ut av Dokumentobjekt
og heller hentes/arves fra Arkivenhet:

 * systemID
 * opprettetDato
 * opprettetAv

Det betyr videre at følgende nye felter arves fra Arkivenhet, det vil
si at de blir nye i Dokumentobjekt-entiteten:

 * oppdatertDato
 * oppdatertAv
 * referanseOppdatertAv
 * referanseOpprettetAv

I stedet for strenger med SystemID-verdier bør referanse*-feltene i
Arkivenhet byttes ut med relasjoner til en Bruker-instans, som brukes
til å sette verdier i opprettetAv og oppdatertAv når entiteten lages.
Det får være tema for en annen mangelmelding.

Ingen av disse nye feltene kan overleveres i avleveringsformatet til
Noark 5 versjon 4 eller versjon 5.  Hva er det i så fall mening skal
gjøres med disse nye verdiene ved avlevering?  Skal informasjonen ikke
tas vare på ved avlevering?  I så tilfelle bør det dokumenteres i
spesifikasjonen, slik at de som implementerer eksport for avlevering
er klar over dette.

Ønsket endring
--------------

Endre entitetsbeskrivelse av 7.2.1.7 (Dokumentobjekt), legg inn at den
arver fra Arkivenhet, fjern attributtene systemID, opprettetDato og
opprettetAv fra tabellen over attributter, samt skriv følgende på
slutten av beskrivelsen for entiteten på side 99:

> Ved avlevering i tråd med XML-skjema for Noark 5 versjon 4 så
> droppes følgende felt arvet fra Arkivenhet: «oppdatertDato»,
> «oppdatertAv», «referanseOppdatertAv» og «referanseOpprettetAv».  Disse
> ikke har korresponderende felt i avleveringsformatet.

I tillegg må filen uml-class-dokumentobjekt.iuml oppdateres og det
bygges nye UML-diagrammer i PNG-format der endringen er inkludert.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/139 .
