Definert måte å hente ut produktinformasjon om tjenestegrensesnittet
====================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
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

FIXME sjekk om listen er riktig og komplett.

FIXME versjon og versjonsdato kan være sikkerhetsmessig utfordrende å gi ut.

Ønsket endring
--------------

FIXME skriv konkret forslag.  hvor bør teksten inn?
