Definer mekanisme for resultat fra automatisk kvalitetskontroll
===============================================================

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

Det er ønskelig at arkivsystemet gjør automatisk konsistenssjekk og
kvalitetskontroll av data som legges inn i arkivet, for å redusere
sjansen for at feil og unøyaktigheter i metadata.  Det mangler en
beskrivelse i tjenestegrensesnittet om hvordan tilbakemelding fra slik
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
konsistenssjekk-resultatene skal returnerer, og å definere en
relasjonsnøkkel som API-klienter kan se etter etter å ha opprettet
eller endret en instans.

En kan se på konsistenssjekk-resultater som en generalisert mekanisme
for feilmeldinger (se
[mangelmelding #93](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/93)).
Alvorlige resultater fører til at opprettelsen av objektet blir
avvist, mens mindre alvorlige resultater kun gir varsling om
problemer.

Hvis en bruker en ektra relasjon i _links, så vil det lite
hensiktsmessig være mulig å returnere samme struktur for feil og
problemer, da listen over feil som gjorde at opprettelsen ble avvist
jo må mellomlagres i ubestemt tidsrom, hvilket gjør det mer komplisert
å lage API-tjenesten som må ta vare på informasjon om forkastede
instanser utenom normal datastruktur.  På den andre siden kan det være
nyttig å ta vare på slike feilmeldinger for analyse og identifikasjon
av potensielle forbedringer på klientsiden.  Et alternativ til å ta
vare på slike feilmeldinger i ubestemt tidsrom kan være å bruke
"_embedded"-mekanismen beskrevet i utkastet til [JSON Hypertext
Application
Language](https://tools.ietf.org/html/draft-kelly-json-hal-08), der
alle detaljer følger med i responsen fra API-et.

Merk at en slik automatisert mekanisme for å returnere resultatene fra
konsisstenssjekk kan være et første steg på veien mot full
datakvalitetsmåling av arkivet, slik det for eksempel er beskrevet i
"[Assessing data quality in records management systems as implemented
in Noark
5](http://edu.oslomet.no/ark2100/h16/syllabus/DQ%20Ouzounov.pdf)" av
Dimitar Ouzounov.

Resultaten fra slik datakvalitet-sjekk bør inneholde

 * entitet som ble forsøkt opprettet, og eventuelt instans hvis den ble opprettet
 * alvorlighet på feilen (for eksempel kritisk, alvorlig, advarsel, tips)
 * navn på felt(er) som ga utslag i konsistenssjekken
 * type feil
 * beskrivelse/melding som beskriver sjekk som feilet

Kritiske feil bør føre til at opprettelsen/endring avvises, mens de
øvrige bør aksepteres med API-klient bør om mulig be bruker bekrefte
verdiene på nytt.

Resultatet fra slike kvalitetssjekker bør samles slik at
arkivansvarlig kan holde et øye med mengden slike feil.

For å kunne identifisere hvilke klient-type som produserer hvilke
typer feil, så bør API-et utvides til å kreve at klienten
identifiserer seg selv, for eksempel ved å bruke HTTP-hodetfelet
"User-Agent".  En vil dermed kunne hente ut statistikk over hva slags
feil ulike klienter produserer, som kan brukes til å identifisere
systematiske feil forårsaket av en defekt i klientprogrammet.

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

FIXME bør inneholde informasjon om hvilken entitet det gjelder

FIXME bør tillate API å ta vare på feilmeldinger en periode, med kjent utløpsdato, for analyse.  bør inkludere klientinformasjon.

FIXME klient bør fortelle hva slags type den er.


FIXME dokumenter hvordan dette skal gjøres og hvordan resultatet fra
konsistenssjekken skal se ut.  Det trengs en beskrivelse i kapittel 6
av mekanismen med eksempler.  Trengs det også en klassebeskrivelse i
kapittel 7?

Ide: ny entitet KonsistensVarsel med følgende felt:

 * entitet som ble forsøkt opprettet, og eventuelt instans hvis den ble opprettet
 * felt med feilet sjekk
 * type feil
 * alvorlighet på feilen
 * beskrivelse/melding som beskriver sjekk som feilet

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

Alterantiv som kan brukes til både feil og utfordringer...

{
  "feilkode": 401,
  "_links": [
      ...
      { "rel": "mangelrel" },
      ...
  ],
  "_embedded": {
      "mangelrel" : { "count": 1,
        "results": [
          {
            "felt": "dokumentdato",
            "varslingstype": "Usannsynlig verdi",
            "melding" : "Datoen er i fremtiden"
          }
        ]
      }
  }
}  


Kodeliste.KonsistensVarselNivaa:
  * Kritisk = 4
  * Alvorlig = 3
  * Advarsel = 2
  * Tips = 1

FIXME Ny kodeliste for varslingstyper og alvorlighet?

FIXME Hvilket språk skal meldingene ha?  Hvordan skal en håndtere flere språk?


{
  "_links": [
      ...
      { "rel": "self",
        "href": "somewhere/asfdasfsf/"
      }
      { "rel": "../arkivstruktur/arkiv/",
        "href": "somewhere/asfdasfsf/"
      }
      { "rel": "mangelrel/datakvalitet/",
        "href": "somewhere/asfdasfsf/datakvalitet"
      },
      ...
  ],
  "_embedded": {
      "mangelrel" : { "count": 1,
        "results": [
          {
            "felt": "dokumentdato",
            "varslingstype": "Usannsynlig verdi",
            "melding" : "Datoen er i fremtiden"
          }
        ]
      }
  }
}  
