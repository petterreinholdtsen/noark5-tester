Fjern ubrukte kolonner fra «attributter»-tabellene
==================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.1 (Arkiv)
         Sidenummer  57
        Linjenummer  n/a
    Innsendingsdato  2019-04-15
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder en rekke sider fra og med 57 til og med 265.

Samtlige tabeller over attributter for entiteter (type=class) og
datatyper (type=dataType) i spesifikasjonen inneholder en tom og
ubrukt kolonne med tittel «Kode».  De eneste «attributter»-tabellene som
bruker denne kolonnen er kodelistene, og der er derimot kolonnene
«Multipl.» og «Type» ubrukte.

Det er ingen grunn til å ha ubrukte kolonner i alle disse tabellene i
teksten.  Det gjør formattering som PDF vanskeligere, samt forvirrer
leseren som lurer på hva kolonnen brukes til.  Jeg foreslår derfor at
kolonnene fjernes.

Ønsket endring
--------------

Fjern kolonne «Kode» fra attributt-tabellen til samtlige entiteter med
type class og dataType.  Fjern kolonnene «Multipl.» og «Type» fra
attributt-tabellen til samtlige entiteter med type codelist.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/138 .
