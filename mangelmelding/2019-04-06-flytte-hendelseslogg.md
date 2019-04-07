Bør entiteten Hendelseslogg flytte til pakken LoggingOgSporing?
===============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.10 (Hendelseslogg)
         Sidenummer  111
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Bør entiteten Hendelseslogg flyttes til pakken LoggingOgSporing?  Det
er uklart hvorfor pakken LoggingOgSporing er en separat pakke, når den
kun inneholder en eneste entitet, Endringslogg.  Når en i tillegg ser
at Arkivstruktur.Hendelseslogg arver fra LoggingOgSporing.Endringslogg
slik at det blir en hard avhengighet fra Arkivstruktur til
LoggingOgSporing, så er det uklart hvorfor disse to entitetene er
fordelt mellom to pakker på denne måten.  Er pakken LoggingOgSporing
valgfri, på samme måte som Sakarkiv og Moeter?  Skal det være
akseptabelt å lage en API-implementasjon som ikke har med logging og
sporing?  Det vil jo gjøre det umulig å ha med hele Arkivstruktur, som
altså inneholder Hendelseslogg.  En alternativ tolkning er at det skal
være greit å lage en API-implementasjon som ikke inneholder
Arkivstruktur, men jeg synes ikke den gir mening.

Et alternativ til å flytte Hendelseslogg til LoggingOgSporing er å
flytte Endringslogg til Arkivstruktur.  Da forsvinner pakken
LoggingOgSporing.

Ønsket endring
--------------

Flytt omtalen av Hendelseslogg i kapittel 7.2.1.10 på side 111 fra
Arkivstruktur til LoggingOgSporing, og oppdater alle relaterte
UML-diagrammer til å reflektere ny pakkeplassering.

Når diagrammer som PlantUML er tatt i bruk i master-grenen
([mangelmelding #76](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/76)),
så skal jeg sende inn konkret endringsforslag for å fikse dette.
