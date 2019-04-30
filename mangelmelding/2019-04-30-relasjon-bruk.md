Savner detaljert forklaring om hvordan relasjoner skal brukes
=============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det bør beskrives i detalj hvordan relasjoner vises frem i JSON, og
hvordan de opprettes og endres via API-et.  Det trengs beskrivelse for
relasjoner med multiplisitet 0..1, 1..1, 0..* og 1..*, da alle disse
neppe kan håndteres på samme måte.

Det bør også beskrives hva navnene i navngitte relasjoner skal brukes
til, for eksempel slik det vises relasjonen mellom Klasse og Mappe:

| **Relasjon**                             | **Kilde**                                                | **Mål**                | **Merknad** |
| ---------------------------------------- | -------------------------------------------------------- | ---------------------- | ----------- |
| **Aggregation** (Bi-Directional)           | mappe 0..* Mappe                                         | klasse 0..1 Klasse     |             |

Hvorfor er det navn på begge siden av relasjonen (henholdsvis 'mappe'
og 'klasse'), og hvordan skal disse navnene representeres i API-et?

Se
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/38
og ide til notasjon i
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/45 .

Ønsket endring
--------------

FIXME
