Hvordan skal felt med tallverdi formateres i JSON?
==================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.2 (Validering av data)
         Sidenummer  28
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Når man laster opp et objekt som inneholder et felt med tallverdi så
sier JSON-definisjone både i [IETF RFC
4627](https://www.ietf.org/rfc/rfc4627.txt) og på
[json.org](http://www.json.org/) at det ikke skal være anførsestegn
rundt tallverdien.  Allikevel kan det lett forekomme at en del
automatiserte løsninger sette anførsestegn rundt tallfelt, spesielt
når det kommer via internett.  For eksempel vil ofte tall som legges
inn via et webskjema være tekststrenger og ikke tall når de sendes
inn.

Et eksempel er attributten dokumentnummer (M007) i klassen
Dokumentbeskrivelse, som er et slik heltallsfelt.  Her er en
illustrasjon på hvordan feltet kan se ut, med og uten anførsestegn:

```
{ dokumentnummer: "12" }
{ dokumentnummer: 12 }
```

Spesifikasjonen beskriver ikke eksplisitt om en tallverdi skal ha
anførselstegn rundt seg eller ikke.  Tallet 12 og strengen "12"
representerer begge verdien 12. Hvis det er ønskelig at det ikke skal
være mulig for en klient å velge å bruke anførses rundt tallverdier så bør
det nevnes eksplisitt i spesifikasjonen.  Det er enklest å
implementere mottakerenden av tjenestegrensesnittet hvis det ikke er
tillatt med anførselstegn rundt tallverdier, mens det er enklest å
implementere senderenden hvis det er valgfritt.

Det bør spesifiseres hva som forventes av sender og mottaker av
tjenestegrensesnittet.  Jeg anbefaler at en ikke lar det være
valgfritt om tall skal oppgis med anførselstegn eller ikke, for å
sikre at protokollen er entydig.

Ønsket endring
--------------

Legg inn nytt avsnitt tre i del 6.2 (Validering av Data) etter
avsnittet som starter med "Restriksjoner som er dokumenterte under":

> Merk at tallfelt som overføres som JSON alltid skal overføres
> formatert som et JSON Number, dvs. uten anførselstegn.
