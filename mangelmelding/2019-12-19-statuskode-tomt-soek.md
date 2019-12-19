Skal statuskode 200 eller 404 returneres for søk uten resultat?
===============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6 (Filter og tilgangsstyring)
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I spesifikasjonen står det hva slags JSON-struktur som skal returneres
for et søk som ikke returnerer noen instanser, men det står intet om
hvilken statuskode som skal brukes.  Det er to åpenbare kandidater:
200 OK og 404 Not Found.  Begge gir mening på sitt vis, da det jo ikke
ble funnet noen instanser (aka 404), og søket fullførte uten feil (aka
200).  Nikita har hatt begge oppførslene, og det har skapt problemer
for API-klienter.

Da et søk som ikke finner noe ikke er en feil, og 4XX-serien av koder
er feilkoder, virker det mest fornuftig og minst overraskende å
returnere 200.

For å sikre at alle implementasjoner av tjenestegrensesnittet oppfører
seg likt så bør det stå eksplisitt i spesifikasjonen hva som skal
returneres i dette tilfellet.

Ønsket endring
--------------

Endre setning i kapittel 6 fra følgende

> Når en forespurt listeressurs fra databasen er tom returneres medlem
> «count» satt til 0, intet medlem «results», samt relevante
> relasjonsnøkler i «_links» inkludert en «self»-relasjon tilbake til
> forespørselen som produserte den tomme listen.

til dette, der "statuskode 200, " er lagt til:

> Når en forespurt listeressurs fra databasen er tom returneres
> statuskode 200, medlem «count» satt til 0, intet medlem «results»,
> samt relevante relasjonsnøkler i «_links» inkludert en «self»-relasjon
> tilbake til forespørselen som produserte den tomme listen.
