Gjør konverteringsverdier obligatoriske slik de er i versjon 3.1 og 5
=====================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.14 (Konvertering)
         Sidenummer  128
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I Noark 5 versjon 3.1 og versjon 5.0 så er feltene M714
konverteringsverktoey og M715 konverteringskommentar i
arkivstruktur.xsd gjort obligatoriske, mens i versjon 4.0 er de gjort
valgfrie.  Dette får meg til å tro at det var en feil at disse feltene
ble gjort valgfrie i versjon 4.  Gitt den antagelsen, så bør
tjenestegrensesnittet endres slik at disse er obligatoriske også her,
for å være foroverkompatibel med versjon 5.0.

Dette er relatert til mangelmelding #71 om overgang til Noark 5
versjon 5.

Ønsket endring
--------------

Endre multiplisitet for konverteringsverktoey og
konverteringskommentar fra 0..1 til 1..1 under 7.2.1.14 (Konvertering)
på side 128.
