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

Bør entiteten Hendelseslogg flytte til pakken LoggingOgSporing?  Det
er uklart hvorfor pakken finnes, når den kun inneholder en eneste
entitet.  Når en i tillegg ser at Arkivstruktur.Hendelseslogg arver
fra LoggingOgSporing.Endringslog, så er det litt uklart hvorfor de er
delt mellom to pakker på den måten.  Skal det være greit å lage en
API-implementasjon som ikke har med logging og sporing?  Det vil jo
gjøre det umulig å ha med hele Arkivstruktur, som altså inneholder
Hendelseslogg.  Alternativ tolkning, at det skal være greit å lage en
API-implementasjon som ikke inneholder Arkivstruktur, gir ikke mening.

Et alternativ til å flytte Hendelseslogg til LoggingOgSporing er å
flytte Endringslogg til Arkivstruktur.

Ønsket endring
--------------

Flytt omtalen av Hendelseslogg i kapittel 7.2.1.10 på side 111 fra
Arkivstruktur til LoggingOgSporing, og oppdatert alle relaterte
UML-diagrammer til å reflektere ny pakkeplassering.

Når diagrammer som PlantUML er tatt i bruk i master-grenen
([mangelmelding #76](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/76)),
så skal jeg sende inn konkret endringsforslag for å fikse dette.
