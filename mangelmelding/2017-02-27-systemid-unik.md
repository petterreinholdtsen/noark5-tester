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
systemer.  Hva menes her?  Hvordan koordineres ID-tildeling på tvers
av leverandører slik at en unngår ID-kollisjoner?  En enkelt
leverandør kan jo ikke garantere at ingen andre lager ID-er som får
samme verdi som det leverandøræn selv lager.  Holder det at det liten
sjanse for kollisjoner, ved å bruke noe ala UUID?  Kan en for eksempel
bruke en tilfeldig UUID slik det er definert i [IETF RFC
4122](http://www.ietf.org/rfc/rfc4122.txt)?

Bør SystemID avledes fra verdier i objektet det henviser til, eller
bør det være frakoblet dette?  Svaret på dette spørsmålet avgjør
hvilken algoritme fra RHC 4122 som er aktuell hvis en skal lage en
UUID.

Ønsket endring
--------------

FIXME Hva kan foreslås her?  Kan en bruke UUID?
