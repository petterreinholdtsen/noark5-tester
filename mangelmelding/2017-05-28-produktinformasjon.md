Definert måte å hente ut produktinformasjon fra tjenestegrensesnittet
=====================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6
         Sidenummer  13
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er nyttig å kunne hente ut informasjon via selve webtjenesten om
programvaren som tilbyr tjenestegrensesnittet.  Dette er
hensiktsmessig når det skal feilsøkes (vite hvilket produkt og versjon
som benyttes hvis oppførselen har endret seg over tid), og også når
det skal lages uttrekk med navn på systemet/løsningen (i
arkivuttrekk.xml sitt systemName-felt).

Det hadde dermed vært en fordel om det ble definert i spesifikasjonen
for tjenestegrensesnittet en relasjon på toppnivå som peker til URL
der slik informasjon kan finnes.  Det kan f.eks. returneres et
JSON-objekt med aktuelle attributter.

Det kan være en sikkerhetsmessig utfordring å dele ut versjon og
versjonsdato offentlig, når det er sikkerhetsproblemer med en gitt
API-implementasjon.  Det bør derfor vurderes om slik
produktinformasjon kun skal være tilgjengelig for innloggede brukere.

Det bør videre vurderes om en skal støtte flere protokollversjoner
(dvs. en liste med strenger i stedet for en streng), jamfør
diskusjonen i [mangelmelding
#71](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/71)
om hvordan en skal håndtere ikke-kompatible endringer i
API-spesifikasjonen

Ønsket endring
--------------

Legg inn ny relasjon/href i det som returneres fra toppnivå, dvs del
6.1.1.1 (Oppkobling og ressurslenker), med relasjonsnøkkel
`http://rel.kxml.no/noark5/v4/api/admin/system/`.

Legg inn følgende del foran del 6.1.1.2 (Finne objekter (Read)) på
side 13:

> #### Systeminformasjon
> 
> Når en tar GET mot href for relasjonsnøkkelen
> `http://rel.arkivverket.no/noark5/v4/api/admin/system/`, så får en informasjon
> om API-tjenersystemet.  Responsen inneholder følgende felter:
> 
>  * `leverandoer` - tekststreng med navn på leverandør av
>                tjenestegrensesnittimplementasjonen.
>  * `produkt` - tekststreng med navn på produktet som leverer
>                tjenestegrensesnittet.
>  * `versjon` - tekststreng med versjon for produktet fra leverandøren.
>  * `versjonsdato` - tekststreng med dato for når produktet ble lansert
>                / programmet ble sist oppdatert.
>  * `protokollversjon` - tekststreng med versjon av
>                tjenestegrensesnittspesifikasjonen som støttes.
>                For dagens utgave vil verdien være '1.0 beta'.
> 
> Responsen kan for eksempel se slik ut:
> 
> ```Python
> {
>   "leverandoer": "Hoffleverandøren",
>   "produkt": "Arkivsystemet Noark 5 kjerne",
>   "versjon": "0.1",
>   "versjonsdato": "2019-03-22",
>   "protokollversjon": "1.0 Beta"
> }
> ```
> 
> Det kan være en sikkerhetsmessig fordel å unngå å fortelle
> potensielle angripere hvilken versjon som kjører på maskinen.  Det
> kan derfor være lurt å kun gjøre dette endepunktet tilgjengelig for
> innloggede brukere.
