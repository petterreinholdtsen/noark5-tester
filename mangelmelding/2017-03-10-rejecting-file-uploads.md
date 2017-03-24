Bør kjernen avvise filopplastinger med lengde 0 eller lengdeavvik?
========================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Hvis API-et mottar en fil med lengde 0, bør filen avvises og
avvisningmeldingen sendes til klienten?  Tilsvarende, hvis en klient
setter Content-Length til en bestemt verdi (f.eks. 54321), mens den
faktiske lengden på filen som blir lastet opp ikke er det samme
(f.eks. 18365), bør dette resultere i at filopplastingen avvises?

Ønsket endring
--------------

FIXME lag konkret endringsorslag.
