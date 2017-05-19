Direktelenker til entiteter hvor mulig i relasjonslister
========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det fremgår ikke klart fra spesifikasjonen hvordan forhold mellom
entiteter skal oppgis i _links-listene.  Skal en bruke underkataloger
eller bør en lenke direkte til relaterte entiteter?

FIXME Basert på https://github.com/HiOA-ABI/nikita-noark5-core/issues/85

Et eksempel er arkivdel (del 7.2.1.2 side 63), som har 0..1-kobling
til klassifikasjonssystem og relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/.

En måte å oppgi dette på er ved å støtte oppslag via en URL ala det
som oppgis på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/, dvs.
../arkivstruktur/Arkivdel/&lt;SystemID&gt;/klassifikasjonssystem.  En
annen måte å oppgi dette på er å la href-verdien av relasjonen peke
direkte til aktuell entitet hvis verdien er satt, slik som dette:
../arkivstruktur/klassifikasjonssystem/&lt;SystemID&gt;/.  Begge
tilnærmingene virker å være rimelige tolkninger av spesifikasjonen.
Den siste gir fordeler når en implementerer tjenestegrensesnittet, da
det blir mindre kode ved å slippe å støtte en rekke URL-er på formen
.../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;.  Den gir også
en forden for API-klienter, som slipper først slå opp
.../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;, så se på
'self'-relasjonen til resultatet for å vite konkret hvilket entitet
det er snakk om.

Denne tilnærmingen fungerer kun for [0..1]-koblinger.  For
[0..*]-koblinger trengs det en liste, og mulighet til å filtere ved
hjelp av odata-notasjonen, slik at for disse tilfellene er det
nødvendig med relasjoner til
.../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;.

Ønsket endring
--------------

FIXME formuler tekst for klargjør hvordan dette skal gjøres
