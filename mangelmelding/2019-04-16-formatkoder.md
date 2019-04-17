Beskriv bruken av PRONOM-koder i format-feltet
==============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.2.10 (Format)
         Sidenummer  172
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge uttalelser fra Arkivverket i mangelmelding
[#4](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/4),
[#11](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/11)
og
[#77](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/77)
er det bestemt at format-feltet i Noark 5, felt M701 i
metadatakatalogen, skal inneholde PRONOM-koder.  Det bør stå i
spesifikasjonen og det bør beskrives hvilken form slike formatkoder
skal ha.  Foreslår å bruke samme form som PRONOM bruker på sine
websider, dvs. fmt/1 og x-fmt/1.  Ved å bruke denne formen kan
formatkoden enkelt sås opp i PRONOM-katalogen ved å besøke URL på
denne formen: http://www.nationalarchives.gov.uk/PRONOM/x-fmt/18 .

Valget av PRONOM gir endel utfordringer.  En utfordring er at
SOSI-formatet mangler PRONOM-kode.  Inntil alle formater som skal
arkiveres får PRONOM-koder må det finnes en prosedyre for å definere
sine egne koder.  En åpenbar mulighet er å definere et annet prefix
enn "fmt" og vedlikeholde sin egen katalog over ekstra formatkoder.
Foreslår at "vnd" brukes for slike formatkoder, at en slik kode
defineres for SOSI ("vnd/1"), og at teksten beskriver at slike koder
skal byttes ut med offisielle koder så snart offisiell PRONOM-kode
eksisterer.

En annen utfordring er at hver av formatene godkjent
i Riksarkivarens forskrift kan bety flere PRONOM-koder.  En liste over
forslag til PRONOM-koder som kan brukes for disse formatene er
tilgjengelig fra mitt prosjekt
[m701-noark5-katalog](https://gitlab.com/petterreinholdtsen/m701-noark5-katalog/blob/master/formatlist.rst),
og en kan der se at flere av formatene har mer enn en formatkode hos
PRONOM.

Et tredje problem er at enkelte PRONOM-koder kan bety flere av
formatene som er listet opp i Riksarkivarens forskrift.  For eksempel
er .docx både fmt/412 og fmt/494, alt etter om filen er kryptert eller
ikke, mens fmt/494 gjelder også .pptx og .xlsx når de er krypterte.
Det er uklart for meg hvordan dette skal løses.  En mulighet er å slå
fast at Riksarkivarens forskrift ikke gjelder krypterte dokumenter.
En annen er å godta samtlige mulige PRONOM-koder for et gitt format.

Ønsket endring
--------------

Legg til beskrivelse for kodelisten om at kodene skal hentes fra
PRONOM.  Beskriv hvordan formater som ikke har pronom-koder skal
håndteres, ved å bruke et annet prefix ("vnd/").  Skriv at listen over
formater i attributter-tabellen er et eksempel og henvis til eksternt
vedlikeholdt liste over formater for oppdatert og komplett liste over
PRONOM-koder for formatene i Riksarkivarens forskrift.  Frem til
Arkivverket publiserer sin liste foreslår jeg at min liste
([m701-noark5-katalog](https://gitlab.com/petterreinholdtsen/m701-noark5-katalog/blob/master/formatlist.rst))
flyttes til nikita-prosjektet og vedlikeholdes der.

Bytt ut alle oppføringer i tabellen over "attributter" til kodelisten
Format til å ha unike PRONOM-koder i "Kode"-kolonnen, samt

Jeg sender inn konkret forslag til endring som patch via github.
