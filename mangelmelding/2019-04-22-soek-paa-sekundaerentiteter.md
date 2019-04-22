Utvid muligheten til å søke på sekundærentiteter
========================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrenesnitt
           Kategori  versjon git 2019-04-22
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  tsodring@oslomet.no
        Dokumentdel  Finn ut
         Sidenummer  Finn ut
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------
Det er en svakhet i tjenestegrensesnitt når det gjelder hvordan en klient skal søke på
sekundærentiteter. Primærentiteter er de entitetene som utgjør arkivstruktur
feks *arkiv ... dokumentobjekt*. Sekundærentiteter er entitetene som 'henger' på
de primære. Eksempler er *merknad*, *noekkelord* og *forfatter*.

Det er mulig å søke på disse med $expand på OData men det gjør at klienten selv
må sammenstille resultatene. For å få en liste av på merknader på tvers av mappen, registrering
og dokumentbeskrivelse gjør man følgende:

    ../arkivstruktur/mappe/?$expand=merknad&$filter=merknad/any(m:m/merknadstype/kode eq 'B')
    ../arkivstruktur/registreging/?$expand=merknad&$filter=merknad/any(m:m/merknadstype/kode eq 'B')
    ../arkivstruktur/dokumentbeskrivelse/?$expand=merknad&$filter=merknad/any(m:m/merknadstype/kode eq 'B')

Når det gjelder sekundærentitetene vil noen av entitetene være ekstra viktig å søke på.
 *merknad*, *noekkelord* og *forfatter* er kandidater der det vil forventes enkel søk på disse
sekundærentitetene. Det kan opprettes en 'sekundaer'-pakke der disse entitetene publiseres som muliggjør
søk. Fordelen med dette er at klienten kan *oppdage' at det er mulig å søke på entitetene og at disse er
'viktige' entiteter. Jeg hadde et tredje tanke men det ble borte.


Ønsket endring
--------------


Jeg sender inn konkret forslag til endring som patch via github.
