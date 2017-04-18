Klargjør om store og små bokstaver er like i feltnavn og identifikatorer
========================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1
         Sidenummer  11
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart fra spesifikasjonen om feltnavn og andre identifikatorer
har entydig form eller om det kan blandes store og små tegn om
hverandre.  Et eksempel er at spesifikasjonen omtaler 'SystemID',
'systemID' og 'systemid' (f.eks. teksten i 6.3 (Identifikatorer) side
28 og 7.2.1.16 (Mappe) side 141).  Er alle riktige?

Det er enklere å implementere en API-klient hvis alle feltnavn og
andre identifikatorer er entydig definert og tegnsekvensen som
identifiserer disse er det samme for alle implementasjoner av
tjenestegrensesnittet.  Jeg anbefaler derfor at det klargjøres hvordan
feltnavn og andre identifikatorer skal skrives og at det nevnes at en
ikke kan behandle små og store bokstaver som like når slike skal
sammenlignes.  Dette gjelder ikke bare feltnavn i JSON, men også for
relasjons-navn (URL-er).

Hvis slik blanding av store og små skal tillates uten å gi udefinerte
effekter for klientimplementasjonen, så må spesifikasjonen dokumentere
om de skal sammenlignes som store eller små bokstaver, og hvilke
språkspesifikke regler som skal brukes for å endre mellom store og små
bokstaver.  Dette for å sikre at en unngår uklarheter som endel språk
har (For eksempel på tysk er bokstaven «ß» overført til store blitt
til «SS» mens «SS» overført til små bokstaver blitt til «ss», mens
tyrkisk «i» som stor bokstav blir I med prikk på tyrkisk, mens den
blir «I» (uten prikk) på norsk.  Det finnes flere tilsvarende
eksempler).

Når en vurderer dette er det greit å ha i bakhodet at
[JSON-spesifikasjonen](http://jsonapi.org/format/) sier at «All member
names used in a JSON API document MUST be treated as case sensitive by
clients and servers».

Ønsket endring
--------------

Det enkleste er antagelig å beskrive dette under punkt 6.1.1 (REST
tjenestene), der følgende setning kan legges inn:

> Det skilles mellom små og store tegn i alle JSON-medlemsnavn og
> HATEOS-relasjoner, slik at disse er entydig definert uten
> konvertering mellom små og store tegn.
