La Kryssreferanse arve fra Arkivenhet?
======================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.15 (Kryssreferanse)
         Sidenummer  129
        Linjenummer  n/a
    Innsendingsdato  2019-04-28
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

For å kunne endre og slette individuelle kryssreferanser, så bør
entiteten Kryssreferanse ha SystemID og self-relasjon.  En grei måte å
løse dette på er å la entieten Kryssreferanse arve fra Arkivenhet.
Det vil sikre at det blir mulig via API-et og finne ut hvem som
opprettet en kryssreferanse, når den ble opprettet, og samt
tilsvarende informasjon om når det ble endret/oppdatert.  Det kan være
vesentlig ved kontroll og etterprøving av avgjørelser gjort av
forvaltningen å vite når en ble kjent med sammenheng mellom saker,
mapper og dokumenter, og slike kryssreferanser bør derfor dateres.

Endringen betyr at Kryssreferanse får følgende attributter arvet fra
Arkivenhet:

 * systemID
 * opprettetDato
 * opprettetAv
 * oppdatertDato
 * oppdatertAv
 * referanseOppdatertAv
 * referanseOpprettetAv

I stedet for strenger med SystemID-verdier bør referanse*-feltene i
Arkivenhet byttes ut med relasjoner til en Bruker-instans, som brukes
til å sette verdier i opprettetAv og oppdatertAv når entiteten lages.
Det må bli tema for en annen mangelmelding.

Ingen av disse nye feltene kan overleveres i avleveringsformatet til
Noark 5 versjon 4 eller versjon 5.  Det bør nevnes i spesifikasjonen
om hva som skal gjøres med disse nye verdiene ved avlevering.  Skal
feltene kastes ved avlevering?  I så tilfelle bør det dokumenteres i
spesifikasjonen, slik at de som implementerer eksport for avlevering
er klar over dette.  Et bedre valg er antagelig å utvide
deponi-XML-formatene i fremtidige versjoner til å ta med disse
feltene.

Se
[mangelmelding
#139](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/139)
for en lignende forespørsel.

Ønsket endring
--------------

Endre entitetsbeskrivelse av 7.2.1.15 (Kryssreferanse), legg inn at
den arver fra Arkivenhet, skriv følgende på slutten av beskrivelsen
for entiteten på side 129:

> Ved avlevering i tråd med XML-skjema for Noark 5 versjon 4 så
> droppes samtlige felt arvet fra Arkivenhet.  Disse ikke har
> korresponderende felt i avleveringsformatet.

I tillegg må filen uml-class-kryssreferanse.iuml oppdateres og det
bygges nye UML-diagrammer i PNG-format der endringen er inkludert.

Jeg sender inn konkret forslag til endring som patch via github.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/151 .
