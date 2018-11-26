Kan en sette verdien «tom streng» i et påkrevd felt?
====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.1
         Sidenummer  31
        Linjenummer  n/a
    Innsendingsdato  2017-07-03
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er flere påkrevde felt for objekter i tjenestegrensesnittet, men
det står ingen steder i spesifikasjonen om hva som er ugyldige
JSON-verdier for slike felt.  Et eksempel er feltet arkiv.tittel som i
følge spesifikasjonen er en tekststreng som må være satt.  En naturlig
tolkning av dette er at JSON-verdi satt til null ikke er tillatt, dvs
at dette ikke er lov:

```
{
  "tittel": null,
  ...
}
```

Men et spørsmål som melder seg er om feltet kan være satt til en tom
tekststreng, dvs om dette er tillatt:

```
{
  "tittel": "",
  ...
}
```

Det virker mest fornuftig å avvise både null og `""` som gyldige
verdier, for å sikre at tittelen kan vises frem og har et reelt
innhold.

Det er ikke åpenbart hvor i spesifikasjonen det bør klargjøres.  Det
virker mest fornuftig å legge det inn under 7 (Tjenester og
informasjonsmodell), men det kan også legges inn under både 4
(Teknologi) og 6 (Konsepter og prinsipper).

Ønsket endring
--------------

Endre i del 7.1, blokken om «Multiplisiteten» på side 31, legg til
følgende setning etter «En Klasse skal alltid ha en klasseID, og kan
bare ha en.»:

> En tom tekststreng-verdi (`""`) er likestilt med en manglende verdi,
> slik at ved multiplisiteten [1..1] betyr det at klasseID også må ha
> en verdi forskjellig fra tom streng.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/39 .
