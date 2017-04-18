Klargjøring av  innlogging og tilgangskontroll
==============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  pere@hungry.com
        Dokumentdel  4.1
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I punkt 4.1 (Autentisering) på side 9 står det at 'Single Sign On bør
støttes'.  Hva betyr dette?  Er det Kerberos-autentisering ala det
Microsoft Active Directory tilbyr, eller noe annet?

Det står også at "NOARK5 kjerne må ha metoder for å autentisere
brukere og gi de riktige tilganger til kjernen".  Hva slags
granularitet kreves?  Bør det kreves at en må kunne gi tilganger ved
hjelp av rettighetsgrupper, for å slippe manuelt vedlikehold av
brukerrettigheter?

Må en logge inn før en kan bruke API-et, eller er det noen deler som
er tilgjengelig uten innlogging?  Hvordan finner klienten hvor/hvordan
innlogging skal gjøres?  Kanskje det bør være en relasjon på toppnivå
som viser hvor innlogging skal gjøres?

Se også side 253.


Ønsket endring
--------------

FIXME Hva kan foreslås her?
