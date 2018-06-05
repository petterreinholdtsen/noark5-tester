Hva er gyldighetsområdet for versjonsnummer (M005) i dokumentobjekt?
====================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.7
         Sidenummer  101
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonens del 7.2.1.7 (Dokumentobjekt) side 101 nevner ikke hva
som er gyldige verdier for versjonsnummer i dokumentobjekt.  Den
forklarer heller ikke hvilken verdi versjonnummeret som tildeltes et
nytt dokument skal ha.  Skal det være 0, 1 eller et annet tall.

Svarene på disse spørsmålene er heller ikke oppgitt i Noark
5-spesifikasjonen.  Noark 5-spesifikasjonens del 5.6
(Dokumentbeskrivelse og Dokumentobjekt) side 71 sier bare at
versjonummer er

> Identifikasjon av versjoner innenfor samme dokument.  Se også
> merknad 1 nedenfor.

Merknaden nedenfor forteller ikke mer om gyldighetsområde:

> Merknad 
> 1. Det er her snakk om arkiverte versjoner av samme dokument. Alle
> de arkiverte variantene skal tas med ved en deponering/avlevering.

For å sikre at alle implementasjoner teller versjoner på samme måte og
er i stand til å håndtere hverandres verdier bør dette klargjøres i
spesifikasjonen.

I følge metadatakatalogen i Noark 5 versjon 5 er versjonsnummer (M005)
av typen 'integer' fra http://www.w3.org/2001/XMLSchema, dvs alle
heltall i det uendelige settet {...,-2,-1,0,1,2,...}.  Hvis
versjonsnummer kan være uendelig stort, så er det litt utfordrende
både for de som skal lage og bruke tjenestegrensesnittet.  Kanskje det
er greit å begrense det i spesifikasjonen for tjenestegrensesnittet,
samt forklare hva som skal gjøres hvis det går over maksgrensen?

Gitt at det sjelden er mange versjoner av et dokument i arkivet, så
kan det være greit å si at verdien er positivt 32-bits tall, dvs. at
versjonsnummer går fra 0 til 2^31-1 = 2147483647.  Det burde holde.
Spørmålet er hva som skal gjøres hvis en har versjon 2147483647 og
ønsker å laste opp en ny versjon.  Det er to åpenbare muligheter.
Enten må dokumentet nektes arkivert, eller så må det opprettes et nytt
dokument med versjonsnummer 0.  Det siste virker å være eneste
fornuftige løsning, da å nekte arkivering av et dokument vel ikke er
lovlig.

FIXME hvordan håndteres det at kun arkivversjoner av dokumenter skal
ha versjonsnummer?

Ønsket endring
--------------

Klargjør hva som er minste og største mulige verdi for versjonsnummer,
hva som er første verdi og hvorvidt verdien skal stige eller synke for
hver ny versjon.

FIXME formuler tekstforslag.

