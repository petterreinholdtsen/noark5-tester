Endre formatfelt i Konvertering til samme type som format i Dokumentobjekt
==========================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Noark 5.5.0 TG versjon 1.0
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.15 (Konvertering)
         Sidenummer  116
        Linjenummer  1472
    Innsendingsdato  Ikke sendt inn ennå
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Filformat har ulik datatype i Dokumentobjekt og Konvertering.  I
førstnevnte er det en kodelisteverdi, i sistnevnte er det to strenger.
I følge https://github.com/arkivverket/schemas/issues/14 har M701,
M712 og M713 som er de aktuelle feltene samme vokabular, hvilket er et
godt argument for å behandle dem likt i tjenestegrensesnittet.

Ønsket endring
--------------

Endre datatype på Konvertering.konvertertFraFormat og
Konvertering.konvertertTilFormat fra string til Format.  Endringen
gjøres i attributtabell i del 7.2.1.15 (Konvertering) på side 116,
mellom linje 1472 og 1473 i PDF-en.
