Skal klasse ha relasjonsnøklene (ny-)klassifikasjonssystem?
===========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.12
         Sidenummer  115
        Linjenummer  n/a
    Innsendingsdato  2019-02-09
 ------------------  ---------------------------------

Beskrivelse
-----------

Dette er relatert til tilsvarende [mangelmelding #33 om
klassifikasjonssystem](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/33).

Spesifikasjonens del 7.2.1.12 (Klasse) på side 115 lister opp to
relasjonsnøkler som gir inntrykk av at det skal være mulig å lage et
underklassifikasjonssystem knyttet til et eksisterende klasse samt
liste opp de tilknyttede underklassifikasjonssystemene:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/

Tilsvarende relasjon i for eksempel Arkiv for å lage Arkivdel
(ny-arkivdel), og i Arkivdel for å lage mappe (ny-mappe) og
registrering (ny-registrering) og der er det mer åpenbart hva
relasjonene betyr.

Det er så vidt jeg kan se ingenting i Noark 5-standarden som indikerer
at det skal være mulig å ha et "under"-klassifikasjonssystem i
klassestrukturen.  Dermed virker dette å være en skrivefeil i
tjenestegrensesnittet.  Dette synet styrkes når en ser i
[arkivstruktur.xsd](http://schema.arkivverket.no/N5/v4.0/arkivstruktur.xsd)
der elementet klasse ikke har støtte for underklassifikasjonssystem.

Det vil være nyttig for API-klienter å kunne slå opp
"foreldre"-klassifikasjonssystem for en klasse, der slik finnes, men
det bør antagelig bruke en annen relasjonsstruktur.

De to relasjonene for å lage nytt og liste opp klassifikasjonssystem
er allerede listed opp under del 7.2.1.2 (Arkivdel), der de virker å
høre hjemme i henhold til Noark 5-standarden.

Ønsket endring
--------------

Endre relasjonsnøkkel-listen på side 115, fjern disse relasjonene:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/67 .
