Når skal det brukes 'uri' i stedet for 'href' \_links?
======================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  http://rel.kxml.no/noark5/
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  2017-04-19
 ------------------  ---------------------------------

Beskrivelse
-----------

I spesifikasjonens 6.1.1.1 (Oppkobling og ressurslenker) på side
11 og 12 skal relasjonnøkler oppgis med 'href' og 'rel'.  Dette blir
ikke gjort for eksempel i
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ som bruker 'uri'
i \_links i stedet for href.  Andre deler av nettstedet, for eksempel i
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/ som bruker
'href'.  Er det feil i nettsiden?  I motsatt tilfelle bør
spesifikasjonen utvides til å forklare når 'uri' skal brukes i stedet
for 'href'.  Jeg antar det er feil på nettsiden.  Det gjelder så vidt
jeg kan se tre tilfeller.

Ønsket endring
--------------

Endre 'url' til 'href' i \_links-responsen som vises frem på disse
nettsidene:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/

Respons
-------

Ingen respons fra Arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/22
