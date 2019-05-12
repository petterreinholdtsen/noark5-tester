Entiteten Admin.Tilgang mangler relasjonsnøkkel
===============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.4.3 (Tilgang)
         Sidenummer  263
        Linjenummer  n/a
    Innsendingsdato  2019-05-12
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Entiteten Tilgang er beskrevet i Admin-pakken, men den er så vidt jeg
kan se ikke brukt noe sted, hverken i relasjoner til Bruker eller
AdministrativEnhet.

Det er uklart hva som er entitetens relasjonsnøkkel.  Kan det være
`http://rel.kxml.no/noark5/v4/api/admin/rettighet/`?  Har entiteten
byttet navn fra Rettighet til Tilgang i et tidligere utkast uten at
relasjonsnøkkelen er oppdatert?  Det må enten defineres en
relasjonsnøkkel for Tilgang, og legges inn en forklaring på
`http://rel.kxml.no/noark5/v4/api/admin/rettighet/`, eller så må
`http://rel.kxml.no/noark5/v4/api/admin/rettighet/` bytte navn til
`http://rel.kxml.no/noark5/v4/api/admin/tilgang/`.  Det siste virker
mest fornuftig på meg.

Det mangler forøvrig en beskrivelse om hvordan denne entieten skal
fungere, og hvordan den skal kobles til brukere.  Det får være tema
for en annen mangelmelding.

Ønsket endring
--------------

Endre relasjonsnøkkel http://rel.kxml.no/noark5/v4/api/admin/rettighet/  til
http://rel.kxml.no/noark5/v4/api/admin/tilgang/.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/180 .
