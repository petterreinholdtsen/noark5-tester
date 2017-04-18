Når skal det brukes 'uri' i stedet for 'href' _links?
=====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  http://rel.kxml.no/noark5/
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I spesifikasjonens 6.1.1.1 (Oppkobling og ressurslenker) side på side
11 og 12 skal relasjonnøkler oppgis med 'href' og 'rel'.  Dette blir
ikke gjort for eksempel i
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ som bruker 'uri'
i _links i stedet for href.  Andre deler av nettstedet, for eksempel i
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/ som bruker
'href'.  Er det feil i nettsiden?  I motsatt tilfelle bør
spesifikasjonen utvides til å forklare når 'uri' skal brukes i stedet
for 'href'.  Jeg antar det er feil på nettsiden.  Det gjelder så vidt
jeg kan se tre tilfeller.

Ønsket endring
--------------

Endre 'url' til 'href' i _links-responsen på følgende nettsider:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/
