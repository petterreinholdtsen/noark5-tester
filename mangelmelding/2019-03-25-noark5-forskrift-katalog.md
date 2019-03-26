Samkjør katalognavn i forskrift og standard for hvor arkivdokumenter skal plasseres
===================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5
           Kategori  Versjon 5.0
        Alvorlighet  protest
       Meldingstype  trenger klargjøring 
    Brukerreferanse  pere@hungry.com
        Dokumentdel  krav 6.4.15:
         Sidenummer  98
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det bør beskrives på en entydig og klar måte hvor arkivdokumentfilene
skal ligge i en avleveringspakke.  I dag spriker beskrivelsen mellom
forskrift, Noark 5-spesifikasjon og praksis.

Følgende står i [Riksarkivarens forskrift), paragraf
5-31b](https://lovdata.no/dokument/SF/forskrift/2017-12-19-2286/KAPITTEL_5):

> § 5-31. Organisering av datafiler i avleverings- eller deponeringspakke
> (1) Filene som utgjør arkivuttrekket, skal være organisert på følgende måte:
[...]
> b) For arkivdokumenter skal det opprettes en katalog med navnet
>    DOKUMENT på første nivå under rotkatalogen på vedkommende
>    lagringsenhet. Dokumentfilene skal samles på andre nivå under
>    rotkatalogen og eventuelt struktureres i underkataloger. Dersom
>    et enkelt arkivdokument består av flere filer, skal disse samles
>    i én katalog med et entydig navn. Filformat for arkivdokumenter
>    angis ved filendelse, f.eks. XML, PDF eller TIF.

> c) Elektroniske utskrifter fra datasystemet skal lagres under en
>    katalog med navnet RAPPORT på første nivå under rotkatalogen på
>    vedkommende lagringsenhet. Rapportfilene skal samles på andre
>    nivå under rotkatalogen.

Dette stemmer ikke overens med det som står i Noark 5 version 3.1 side
97 og Noar 4.0 side 99 (i PDF, mangler sidetall):

> Filene i en avleveringspakke
[...]
> F. Dokumentfilene. Disse skal ligge i en underkatalog kalt
>    dokumenter.  Denne katalogen kan struktureres i nye
>    underkataloger etter fritt valg, f.eks. en underkatalog for hver
>    måned. Det er ingen krav til navngiving av dokumentfilene, men
>    filenes endelse skal angi arkivformat: pdf, tif, txt osv.

I Noark 5 versjon 5 side 98 står derimot følgende i krav 6.4.15:

> Dokumentene skal ligge i en underkatalog kalt DOKUMENT. Denne
> katalogen kan struktureres i nye underkataloger etter fritt
> valg. Dokumentfilene endelse skal angi arkivformat: pdf, tif, txt
> osv.

På side 109 i del 6.4.9 (Arkivdokumentene) står derimot følgende:

> Arkivdokumentene skal lagres i en egen underkatalog i
> avleveringspakken, og denne underkatalogen kan struktureres i nye
> underkataloger etter behov. Referansen fra arkivstrukturen til
> dokumentfilene vil ligge i dokumentobjektet, dvs. pÃ¥ laveste nivÃ¥
> i strukturen. Alle dokumentfiler som det blir referert til i
> arkivstruktur.xml, skal vÃ¦re med i uttrekket. Dessuten mÃ¥ ikke
> uttrekket inneholde noen dokumentfiler som mangler referanse fra
> dokumentobjektet. Referansen fra arkivstrukturen skal vÃ¦re relativ
> til dokumentfilene, dvs.  inneholde hele "stien" til dokumentet -
> f.eks. slik: dokumenter/2010/januar/123456789.pdf.

Underkatalogen skal altså enten hete "DOKUMENT" eller "dokumenter",
men den kan ikke hete begge deler samtidig og det er dermed ikke mulig
å følge både standard og forskrift samtidig.  Er det noen grunn til å
bruke store bokstaver i katalognavnene?


Ønsket endring
--------------

Det viktigste er at det brukes samme katalognavn overalt.  Jeg
foreslår å endre Riksarkivarens forskrift og Noark 5-standarden til å
bruke katalognavn med små bokstaver, dvs.  "dokumenter" og
"rapporter", for å unngå å gi inntrykk av å rope i beskrivelsen.
