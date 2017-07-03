Hvordan defineres relasjoner mellom mappe og undermappe?
===================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.16
         Sidenummer  134
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder del 7.2.1.16 (Mappe).

Listen over relasjonsnøkler på sidene 133-134 viser at en kan få ut oversikt over undermapper ved å benytte relasjonen
.../arkivstruktur/undermappe/, men har ingen relasjon ny-undermappe/ for å
opprette et nytt undermappe.  Hvordan er det mening at en skal opprette et nytt undermappe knyttet til et mappe?

Det er uklart hva som er forskjellen på relasjonene 'mappe' og
'undermappe'.  I følge UML-skjema er ethvert mappe koblet under et
annet mappe et undermappe.  

_Er det et eller en mappe??_

Det virker dermed nærliggende å tro at
relasjonen .../arkivstruktur/undermappe/ er en skrivefeil.  Hvis ikke,
må det forklares hva som er forskjellen på mappe- og
undermappe-relasjonene for klassen mappe.

Jeg foreslår at relasjonen 'undermappe' fjernes og at kun relasjonene
'mappe/' og 'ny-mappe/' brukes til å finne og opprette undermappe. 
Følgende brukes for å illustrere dette.

For å opprette en undermappe kan følgende href brukes:

   POST [contextpath][api]/arkivstruktur/mappe/{systemID}/ny-mappe

For å hente en liste av undermappe kan følgende href brukes:

   GET [contextpath][api]/arkivstruktur/mappe/{systemID}/mappe

Merk, det er en tilsvarende situasjon for arkiv/underarkiv, der det
kun finnes relasjoner for å opprette 'arkiv', men ingen relasjoner for å
liste opp både 'arkiv' og 'underarkiv'.

Ønsket endring
--------------

> Lenker til undermappe.

Fjern duplikat-Aggregation med kilde undermappe som er både på side 133 og 132.

Fjern relasjonen
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/` fra
listen over relasjonsnøkler på side 134.
