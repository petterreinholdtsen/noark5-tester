Vedlikeholde UML-diagrammer som tekstfiler med kommandolinjeverktøy for PNG-omforming
=====================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I dag finnes UML-diagrammene i spesifikasjonen som bilder.  Det gjør
vedlikehold og oppdatering vanskelig og gjør det umulig å bruke git
til å se hva som er endret i dem over tid.

Et bedre opplegg vil være å vedlikeholde UML-diagrammene som
tekstfiler som automatisk omformes til bilder.  Det er en stor fordel
om det finnes et fri programvare-kommandolinjeverktøy som kan omforme
tekstfilene til bilder som kan vises frem i spesifikasjonen.

Det finnes flere kandidater til verktøy som kan gjøre dette for oss.
Se https://modeling-languages.com/text-uml-tools-complete-list/ for en
liste.

Har testet endel av dem, og PlantUML ser ut til å være et bra
alternativ for vedlikehold av UML-diagrammer.  Nettsiden
http://plantuml.com/class-diagram har mer informasjon om formatet.
Her er et eksempel på hvordan UML-diagram fra kapittel 7 med tittelen
"LoggingOgSporing - (diagram)" kan se ut i PlantUML-format:

```
@startuml
class Endringslogg {
  systemID : SystemID [0..1]
  referanseArkivenhet : SystemID [0..1] 
  referanseMetadata : string [0..1]
  endretDato : datetime
  endretAv : string
  referanseEndretAv : string
  tidligereVerdi : string [0..1]
  nyVerdi : string [0..1]
}
@enduml
```

Ønsket endring
--------------

Velge et fri programvarebasert tekstformat for vedlikeholde
UML-diagrammer fremover, fortrinsvis PlantUML, og så omforme alle
dagens UML-diagrammer til PlantUML-format.  Deretter må det lages
byggeregler for å lage PNG eller SVG-utgaver automatisk fra
tekstfilene for bruk i web- og PDF-utgave av spesifikasjonen.
