Hva skal statuskode være etter opplasting av små filer?
=======================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9 (Hente og overføre filer)
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  2019-05-22
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette er relatert til mangelmelding #25 og endringsforslag #70, og
inneholder en klargjøring som manglet der.

Det står ikke noe i spesifikasjonen om hvilken statuskode som skal
returneres etter at en liten fil er lastet opp.  For store filer som
lastes opp i bulk, så skal det returneres 201 når opplastingen er
ferdig.  Tidligere returnerte Nikita 200 ved opplasting (før den fikk
støtte for bulkopplasting), men nå returnerer den 201 også for små
filer.  Personlig antok jeg 200 var riktig statuskode for små filer,
hvilket demonstrerer at spesifikasjonen mangler en liten detalj her.
Jeg oppdaget endringen i Nikita da et av mine skript sluttet å
fungere.  Det er et åpent spørsmål hvilken kode skal brukes.  Det bør
stå eksplisitt i spesifikasjonen.

Ønsket endring
--------------

Foreslår at begge opplastingsmetodene, for både små og store filer,
returnerer samme statuskode når opplastingen er vellykket, og at dette
er 201 Created.  Det bør legges inn en 'Respons: 201 Created' etter
POST-eksemplet under overskriften **Overføre små filer** i kapittel 6,
like før overskriften **Overføre store filer**.  I tillegg bør det
nevnes eksplisitt i teksten hvilken returkode som skal returneres.

Jeg sender inn konkret forslag til endring som patch via github.


Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/191 .
