Journalpost.mottattDato skal være datetime, ikke date
=====================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.4
         Sidenummer  218
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også UML-diagrammer på side 54, 197, 198, 202 og 203.

Listen over attributter i Journalpost har «date» som type for
«mottattDato» (M104).  I metadatakatalog.xsd for Noark 5 versjon 4 er
M104-typen derimot definert til enten «date» og «datetime».  Hvis en
antar at XSD-filen er korrekt, så må datatypen i beskrivelsen av
API-et endres til «datetime».

Ønsket endring
--------------

Bytt ut «date» med «datetime» som type for mottattDato (M104) i
tabellen over attributter for Journalpost, og oppdater alle aktuelle
UML-diagrammer.

Når diagrammer som PlantUML er tatt i bruk i master-grenen, så skal
jeg sende inn konkret endringsforslag for å fikse dette.
