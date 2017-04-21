Klargjør om store og små bokstaver er like i feltnavn og relasjoner
===================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1
         Sidenummer  11
        Linjenummer  n/a
    Innsendingsdato  2017-04-20
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også side 141, 148, 253, 258 og 263.

Det er uklart fra spesifikasjonen om feltnavn og andre identifikatorer
har entydig form eller om det kan blandes store og små tegn om
hverandre.

Et eksempel er at spesifikasjonen omtaler «SystemID», «systemID» og
«systemid» (f.eks. teksten i 6.3 (Identifikatorer) side 28 og 7.2.1.16
(Mappe) side 141).  Er alle riktige?  Det kan se ut til at «SystemID»
er ment å være typenavn, mens «systemID» er ment å være attributtnavn,
men bruken av «systemid» gjør det vanskelig å være sikker.  Hvis det
er tilfelle bør det kanskje nevnes eksplisitt i spesifikasjonen for
hver klasse/attributt?

Det er enklere å implementere en API-klient hvis alle feltnavn og
andre identifikatorer er entydig definert og tegnsekvensen som
identifiserer disse er det samme for alle implementasjoner av
tjenestegrensesnittet.  Det er dermed lurt å klargjøre hvordan
feltnavn og andre identifikatorer skal skrives og at det nevnes at en
ikke kan behandle små og store bokstaver som like når slike skal
sammenlignes.  Dette gjelder ikke bare feltnavn i JSON, men også for
relasjons-navn (URL-er).

Hvis slik blanding av store og små skal tillates uten å gi udefinerte
effekter for klientimplementasjonen, så må spesifikasjonen dokumentere
om de skal sammenlignes som store eller små bokstaver, og hvilke
språkspesifikke regler som skal brukes for å navnene gjøres om til
store eller små bokstaver.  Dette for å sikre at en unngår uklarheter
som endel språk har.  Et eksempel er tysk, der bokstaven «ß» overført
til store blir til «SS» mens «SS» overført til små bokstaver blitt til
«ss».  Et annet eksempel er «i» som overført til stor bokstav på
tyrkisk blir «İ» (I med prikk), mens den blir «I» (uten prikk) på
norsk.  Det finnes tilsvarende eksempler for andre språk.

Når en vurderer hva som bør gjøres i
tjenestegrensesnitt-spesifikasjonen er det greit å ha i bakhodet at
[JSON-spesifikasjonen](http://jsonapi.org/format/) sier at «All member
names used in a JSON API document MUST be treated as case sensitive by
clients and servers».

Det enkleste er antagelig å forklare eksplisitt at det skilles mellom
store og små bokstaver, for å unngå problemet med språkspesifikk
omforming til store eller små bokstaver.

Ønsket endring
--------------

Foreslår at følgende setning legges inn under punkt 6.1.1 (REST
tjenestene) på side 11 for å gjøre det klart hvordan alle navn skal
håndteres:

> Det skilles mellom små og store tegn i alle XML- og JSON-attributter
> og HATEOS-relasjoner, slik at disse har entydig definerte navn som
> ikke er avhengig av språkspesifikke regler for konvertering mellom
> små og store tegn.

I tillegg bør 'systemid' endres til 'systemID' på side 141, 148, 253,
258 og 263, hvis de er ment å være attributtnavn og ikke typenavn.
Har kun lett etter 'systemid'-inkonsistenser.  Det kan være flere.

Respons
-------

Ingen respons fra Arkivverket så langt.
