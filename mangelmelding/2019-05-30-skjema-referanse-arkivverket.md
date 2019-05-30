Autorativ kilde til skjema for overføringsformat bør være under arkivverket.no
==============================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  krever klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.8 (Overføringsformat)
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I 6.1.1.8 (Overføringsformat) på side 25 står det følgende:

> Overføringsformat skal være i henhold til følgende skjema for begge innholdstyper:
> 
>   - http://skjema.kxml.no/arkivverket/noark5/v4.0/

Av årsaker beskrevet i mangelmelding #23 bør URL til autorativ kilde
for spesifikasjonens skjema eies av Arkivverket, eller i hvert fall
sikre at Arkivverket i fremtiden kan peke URL-en til et sted de
kontrollerer.  Det kan løses ved å legge ut aktuelle skjemaer på en URL
med DNS-navn eid av Arkivverket, eventuelt la skjema.arkivverket.no
peke til skjema.kxml.no og endre URL i 6.1.1.8 til
http://skjema.arkivverket.no/arkivverket/noark5/v4.0/.


Det er uklart for meg hvorfor det henvises til et XML-skjema på
eksternt nettsted i spesifikasjonen.  Det åpner jo for at
overføringsformat kan endres uavhengig av spesifikasjonen.
Beskrivelsen av JSON er og bør være i spesifikasjonsteksten, og XML
bør som nevnt i mangelmelding #57 droppes.  Foreslår derfor å fjerne
kapittel 6.1.1.8 fra spesifikasjonen.

Ønsket endring
--------------

Fjern følgende fra 6.1.1.8 (Overføringsformat) på side 25:

> Overføringsformat skal være i henhold til følgende skjema for begge innholdstyper:
> 
>   - http://skjema.kxml.no/arkivverket/noark5/v4.0/
