Direktelenker til entiteter hvor mulig i relasjonslister
========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

FIXME Basert på https://github.com/HiOA-ABI/nikita-noark5-core/issues/85

FIXME finn relevant sidenummer

Det fremgår ikke klart fra spesifikasjonen hvordan forhold mellom
entiteter skal oppgis i _links-listene.  Skal en bruke
"underkataloger" eller bør en lenke direkte til relaterte entiteter?

Et eksempel er arkivdel (del 7.2.1.2 side 63), som har 0..1-kobling
til klassifikasjonssystem og derfor relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/
i sin _links-liste.

En måte å oppgi dette på er ved å støtte oppslag via en URL oppgitt
som href ala slik det oppgis på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/, der det er
en underkatalog under arkivdelen,
../arkivstruktur/Arkivdel/&lt;SystemID&gt;/klassifikasjonssystem.  Når
en tar GET på denne URL-en får en kopi av entiteten for
klassifikasjonssystem som gjelder for den aktuelle arkivdel.

En annen måte å oppgi dette på er å la href-verdien av relasjonen peke
direkte til aktuell entitet hvis verdien er satt, dvs. href peker til
noe ala ../arkivstruktur/klassifikasjonssystem/&lt;SystemID&gt;/.  Her
lenkes det direkte til 'self'-URL-en til entiteten, i stedet for å
lenke til en "kopi" av entiteten tilgjengelig under arkivdel.

Begge tilnærmingene virker å være rimelige tolkninger av
spesifikasjonen slik den er skrevet i dag.  Den siste tilnærmingen gir
fordeler når en implementerer tjenestegrensesnittet, da det blir
mindre kode å vedlikeholde ved å slippe å støtte en rekke URL-er på
formen .../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;.  Den gir
også en forden for API-klienter, som slipper først slå opp
.../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;, for så se på
'self'-relasjonen til resultatet for å vite konkret hvilket entitet
det er snakk om.

Her er et eksempel based på dokumentobjekt, der referanse til hvilket
dokumentbeskrivelse-entitet det hører til er en direktelenke:

```
{ ...
    "_links": [
    ...
    {
      "href" : "http://something/arkivstruktur/dokumentbeskrivelse/543543/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse/",
      "templated" : false
    }, {
      "href" : "http://something/arkivstruktur/dokumentobjekt/64564/",
      "rel" : "self",
      "templated" : false
    } ]
   }
```

Denne tilnærmingen fungerer kun for [0..1]-koblinger.  For
[0..*]-koblinger trengs det en liste, og mulighet til å filtere ved
hjelp av odata-notasjonen, slik at for disse tilfellene er det
nødvendig med relasjoner til
.../&lt;entitet&gt;/&lt;systemid&gt;/&lt;feltnavn&gt;.

Ønsket endring
--------------

FIXME formuler tekst for klargjør hvordan dette skal gjøres
