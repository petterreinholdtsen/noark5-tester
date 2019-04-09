La Dokumentobjekt arve fra Arkivenhet?
======================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.7 (Dokumentobjekt)
         Sidenummer  99
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Jeg er fortalt at Arkivverket tenker å la Dokumentobjekt i
tjenestegrensesnittet arve fra Arkivenhet.  Det betyr slik jeg forstår
det at følgende attributter tas ut av Dokumentobjekt og heller hentes
fra Arkivenhet:

 * systemID
 * opprettetDato
 * opprettetAv

Det betyr videre at følgende nye felter arves fra Arkivenhet,
dvs. legges til i Dokumentobjekt-entiteten:

 * oppdatertDato
 * oppdatertAv
 * referanseOppdatertAv
 * referanseOpprettetAv

Ingen av disse nye feltene kan overleveres i avleveringsformatet til
Noark 5 versjon 4 eller versjon 5.  Hva er det mening skal gjøres med
disse nye verdiene?  referanse*-feltene bør kanske byttes ut med
relasjoner til en Bruker-instans, men hva med oppdatert*-feltene?
Skal informasjonen ikke tas vare på?

Ønsket endring
--------------

FIXME finn ut hva som kan gjøres
