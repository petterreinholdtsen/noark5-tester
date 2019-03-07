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
nytt dokument skal ha.  Skal det være 0, 1 eller et annet tall.  Den
sier heller ingenting om versjoner skal tildeles med stigende eller
fallende rekkefølge.

Svarene på disse spørsmålene er heller ikke oppgitt i Noark
5-spesifikasjonen, hverken versjon 4 eller 5.  Noark
5-spesifikasjonens versjon 4 del 5.6 (Dokumentbeskrivelse og
Dokumentobjekt) side 71 sier bare at versjonummer er

> Identifikasjon av versjoner innenfor samme dokument.  Se også
> merknad 1 nedenfor.

Merknaden det henvises til nedenfor forteller ikke mer om aktuelle
verdier og gyldighetsområde:

> Merknad 
> 1. Det er her snakk om arkiverte versjoner av samme dokument. Alle
> de arkiverte variantene skal tas med ved en deponering/avlevering.

For å sikre at alle implementasjoner av tjenestegrensesnittet teller
versjoner på samme måte og at en klient er i stand til å håndtere
enhver implementasjons verdier bør bruken av versjonsnummer klargjøres
i spesifikasjonen.

I følge metadatakatalogen i Noark 5 versjon 5 er versjonsnummer (M005)
av typen 'integer' fra http://www.w3.org/2001/XMLSchema, dvs alle
heltall i det uendelige settet {...,-2,-1,0,1,2,...}.  Hvis
versjonsnummer kan være uendelig stort, så er det litt utfordrende
både for de som skal lage og bruke tjenestegrensesnittet.  Kanskje det
er bedre å begrense i spesifikasjonen for tjenestegrensesnittet hvilke
verdier feltet kan ha, samt forklare hva som skal gjøres hvis det går
over maksgrensen?

Gitt at det sjelden er mange versjoner av et dokument i arkivet, så
kan det være greit å si at verdien er et positivt 32-bits tall, dvs. at
versjonsnummer går fra 0 til 2^31-1 = 2147483647.  Erfaring fra dagens
arkiver tyder på at det holder.  Et spørsmål med begrenset verdiområde
er hva som skal gjøres hvis en har kommet til versjon 2147483647 og
ønsker å laste opp en ny versjon.  Det er to åpenbare muligheter.
Enten må dokumentet nektes arkivert, eller så må det opprettes et nytt
dokument med versjonsnummer 0.  Det siste virker å være eneste
fornuftige løsning, da å nekte arkivering av et dokument er vel ikke
lovlig.  Alternativt kan verdien stige eller synke i det uendenlige,
og implementasjoner må håndtere dette på vanlig måte.

Det er uklart om det er greit med hull i versjonsnummer-serien.  Slike
hull vil oppstå hvis en (midlertidig) versjon av det dokument blir
lagret i arkivet for å å bli erstattet med en endelig versjon og det
midlertidige versjonen slettes.  Det bør nevnes om det er akseptabelt
med versjonsnummerhull eller ikke.  Alternativet er at dokumenter får
nye versjonsnummer hvis et dokument slettes, med de utfordringer det
gir.

Jeg tror det er best å telle versjonsnummer oppover fra 0, akseptere
hull og ikke ha øvre begrensning på versjonsnummer.

Ønsket endring
--------------

Klargjør hva som er første verdi for versjonsnummer lastet inn i
tjenestegrensesnittet, og om neste dokument får større eller mindre
versjon enn første dokument.  Dokumenter at versjonummer deles ut
sekvensielt uten hull, men at hull kan oppstå når tidligere versjoner
slettes.

Klargjør også om det er en minste eller største verdi for
versjonsnummer, og hva som eventuelt skal gjøres hvis en kommer til
grensen og ønsker laste opp nok en versjon.

Endre definisjonen av versjonsnummer for klassen dokumentobjekt, endre
"Identifikasjon av versjoner innenfor ett og samme dokument" til

> Identifikasjon av versjoner innenfor ett og samme dokument.  Første
> versjon får nummer 0, deretter påfølgende heltall i stigende
> rekkefølge (1, 2, 3, ...).  Det er ok med "hull" i
> versjonsnummer-sekvensen, da dette dokumenterer hvilke tidligere
> versjoner av dokumentet som er fjernet.
