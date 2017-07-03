Hvordan defineres relasjoner mellom mappe og undermappe?
========================================================

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

Listen over relasjonsnøkler for klassen Mappe på sidene 133-134 viser
at en kan få ut oversikt over undermapper ved å benytte relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/, men har
ingen tilsvarende relasjon ny-undermappe/ for å *opprette* en ny
undermappe.  Hvordan er det mening at en skal opprette en nytt
undermappe knyttet til et mappe?

I listen over relasjonsnøkler finnes relasjonene
http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/ og
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/, men det er
uklart hva som er forskjellen på relasjonene 'mappe' og 'undermappe'.
I følge UML-skjema er enhvert mappe som er koblet under en annet mappe
en undermappe.  Det virker dermed som om relasjonene for 'mappe' og
'undermappe' er redundante.

Det virker dermed nærliggende å tro at relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/ er en
skrivefeil.  Hvis det ikke er en skrivefeil bør det forklares i
spesifikasjonen hva som er forskjellen på mappe- og
undermappe-relasjonene for klassen Mappe.

En mulig tolkning er at relasjonen 'mappe' peker til
"foreldre"-mappen, mens 'undermappe' peker til undermapper, men en
slik tolkning gir ikke mening når det eksisterer en relasjon
'ny-mappe' men ingen 'ny-undermappe'.

Jeg foreslår at relasjonen 'undermappe' fjernes og at kun relasjonene
'mappe/' og 'ny-mappe/' brukes til å finne og opprette undermappe.
Følgende brukes for å illustrere dette.

For å opprette en undermappe kan følgende href brukes:

   POST [contextpath][api]/arkivstruktur/mappe/{systemID}/ny-mappe

For å hente en liste av undermappe kan følgende href brukes:

   GET [contextpath][api]/arkivstruktur/mappe/{systemID}/mappe

Merk, det er en tilsvarende situasjon for arkiv/underarkiv i del
7.2.1.1 side 57, der det kun finnes relasjon 'ny-arkiv' for å opprette
'arkiv', og ingen relasjon 'ny-underarkiv'.  Det finnes derimot
relasjoner for å liste opp både 'arkiv' og 'underarkiv'.

Ønsket endring
--------------

Fjern duplikat-Aggregation med kilde undermappe som er både på side
133 og 132.

Fjern relasjonen
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/` fra
listen over relasjonsnøkler på side 134.
