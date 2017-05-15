Skal klassifikasjonssystem ha relasjonsnøklene (ny-)klassifikasjonssystem?
==========================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.13
         Sidenummer  122
        Linjenummer  n/a
    Innsendingsdato  2017-05-15
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonens del 7.2.1.13 (Klassifikasjonssystem) på side 122
lister opp to relasjonsnøkler som gir inntrykk av at det skal være
mulig å lage et underklassifikasjonssystem knyttet til et eksisterende
klassifikasjonssystem samt liste opp de tilknyttede
underklassifikasjonssystemene:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/

Tilsvarende relasjon i for eksempel Arkiv for å lage Arkivdel
(ny-arkivdel), og i Arkivdel for å lage mappe (ny-mappe) og
registrering (ny-registrering) og der er det mer åpenbart hva
relasjonene betyr.

Det er så vidt jeg kan se ingenting i Noark 5-standarden som indikerer
at det skal være mulig å ha et "under"-klassifikasjonssystem i
klassifikasjonsstrukturen. Dermed virker dette å være en skrivefeil i
tjenestegrensesnittet.  Dette synet styrkes når en ser i
[arkivstruktur.xsd](http://arkivverket.no/arkivverket/content/download/21276/191603/version/1/file/arkivstruktur.xsd)
der elementet klassifikasjonssystem ikke har støtte for
underklassifikasjonssystem.

De to relasjonene for å lage nytt og liste opp klassifikasjonssystem
er allerede listed opp under del 7.2.1.2 (Arkivdel), der de virker å
høre hjemme i henhold til Noark 5-standarden.

Ønsket endring
--------------

Endre relasjonsnøkkel-listen på side 122, fjern disse relasjonene:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/

Respons
-------

Ingen respons fra arkivverket så langt.
