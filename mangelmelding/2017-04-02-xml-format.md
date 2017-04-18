Beskriv hvordan lister og relasjoner skal formatteres i XML
===========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.2
         Sidenummer  
        Linjenummer  
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonen mangler en klar beskrivelse av hvordan
REST-forespørsler som bruker XML skal se ut, og hvilket resultat de
skal få tilbake.  Det eneste eksempelet er på side 12, som viser
hvordan relasjonslenker skal formatteres.

Men spesifikasjon og XML-eksempel på http://rel.kxml.no/noark5/v4/api/
er ikke enige om hvordan XML-lister med relasjoner skal se ut.
Demotjenesten på http://n5test.kxml.no/api/ ser derimot ut som
eksemplet i spesifikasjonen.
 
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
hverandre.  Det fremstår som redundant.

eksempelet på http://rel.kxml.no/noark5/v4/api/ bruker derimot
LinkListe som ytre XML-tag i stedet for Links:

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

FIXME beskriv behovet for informasjon om formattering av objekter og
lister.

Ønsket endring
--------------

FIXME foreslå formuleringer som beskriver formattering av objekter og
lister, f.eks. ved å beskrive hvordan JSON-eksempler kan gjøres om til
XML-eksempler (for å slippe doble eksempler i hele dokumentet).
