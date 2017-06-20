Kan en sette verdien tom streng ok i et påkrevd felt?
=====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  ?
       Meldingstype  ?
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er flere påkrevde felt for objekter i tjenestegrensesnittet, men
det står ingen steder i spesifikasjonen om hvorvidt hva som er
ugyldige verdier i JSON for slike felt.  Feltet arkiv.tittel er i
følge spesifikasjonen en tekststring som må være satt.  Dette tolker
vi til at en verdi satt til null ikke er tillatt, dvs at dette ikke er
lov:

```
{
  "tittel": null,
  ...
}
```

Et spørsmål som melder seg er om den kan være satt til en tom
tekststreng, dvs om dette er tillatt:

```
{
  "tittel": "",
  ...
}
```

Det virker mest fornuftig å både avvise null og "" som gydlige verdier.

Ønsket endring
--------------

Endre i del 7.1 blokken om "Multiplisiteten på side 31, legg til
følgende setning etter "En Klasse skal alltid ha en klasseID, og kan
bare ha en":

> En om tekststreng-verdi er likestilt med en manglende verdi, slik at
> i dette tilfellet betyr det at klasseID må ha en verdi forskjellig
> fra tom streng.
