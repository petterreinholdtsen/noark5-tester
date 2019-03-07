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
    Innsendingsdato  2019-03-07 (github issue #76)
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

Her er et eksempel på hvordan UML-diagram fra kapittel 7 merket
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

Her er et enklere eksempler fra delen om Kodelister i kapittel 7,
figuren merket "Metadata - (diagram)" som PlantUML:

```
@startuml
class SystemID << simple >>
class BasicTypes::string << simple >>
BasicTypes::string <|-- SystemID
@enduml
```

Til slutt et mer komplekst eksempel figuren merket "Sakarkiv -
(diagram)" i delen om Sakarkiv i kapittel 7:

```
@startuml uml-sakarkiv-entiteter.puml
Arkivstruktur::Registrering <|-- Arkivstruktur::Basisregistrering
Arkivstruktur::Basisregistrering <|-- Journalpost
Arkivstruktur::Mappe <|-- Saksmappe

Arkivstruktur::Mappe "+mappe 0..1" *--> "+registrering 0..*" Arkivstruktur::Registrering
Arkivstruktur::Mappe *--> "+undermappe 0..*" Arkivstruktur::Mappe

Saksmappe *--> "+sakspart 0..*" Sakspart
Saksmappe "+sak 0..*" o--> "+presedens 0..*" Presedens
Presedens "+presedens 0..*" <--o "+journalpost 0..*" Journalpost

Journalpost *--> "+korrespondansepart 0..*" Korrespondansepart
Journalpost *--> "+avskrivning 0..*" Avskrivning
Journalpost *--> "+dokumentflyt 0..*" Dokumentflyt

Arkivstruktur::Registrering "+registrering 1..*" *--> "+dokumentbeskrivelse 0..*" Arkivstruktur::Dokumentbeskrivelse
@enduml
```

For denne siste er jeg i tvil om jeg har modellert riktig, da
originalfiguren har aggregeringslenker med pil begge veier, og det er
en relasjon jeg ikke har funnet i beskrivelser av UML og ikke helt
forstår hva betyr.

Ønsket endring
--------------

Velg et fri programvarebasert tekstformat for vedlikeholde
UML-diagrammer fremover.  Jeg anbefaler PlantUML-format, men er åpen
for bedre alternativer hvis det finnes.  Deretter må alle dagens
UML-diagrammer omformes til ønsket format.  Deretter må det lages
byggeregler for å lage PNG eller SVG-utgaver automatisk fra
tekstfilene for bruk i web- og PDF-utgave av spesifikasjonen.

Jeg kan bidra med omforming og justering av byggeregler.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/76 .
