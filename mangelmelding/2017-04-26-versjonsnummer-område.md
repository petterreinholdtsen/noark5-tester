Hva er gyldighetsområdet for versjonsnummer i dokumentobjekt?
=============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.7
         Sidenummer  101
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonens del 7.2.1.7 (Dokumentobjekt) side 101 nevner ikke hva
som er gyldige verdier for versjonsnummer i dokumentobjekt.  Den
forklarer heller ikke om første versjon av et dokument skal gis ha
nummer 0, 1 eller et annet tall.  Det nevnes heller ikke om det er
krav til hvor stort versjonstallet kan bli.  Er det krav eller
begresninger til bitlengde for verdien i versjonsnummer, eller kan det
bli uendelig stort?

Dette er heller ikke oppgitt i Noark 5-spesifikasjonen.  Noark
5-spesifikasjonens del 5.6 (Dokumentbeskrivelse og Dokumentobjekt)
side 71 sier at versjonummer er

> Identifikasjon av versjoner innenfor samme dokument.  Se også
> merknad 1 nedenfor.

Merknaden nedenfor forteller ikke mer om gyldighetsområde:

> Merknad 
> 1. Det er her snakk om arkiverte versjoner av samme dokument. Alle
> de arkiverte variantene skal tas med ved en deponering/avlevering.

For å sikre at alle implementasjoner teller versjoner på samme måte og
er i stand til å håndtere hverandres verdier bør dette klargjøres i
spesifikasjonen.

Ønsket endring
--------------

Klargjør hva som er minste og største mulige verdi for versjonsnummer,
hva som er første verdi og hvorvidt verdien skal stige eller synke for
hver ny versjon.

FIXME formuler tekstforslag.
