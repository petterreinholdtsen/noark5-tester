Klassifikasjonssystem uten relasjonsnøkler (ny-)klassifikasjonssystem?
======================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.13
         Sidenummer  122
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonens del 7.2.1.13 (Klassifikasjonssystem) på side 122
lister opp relasjonsnøklene
http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
og
http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/
og gir dermed inntryk av at det skal være mulig å lage et
underklassifikasjonssystem knyttet til et eksisterende
klassifikasjonssystem og liste opp de tilknyttede
klassifikasjonssystemene.

Men det er så vidt jeg kan se ingenting i Noark 5-standarden som
indikerer at det skal være mulig å ha et "under"-klassifikasjonssystem
i klassifikasjonsstrukturen, så dette virker å være en skrivefeil i
tjenestegrensesnittet.

De to relasjonene er allerede listed opp under del 7.2.1.2 (Arkivdel),
der de virker å høre hjemme i henhold til Noark 5-standarden.

Ønsket endring
--------------

Endre side 122, fjern relasjonsnøklene
http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klassifikasjonssystem/
og
http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/ .
