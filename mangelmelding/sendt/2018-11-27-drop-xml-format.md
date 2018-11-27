Dropp støtte for XML-varianten av API-et?
=========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.2
         Sidenummer  12
        Linjenummer  n/a
    Innsendingsdato  2018-11-27 (github issue #57)
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonen mangler en klar beskrivelse av hvordan
REST-forespørsler som bruker XML skal se ut, og hvilket resultat de
skal få tilbake.  Det eneste eksempelet er i del 6.1.1.1 (Oppkobling
og ressurslenker) på side 12, som viser hvordan relasjonslenker skal
formatteres som XML.

Men spesifikasjon, demotjenesten på http://n5test.kxml.no/api/ og
XML-eksempel på http://rel.kxml.no/noark5/v4/api/ er ikke enige om
hvordan XML-lister med relasjoner skal se ut.  Spesifikasjon og
demotjeneste er like, mens XML-eksempelet er forskjellig fra dem.
 
Slik ser eksempelet på side 12 og http://n5test.kxml.no/api/ ut:

> &lt;Links
>   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
>   xmlns="http://www.kxml.no/rest/1.0"&gt;
>   &lt;Links&gt;
>     &lt;link&gt;
>       &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/arkivstruktur&lt;/rel&gt;
>       &lt;href&gt;http://n5test.kxml.no/api/arkivstruktur&lt;/href&gt;
>       &lt;type xsi:nil="true" /&gt;
>       &lt;deprecation xsi:nil="true" /&gt;
>       &lt;name xsi:nil="true" /&gt;
>       &lt;title xsi:nil="true" /&gt;
>     &lt;/link&gt;
>     &lt;link&gt;
>       &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/sakarkiv&lt;/rel&gt;
>       &lt;href&gt;http://n5test.kxml.no/api/sakarkiv&lt;/href&gt;
>       &lt;type xsi:nil="true" /&gt;
>       &lt;deprecation xsi:nil="true" /&gt;
>       &lt;name xsi:nil="true" /&gt;
>       &lt;title xsi:nil="true" /&gt;
>     &lt;/link&gt;
>   &lt;/Links&gt;
> &lt;/Links&gt;

Merk hvordan denne har to identiske XML-tagger (Links) inne i
hverandre.  Hva er årsaken til at det brukes to identiske XML-tagger
slik?  En skulle tro det holder med et nivå.

Eksempelet på http://rel.kxml.no/noark5/v4/api/ har ikke
duplikat-tagger, men derimot LinkListe som ytre XML-tag i stedet for
Links:

> &lt;LinkListe
> xmlns:xsd="http://www.w3.org/2001/XMLSchema"
> xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
> xmlns="http://www.kxml.no/rest/1.0"&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/arkivstruktur&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/arkivstruktur&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/sakarkiv&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/sakarkiv&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/moeteogutvalgsbehandling&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/moeteogutvalgsbehandling&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/administrasjon&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/administrasjon&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/loggingogsporing&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/loggingogsporing&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;_links&gt;
> &lt;href&gt;http://n5test.kxml.no//api/rapporter&lt;/href&gt;
> &lt;rel&gt;http://rel.kxml.no/noark5/v4/api/rapporter&lt;/rel&gt;
> &lt;/_links&gt;
> &lt;/LinkListe&gt;

Hvilke av disse variantene er korrekte?  Den med duplikatlenker eller
den uten?

Spesifikasjonen mangler beskrivelse av hvordan objekter og lister skal
formatteres i XML.  Det er dermed uklart for de som skal utvikle
REST-klienter og -tjenester hvordan informasjonen som skal utveksles
skal være.  Det enkleste for alle ville være om det kun var en entydig
måte å snakke med API-et på, i stedet for to (JSON og XML).  Hvorfor
er det to ulike "dialekter" i spesifikasjonen?

Hvis XML skal være en del av API-definisjonen, så bør enten
spesifikasjonen beskrive hvordan alle objekter og lister av objekter
skal formateres i XML, eller så bør den inneholde en forklaring på
hvordan JSON-strukturer kan omdannes til XML.  Gitt at
XML-formatteringen nok trenger navnerom-informasjon, mens
JSON-formatteringen ikke trenger tilsvarende, så vil det ikke være
mulig å automatisk omforme JSON til XML uten at det tilføres ekstra
informasjon.  Hvorvidt det er praktisk gjennomførbart eller ikke
kommer an på hvor mange ulike navnerom som forventes brukt i
XML-formatteringen. 

Gitt at JSON-utgaven er tilstrekkelig og bedre beskrevet i
spesifikasjonen enn XML, så er det kanskje like greit å droppe
XML-dialekten?  Alternativt så må det beskrives i detalj hvordan
XML-utvekslingen for alle endepunktene skal se ut, og alle eksemplene
på http://rel.kxml.no/noark5/ endres til å stemme overens med
spesifikasjonen.

Ønsket endring
--------------

Dropp XML-utveksling fra API-spesifikasjonen, og bruk kun JSON.  Fjern teksten på side 12-, fra "Alternativt som XML" til og med siste "</Links>".

Respons
-------

Rapportert til
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/57 .
Ingen respons fra arkivverket så langt.
