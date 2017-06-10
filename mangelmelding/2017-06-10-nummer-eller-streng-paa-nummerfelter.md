Hvordan skal formatet på som inneholder nummer se ut
===================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  FIXME
         Sidenummer  FIXME
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------
Når man laster opp et objekt som inneholder et nummer så er det vanlig
at det ikke er parantes tegn rundt verdien. Allikevel kan det lett forekomme
fra en del automatiserte løsninger at det sette parantes tegn rundt felter, 
spesielt når det kommer via internett.

dokumentnummer er et slik felt som er et nummer og følgende eksempel
illustrerer hvordan det ser ut parantes og uten

{dokumentnummer: "12"}
{dokumentnummer: 12}

vi ser at det ikke er eksplisit beskrevet at nummerfelt skal ikke ha
parantes rundt seg. Tallet 12 og strengen "12" begge representerer verdien
12. Hvis det er ønskelig at det ikke skal være mulig for en klient å velge
å bruke parantes for tall så bør det nevnes eksplisitt.

FIXME: Er det beskrevet via at de nevner et annet standard

Ønsket endring
--------------
FIXME

Det må komme tydelig fram at felt som inneholder nummer kan 
