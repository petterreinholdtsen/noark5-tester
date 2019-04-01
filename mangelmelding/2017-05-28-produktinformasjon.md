Definert måte å hente ut produktinformasjon om tjenestegrensesnittet
====================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
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
det skal lages uttrekk med navn på systemet/løsningen.

Det hadde dermed vært en fordel om det ble definert i spesifikasjonen
for tjenestegrensesnittet en relasjon på toppnivå som peker til URL
der slik informasjon kan finnes.  Det kan f.eks. returneres et
JSON-objekt med aktuelle attributter.  Vi ønsker oss noe ala dette:

 * `leverandoer` - tekststreng med navn på leverandør av
               tjenestegrensesnittimplementasjonen.
 * `produkt` - tekststreng med navn på produktet som leverer
               tjenestegrensesnittet.
 * `versjon` - tekststreng med versjon for produktet fra leverandøren.
 
 * `versjonsdato` - tekststreng med dato for når produktet ble lansert
               / programmet ble sist oppdatert.
 * `protokollversjon` - tekststreng med versjon av
               tjenestegrensesnittspesifikasjonen som støttes.
               For dagens utgave vil verdien være '1.0 beta'.

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

FIXME sjekk om listen er riktig og komplett.

Ønsket endring
--------------

FIXME skriv konkret forslag.  hvor bør teksten inn?

Det legges inn en ny relasjon
`http://rel.kxml.no/noark5/v4/api/tjenesteinfo/` på toppnivå der GET
på tlihørende href returnerer en struktur ala dette:


```Python
{
  "leverandoer": "Nikita-prosjektet",
  "produkt": "Nikita Noark 5-kjerne",
  "versjon": "0.3",
  "versjonsdato": "2019-03-22",
  "protokollversjon": "1.0 Beta"
}
```

Det trengs en ny entitetsbeskrivelse i kapittel 7 for dette.  Tenker
den kan legges inn helt på slutten.  Kanskje den bør legges inn som
del av 'admin'-pakke i stedet for å lage et nytt toppnivå i
relasjons-URLene?
