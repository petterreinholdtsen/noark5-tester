Bør format i Konvertering bruke samme semantikk som i Dokumentobjekt?
=====================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Noark 5.5.0 TG versjon 1.0
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn ennå
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Filformat har ulik datatype i Dokumentobjekt og Konvertering.  I
førstnevnte er det en kodelisteverdi, i sistnevnte er det to strenger.
I følge https://github.com/arkivverket/schemas/issues/14 har M701,
M712 og M713, hvilket er et godt argument for å behandle dem likt i
protokollen.

Ønsket endring
--------------

Endre datatype på Konvertering.konvertertFraFormat og
Konvertering.konvertertTilFormat fra string til Format.
