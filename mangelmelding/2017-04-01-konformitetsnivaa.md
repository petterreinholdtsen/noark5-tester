Konformitetsnivå bør beskrives slik at det kan automatisk testes
================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  3
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder også vedlegg 1 på side 267.

Spesifikasjonen referer til
[http://rel.kxml.no/noark5/konformitetsniva/](http://rel.kxml.no/noark5/konformitetsniva/)
som inneholder foreløbig liste med konformitetsnivåer for krav som må
oppfylles for at en implementasjon skal oppfylle et gitt
konformitetsnivå.  Men listen er veldig kort og det er vanskelig å
vite når et kraver oppfylt eller ikke.  Finnes det flere detaljer om
hva de ulike kravene innebærer?

F.eks. for grunnleggende nivå 0 (basiskrav), sier listen på den
omtalte websiden ganske enkelt

 * CORS Cross-origin resource sharing
 * krav om autentisering
 * formatstøtte – json
 * formatstøtte – xml
 
For eksempel når det gjelder CORS, er det nok å støtte
OPTIONS-forespørsler, eller skal forespørsler og svar ha et bestemt
innhold?  Testinstansen på http://n5test.kxml.no/api/ støtter ikke
OPTIONS, så det er lite avklaring å finne der.  CORS er ikke nevnt i
spesifikasjonen.  Det bør vel legges inn en referanse der for å
forklare hva som menes med CORS i konformitetsnivåene.

Og når det gjelder støtte av JSON og XML, holder det at en kan hente
ut informasjon i JSON eller XML, eller må en kunne bruke POST og PUT i
begge formatene for å fylle kravene?  Må det brukte XML-formatet følge
et bestemt skjema?  Spesifikasjonen er uklar på XML-formatteringen,
slik at det vanskelig å vite hvilket skjema som i så fall skal brukes.

Det hadde vært fint om kravene refererte til deler av spesifikasjoen,
og var formulert på en måte som tillot automatisk testing av ET API
for å finne konformitetsnivå.

Jeg mistenker Nikita Noark 5 Core allerede oppfyller alle basiskrav,
men det er vanskelig å vite når beskrivelsen av kravene er så kort.

Ønsket endring
--------------

FIXME foreslå konkrete forbedringer
