Definer mekanisme for tilbakemelding på konsistenssjekk
=======================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er ønskelig at arkivsystemet gjør konsistenssjekk av data som
legges inn i arkivet, og det mangler en beskrivelse i
tjenestegrensesnittet om hvordan tilbakemelding fra slik
konsistenssjekk skal sendes tilbake til klienter som legger inn data i
arkivet.

Her er noen eksempler på slike konsistenssjekker:

 * Kontrollere at metadata gir tidsmessig mening.  For eksemepel vil
   dokumentdato være før journaldato i normale tilfeller, og
   dokumentdato vil ikke være veldig langt inn i for- eller fremtiden.

 * Sammenligne metadata i opplastet fil med metadata registrert i
   arkivstrukturen, rapporter hvis de ikke ligner.

 * Graderte dokumenter er nyere enn foreldelsesfristene for
   graderingen.

 * Navn og organisasjonsnummer på KorrespondansepartEnhet stemmer ikke
   over ens med det som står i brønnøysundsregisteret.

 * Postnummeret brukt i en korrespondanseenhet finnes ikke.

 * Det opplastede dokumentet har et format som ikke aksepteres av
   arkivverket for langtidsoppbevaring.

 * Det opplastede dokumentet er et interakivt regneark, eller et
   regneark som gjør oppslag i ekstern database som del av
   beregninger, som dermed ikke kan automatisk konverteres til PDF på
   meningsfylt vis.

Slike feil er ofte resultat av manuelle skrivefeil, og bør oppdages så
raskt som mulig for å holde kvaliteten i arkivsystemet oppe.

Slik konsistenssjekk kan gjøres når ny entitet opprettes med POST Til
ny-* eller når en entitet oppdateres med PUT.  Det er dermed fint om
resultatet fra slike konsistenssjekker kan være del av svaret som
kommer fra POST og PUT.

En lite inngripende måte å gjøre dette på er å legge ved en ekstra
relasjon i _links hvis konsistenssjekken har oppdaget noe rart, og så
peke href-verdien til et sted der detaljer om hva som ble oppdaget
returneres.  Det gjør at klienter som ikke forstår
konsistenssjekk-tilbakemeldingen kan ignorere den, mens klienter som
forstår relasjonen kan vise frem detaljene til brukeren, i tilfelle
det for eksempel er skrivefeil som brukeren kan korrigere.

Det som trengs for å få dette til er en definisjon av hva
Konsistenssjekk-resultatene skal returnerer, og å definere en
relasjonsnøkkel som API-klienter kan se etter etter å ha opprettet
eller endret en instans.

http://edu.oslomet.no/ark2100/h16/syllabus/DQ%20Ouzounov.pdf

Ønsket endring
--------------

Jeg er litt usikker på hvordan denne mekanismen legges inn i
spesififikasjonen.  Holder det med en beskrivelse av mekanismen med
eksempler i kapittel 6, eller trengs det også entitetsbeskrivelser i
kapittel 7?


FIXME kanskje behandle konsistenssjekk-resultater som en variant av
feilmelding, der alvorlighet ikke er fatal, men litt lavere (dvs. når
kode=200 i forslaget i [mangelmelding
#93](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/93)?


FIXME dokumenter hvordan dette skal gjøres og hvordan resultatet fra
konsistenssjekken skal se ut.  Det trengs en beskrivelse i kapittel 6
av mekanismen med eksempler.  Trengs det også en klassebeskrivelse i
kapittel 7?

Ide: ny entitet KonsistensVarsel med følgende felt:

 * felt
 * type
 * alvorlighet
 * beskrivelse

Eksempel på GET mot href for konsistenssjekk-relasjon:

```
{
  "results": [
    {
      "felt": "dokumentdato",
      "varslingstype": "Usannsynlig verdi",
      "melding" : "Datoen er i fremtiden"
    }
  ]
}
```

Kodeliste.KonsistensVarselNivaa:
  * Kritisk = 4
  * Alvorlig = 3
  * Advarsel = 2
  * Tips = 1

FIXME Ny kodeliste for varslingstyper og alvorlighet?

FIXME Hvilket språk skal meldingene ha?  Hvordan skal en håndtere flere språk?
