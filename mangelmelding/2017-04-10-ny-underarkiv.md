Hvordan defineres relasjoner mellom arkiv og underarkiv?
========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.1
         Sidenummer  57
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder del 7.2.1.1 (Arkiv).

Listen over relasjonsnøkler på side 57 viser at en kan få ut oversikt
over underarkiv ved å benytte relasjonen
.../arkivstruktur/underarkiv/, men har ingen ny-underarkiv/ for a
opprette et nytt underarkiv.  Det er relasjonspar for
arkivskaper/ny-arkivskaper, arkivdel/ny-arkivdel, arkiv/ny-arkiv men
ikke for underarkiv.  Hvordan er det mening at en skal opprette et
nytt underarkiv knyttet til et arkiv?

Det er uklart hva som er forskjellen på relasjonene 'arkiv' og
'underarkiv'.  I følge UML-skjema er ethvert arkiv koblet under et
annet arkiv et underarkiv.  Det virker dermed nærliggende å tro at
relasjonen .../arkivstruktur/underarkiv/ er en skrivefeil.  Hvis ikke,
må det forklares hva som er forskjellen på arkiv- og
underarkiv-relasjonene for klassen Arkiv.

Jeg foreslår at relasjonen 'underarkiv' fjernes og at kun relasjonene
'arkiv/' og 'ny-arkiv/' brukes til å finne og opprette underarkiv. 
Følgende brukes for å illustrere dette.

For å opprette en underarkiv skal en dermed bruke POST til href knyttet til
rel-verdien  
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkiv/`.
 
Den kan for eksempel angi en slik struktur:

 * POST `[contextpath][api]/arkivstruktur/arkiv/{systemID}/ny-arkiv`   

For å hente en liste av underarkiv skal en dermed bruke  GET til href knyttet
til rel-verdien  
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/`.
 
Den kan for eksempel angi en slik struktur:

 * GET `[contextpath][api]/arkivstruktur/arkiv/{systemID}/arkiv`

Merk, det er en tilsvarende situasjon for mappe/undermappe, der det
kun finnes relasjoner for å opprette 'mappe', men ingen relasjoner for å
liste opp både 'mappe' og 'undermappe'.

Ønsket endring
--------------

I del 7.2.1.1 (Arkiv), endre følgende setning i siste avsnitt i
beskrivelsen av klassen på side 56:

> Toppnivået skal bare ha én forekomst, men kan ha ett eller flere
> undernivåer, se om underarkiv nedenfor.

Endres til følgende:

> Toppnivået skal bare ha én forekomst, men kan ha ett eller flere
> undernivåer, se om underarkiv nedenfor.  Underarkiv opprettes ved å
> bruke arkiv-objektets relasjon  
> `http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkiv/`
> og listes
> opp ved å bruke arkiv-objektets relasjon
> `http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/`.

Endre i relasjonslisten på side 56, endre Kilde 'undearkiv' til
'arkiv' og legg inn følgende merknad:

> Lenker til underarkiv.

Fjern duplikat-Aggregation med kilde underarkiv på side 57 (identisk
med første relasjon i listen).

Fjern relasjonen
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/underarkiv/` fra
listen over relasjonsnøkler på side 57.
