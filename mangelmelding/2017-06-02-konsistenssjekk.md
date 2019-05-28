Definer mekanisme for resultat fra automatisk kvalitetskontroll
===============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
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

 * Postnummeret brukt i en korrespondanseenhet er ikke i listen over
   kjente postnummer.

 * Det opplastede dokumentet har et format som ikke aksepteres av
   arkivverket for langtidsoppbevaring.

 * Det opplastede dokumentet er et interakivt regneark, eller et
   regneark som gjør oppslag i ekstern database som del av
   beregninger, som dermed ikke kan automatisk konverteres til PDF på
   meningsfylt vis.
   
 * Det opplastede dokumentet har ikke et klart språk, jamfør
   <URL:https://www.digi.no/artikler/kommentar-den-digitale-borger-og-klarsprak/466014>

 * Hvilken målform dokumentet i hovedsak består av, og hvorvidt dette
   er målformen det trengs mer eller mindre av.

Slike feil er ofte resultat av manuelle skrivefeil, og bør oppdages så
raskt som mulig for å holde kvaliteten i arkivsystemet oppe.

Slik konsistenssjekk kan gjøres når ny entitet opprettes med POST til
ny-* eller når en entitet oppdateres med PUT.  Det er dermed fint om
resultatet fra slike konsistenssjekker kan være del av svaret som
kommer fra POST og PUT.

En lite inngripende måte å gjøre dette på er å legge ved en ekstra
relasjon i \_links hvis konsistenssjekken har oppdaget noe rart, og så
peke href-verdien til et sted der detaljer om hva som ble oppdaget
returneres.  Det gjør at klienter som ikke forstår
konsistenssjekk-tilbakemeldingen kan ignorere den, mens klienter som
forstår relasjonen kan vise frem detaljene til brukeren, i tilfelle
det for eksempel er skrivefeil som brukeren kan korrigere.

Det som trengs for å få dette til er en definisjon av hva
konsistenssjekk-resultatene skal returnere, og å definere en
relasjonsnøkkel som API-klienter kan se etter etter å ha opprettet
eller endret en instans.

En kan se på konsistenssjekk-resultater som en generalisert mekanisme
for feilmeldinger (se
[mangelmelding #93](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/93)).
Alvorlige resultater fører til at opprettelsen av objektet blir
avvist, mens mindre alvorlige resultater kun gir varsling om
problemer.

Hvis API-et bruker en ektra relasjon i \_links, så vil det være lite
hensiktsmessig å returnere samme struktur for feil og
problemer, da listen over feil som gjorde at opprettelsen ble avvist
må mellomlagres i ubestemt tidsrom, hvilket gjør det mer komplisert
å lage API-tjenesten som må ta vare på informasjon om forkastede
instanser utenom normal datastruktur.  På den andre siden kan det være
nyttig å ta vare på slike feilmeldinger for analyse og identifikasjon
av potensielle forbedringer på klientsiden.  Et alternativ til å ta
vare på slike feilmeldinger i ubestemt tidsrom kan være å bruke
"_embedded"-mekanismen beskrevet i utkastet til [JSON Hypertext
Application
Language](https://tools.ietf.org/html/draft-kelly-json-hal-08), der
alle detaljer følger med i responsen fra API-et.




```Python
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
```

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
øvrige bør aksepteres men API-klient bør om mulig be bruker bekrefte
verdiene på nytt.

Resultatet fra slike kvalitetssjekker bør samles slik at
arkivansvarlig kan holde et øye med mengden slike feil.

For å kunne identifisere hvilke klient-type som produserer hvilke
typer feil, så bør API-et utvides til å kreve at klienten
identifiserer seg selv, for eksempel ved å bruke HTTP-hodetfelet
"User-Agent".  En vil dermed kunne hente ut statistikk over hva slags
feil ulike klienter produserer, som kan brukes til å identifisere
systematiske feil forårsaket av en defekt i klientprogrammet.

Sjekk også
https://en.wikipedia.org/wiki/Object_Constraint_Language

# Ønsket endring
--------------

Denne endringsforslaget medfører følgende:

1. Identifiser og beskriv konsistenssjekk-relasjon  
2. Beskriv konsistenssjekk entitet/nyttelast
3. Det introduseres en ny REL under administrasjon
4. Krav om identifisering av klienter



## Identifiser og beskriv konsistenssjekk-relasjon  



## Beskriv konsistenssjekk entitet/nyttelast


En konsistensvarsel har følgende felt:

 * entitet: som ble forsøkt opprettet, og eventuelt instans hvis den ble opprettet
 * felt: med feilet sjekk
 * varslingstype: type feil
 * melding: beskrivelse/melding som beskriver sjekk som feilet
 * alvorlighet: alvorlighet på feilen


Følgende JSON viser resultatet av en GET mot en href for konsistenssjekk-relasjon etter opprettelse av en journalpost der dokumentetsDato (M103) er satt til en dato i fremtiden.

```
{
  "results": [
    {
      "entitet": "journalpost",
      "systemID": "21a8652d-54cc-40da-80f2-c487708f2879",
      "felt": "dokumentdato",
      "varslingstype": "Usannsynlig verdi",
      "melding" : "Datoen er i fremtiden",
      "alvorlighet" : "Advarsel",
      "_links": [
        ... self osv ...
	   { 
	    "rel": "http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/",
        "href": "https://nikita.oslomet.no/noark5v4/api/sakarkiv/journalpost/21a8652d-54cc-40da-80f2-c487708f2879"
       }
    }
  ]
}
```

Det foreslåes da å introdusere en kodeliste for alvorlighet:

Kodeliste.KonsistensVarselNivaa:
  * Kritisk = 4
  * Alvorlig = 3
  * Advarsel = 2
  * Tips = 1

pere: Kommentar. Skal vi lage en tabell tilnærming med kode og beskrivelse her??

I nåværende forslag forslag skal meldingene være på bokmål. Senere kan det spesifiseres hvordan andr målform/språk skal håndteres.

pere: Kommentar. Dette gjelder vel generelt alt i TG. Kodestatusverdier osv skal kunne hente us på bokmål og nynorsk.

## Ny REL under administrasjon-pakke

Arkivkjernen lagrer disse konsistens vurderingene. Dersom klienter er identifisert via "User-agent", kan vurderingene søkes ut per klient med OData.

> http://rel.kxml.no/noark5/v4/api/admin/konsistenssjekk

Et oppslag mot HREFen til ovennevnte REL vil da returnere en sideinndelt liste av alle
konsistensjekk. Det er selvfølgelig kun en autorisert bruker som har tilgang til å hente ut informasjon om alle kvalitetsvurderinger. Disse kan videre filtreres med OData spørringer.

## Krav om identifisering av klienter


Det bør legges til en egen underkappitel i kapittel "Kapittel 6 KONSEPTER OG PRINSIPPER" der de forskjellige verdiene i HTTP-headers som forventes å være brukt. 


> "User-Agent": Identifikasjon av klient. Klienten kan identifiseres med system navn og versjon nummer.



Kommentar til pere. Tid på lagring trenger vi ikke å ta medr. De lagres
FIXME bør tillate API å ta vare på feilmeldinger en periode, med kjent utløpsdato, for analyse.  bør inkludere klientinformasjon.
.
