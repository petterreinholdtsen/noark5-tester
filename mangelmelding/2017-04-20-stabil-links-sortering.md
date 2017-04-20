Kreves stabil rekkefølge på listene i \_links?
==============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.2
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonen sier ingenting om rekkefølgen på relasjonene i \_links
skal være stabil, dvs. at det returneres samme rekkefølge hver gang en
spør.  For å sikre at alle som implementerer API-et, det være seg
tjenere eller klienter, vet hva de kan forvente, bør det nevnes i
spesifikasjonen om rekkefølgen er stabil eller ikke.

For å sikre forutsigbare resultater fra API-et, og gjøre det enklere å
teste om API-et er korrekt (en kan sammenligne resultatet med
forhåndslagrede resultater i stedet for å måtte sammenligne
individuelle elementer i returnerte lister), så foreslår jeg at det
kreves stabil rekkefølge på listene i \_links.

Ønsket endring
--------------

Legg inn en setning i første avsnitt av 6.1.1.2 (Finne objekter
(Read)) på side 13, som lyder:

> Ressurslisten i _links skal være alfabetisk sortert på 'rel'-feltet
> for å sikre samme rekkefølge hos alle implementasjoner.

FIXME bedre formulering?
