Ubeskrevet relasjonsnøkkel .../avslutt-mappe/ i eksempel
========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.3 (
         Sidenummer  16
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I to eksempler i kapittel 6 i del 6.1.1.3 (Opprette objekter (Create))
på side 18 og 6.1.1.4 (Oppdatere objekter (Update)) på side 20 så er
det en \_links-oppføring med relasjonsnøkkel
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/avslutt-mappe/`:

```Python
{
    "href": "http://localhost:49708/api/arkivstruktur/Mappe/515c45b5-e903-4320-a085-2a98813878ba/avslutt",
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/avslutt-mappe/",
},
```

Denne relasjonsnøkkelen er ikke nevnt i kapittel 7 for Mappe, og er
heller ikke dokumentert noe annet sted i spesifikasjonen.

Ønsket endring
--------------

FIXME Finn ut hva som er meningen her.  Tror det skal være mekanisme
for å avslutte mappe, som har ekstra kontroll med alle underliggende
registreringer.
