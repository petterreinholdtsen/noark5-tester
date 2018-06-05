Klargjøring av innlogging og tilgangskontroll
=============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  pere@hungry.com
        Dokumentdel  4.1
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I punkt 4.1 (Autentisering) på side 9 står det at «Single Sign On bør
støttes».  Hva konkret betyr dette?  Er det Kerberos-autentisering ala
det Microsoft Active Directory tilbyr, eller noe annet?

Det står også at «NOARK5 kjerne må ha metoder for å autentisere
brukere og gi de riktige tilganger til kjernen».  Hva betyr dette?
Hva er «de riktige tilganger»?  Hva slags granularitet kreves,
dvs. hvor finkornet tilgangsstyring skal tjenestegrensesnittet ha?  Er
det nok med tilgang / ikke tilgang til API-et, eller for å ta et annet
ytterpunkt, må tilgangen kunne styres pr. entitet eller attributt?
Det virker ut fra Tilgangskategori-kodelisten i figur 32 på side 253
at tilgang skal kunne gis pr. arkivdel, klasse, mappe, registrering og
dokumentbeskrivelse, men har ikke funnet noe klart krav i
spesifikasjonen på hva som kreves.

Et relatert spørsmål er om en må logge inn før en kan bruke API-et,
eller er det noen deler som er tilgjengelig uten innlogging?

Et vels å viktig spørsmål er hvordan klienten finner hvor/hvordan
innlogging skal gjøres?  Vi foreslår en eller flere relasjon på
toppnivå som peker til href som skal brukes til innlogging.

Bør spesifikasjonen kreve at en må kunne gi tilganger ved hjelp av
rettighetsgrupper, for å slippe manuelt vedlikehold av hvem som får
lov til hva?

FIXME Se UML-diagramet på side 253 om brukere og tilgang og del 7.2.4
(Admin), kanskje noe å forstå ut fra den?

Ønsket endring
--------------

FIXME Hva kan foreslås her?

Endre punkt 4.1 side 9 til å ta med referanse til del 7.2.4 på side 253.

FIXME ta med relasjon for innlogging?

