Hvordan gjøres SystemdID unik og persistent på tvers av andre systemer?
=======================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.3
         Sidenummer  28
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

I følge del 6.3 (Identifikatorer) skal arkivkjernen sørge for at
SystemID blir en unik og persistent identifikator på tvers av andre
systemer.  Hva tenker en på her?  Hvordan koordineres ID-tildeling på
tvers av leverandører slik at en unngår ID-kollisjoner?  Holder det at
det liten sjanse for kollisjoner, slik UUID er definert?  Kan en
f.eks. bruke en tilfeldig UUID slik det er definert i [IETF RFC
4122](http://www.ietf.org/rfc/rfc4122.txt)?

Bør SystemID avledes fra verdier i objektet det henviser til, eller
bør det være frakoblet dette?  Svaret på dette spørsmålet avgjør
hvilken algoritme som er aktuell hvis en skal lage en UUID.

Ønsket endring
--------------

FIXME Hva kan foreslås her?  Kan en bruke UUID?

Respons
-------

Ingen respons fra arkivverket så langt.
