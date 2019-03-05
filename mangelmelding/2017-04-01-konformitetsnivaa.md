Konformitetsnivå bør beskrives slik at det kan automatisk testes
================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  3
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også vedlegg 1 på side 267.

Spesifikasjonen referer til
[http://rel.kxml.no/noark5/konformitetsniva/](http://rel.kxml.no/noark5/konformitetsniva/)
som inneholder foreløpig liste med konformitetsnivåer for krav som må
oppfylles for at en implementasjon skal oppfylle et gitt
konformitetsnivå.  Men listen er veldig kort og det er vanskelig å
vite når et krav er oppfylt eller ikke.  Finnes det flere detaljer om
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
forklare hva som menes med CORS i konformitetsnivåene.  Se forøvrig
mangelmelding
[#29](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/29)
om behovet for spesifisering av CORS.

Og når det gjelder støtte av JSON og XML, holder det at en kan hente
ut informasjon i JSON eller XML, eller må en kunne bruke POST og PUT i
begge formatene for å fylle kravene?  Må det brukte XML-formatet følge
et bestemt skjema?  Spesifikasjonen er uklar på XML-formatteringen,
slik at det vanskelig å vite hvilket skjema som i så fall skal brukes.

Det hadde vært fint om kravene refererte til deler av spesifikasjoen,
og var formulert på en måte som tillot automatisk testing av et API
for å finne konformitetsnivå.

Jeg mistenker Nikita Noark 5 Core allerede oppfyller alle basiskrav,
men det er vanskelig å vite når beskrivelsen av kravene er så kort.

Ønsket endring
--------------

Skriv om konformitetskravene til å henvise til spesifikasjonsteksten,
og sikre at de ulike kravene kan testes maskinelt slik at det er mulig
å kjøre et program som snakker med API-tjenesten for å kontrollere om
den er konform eller ikke.  En måte å gjøre dette på er å henvise til
hvilke relasjoner som skal være tilstede og funksjonelle i
\_links-listen for en gitt klasse, slik at en kan opprette objekter av
den gitte klassen og se at relasjonsoperasjonen er på plass.

Eller kanskje enda bedre, bytt ut listen med konformitetskrav med et
program med fri programvarelisens som kan brukes til å teste om en
API-implementasjon fungerer som den skal.  Dermed kan enhver som lager
en tjenestegrensesnitt-implementasjon sjekke om det oppfører seg som
forventet av dette programmet.

Hvis det blir avklart at konformitetskravene skal være maskinelt
testbare, så bidrar jeg gjerne med forslag til formuleringer og
skriving av program for å teste konformitetsnivå.

Kan det være en ide å flytte oversikten over konformitetskravene fra
http://rel.kxml.no/noark5/konformitetsniva/ til github-depotet for
tjenestegrensesnittet, slik at det blir versjonskontrollert og mulig
for enhver å se hvordan den endrer seg over tid?
