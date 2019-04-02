Hvordan håndteres undermappe i mappe?
=====================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.16
         Sidenummer  134
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder del 7.2.1.16 (Mappe) side 134, men tilsvarende problem
eksisterer for 7.2.1.1 (Arkiv ) side 57 og 7.2.1.12 (Klasse) side 116.

Listen over relasjonsnøkler for entiteten Mappe på sidene 133-134 viser
at en kan få ut oversikt over undermapper ved å benytte relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/, men har
ingen tilsvarende relasjon ny-undermappe/ for å *opprette* en ny
undermappe.  Det er ikke beskrevet hvordan det er mening at en skal
opprette en ny undermappe knyttet til en mappe.

I listen over relasjonsnøkler finnes relasjonene
http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/ og
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/, men det er
uklart fra beskrivelsen hva som er forskjellen på relasjonene 'mappe'
og 'undermappe'.  Det virker rimelig å anta at
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ henviser til
entitetstype og skal brukes for å identifisere 'self'-relasjonens
entitet, mens
http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/ er
operasjonen for å hente ut undermapper.  I følge UML-skjema er enhver
mappe som er koblet under en annen mappe en undermappe.  Det bør
beskrives i spesifikasjonen hva som er forskjellen på mappe- og
undermappe-relasjonene for entiteten Mappe, og hvordan en oppretter en
ny undermappe.

Det er ikke klart fra spesifikasjonen hvordan en finner
«foreldremappen» til en mappe i en mappe.  Er det attributten
referanseForelderMappe med verditype SystemID som er tiltenkt denne
rollen?  For andre entiteter er foreldre-entitet tilgjengelig med
navngitte relasjoner som oppgir href til foreldre-entiteten.  For
eksempel for entiteten Arkivdel er det en navngitt relasjon 'arkiv'
med tilhørende relasjonsnøkkel
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/ som jeg
forventer peker til foreldrearkivet.

Det er ikke mulig å bruke en tilsvarende relasjon for å referere til
en foreldrentitet av samme type som seg selv, da det ville føre til
følgende innhold i _links:

```
"_links": [
  {
    "rel": "self",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/5a441fae-557b-11e9-9b92-002354090596/"
  },
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/5a441fae-557b-11e9-9b92-002354090596/"
  },
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/69d5a4f6-557b-11e9-bbbd-ff44b1a15f30/"
  },
  ...
}
```

Merk hvordan rel for mappe er listet opp to ganger med to ulike
UUID-er i href-er.  HATEOAS-prinsippene legger opp til at en gitt i
_links kun skal forekomme en gang.  En kan ikke ha to identiske
relasjoner som peker til to ulike href-verdier.

En mulig løsning er å lage en relasjon «foreldermappe» eller
«forelder», ala dette:

```
"_links": [
  {
    "rel": "self",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/5a441fae-557b-11e9-9b92-002354090596/"
  },
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/5a441fae-557b-11e9-9b92-002354090596/"
  },
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/foreldermappe/",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/69d5a4f6-557b-11e9-bbbd-ff44b1a15f30/"
  },
  ...
}
```

En kan tilsvarende ha en relasjon til undermapper ved å søke etter
mapper med gjeldende mappe som foreldermappe.

```
"_links": [
  ...
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/",
    "href": "http://localhost:49708/api/arkivstruktur/mappe/?$filter=foreldermappe eq <denne mappens systemID>"
  },
  ...
}
```

Oversikten over undermapper kan så se ut ala dette, gitt at forslag om
formattering av lister fra
[mangelmelding #12](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/12)
blir tatt i bruk:

```
{ "results" : [
    { "mappeID": "1234/2017",
      "tittel": "testmappe 1",
      ...
    "_links" : [
      { "rel": "self",
        "href": "http://localhost/noark5v4/api/arkivstruktur/mappe/f97b1a9a-557c-11e9-bad4-63d81e3ee1f6/"
      },
      ...
    },
    { "mappeID": "1235/2017",
      "tittel": "testmappe 2",
      ...
    "_links" : [
      { "rel": "self",
        "href": "http://localhost/noark5v4/api/arkivstruktur/mappe/1e29f8de-557d-11e9-b479-83abafe61152/"
      },
      ...
    }
  ],
  "count" : 2,
  "_links" : [
    { "rel": "self",
      "href": "http://localhost:49708/api/arkivstruktur/mappe/?$filter=foreldermappe eq 5a441fae-557b-11e9-9b92-002354090596"
    }
  ]
}
```

En alternativ og kanskje mer generisk navnestruktur for slik
relasjonsnøkler kan være å skille dem med skråstreker, dvs. bruke
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/forelder/` og
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/under/`.


For å opprette en undermappe skal POST til href som er knyttet til
følgende relasjon brukes:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/

Merk, det er en tilsvarende utfordring for arkiv/underarkiv i del
7.2.1.1 side 57 og klasse/underklasse i del 7.2.1.12 side 116.
Løsningen som velges for mappe/undermappe bør også gjelde for
arkiv/underarkiv og klasse/underklasse og dokumenteres tilsvarende
der.  Det er også tilsvarende utfordring for entiteter som kan peke
til seg selv av andre grunner en å danne et hierarki, slik Arkivdel,
Moetemappe og Moeteregistrering kan.  

Merk videre at relasjon for underarkiv/underklasse/undermappe er ført
opp med duplikater i spesifikasjonen, å rydde opp i dette er sendt inn
som [endringsforslag #84](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/pull/84).

Ønsket endring
--------------

Foreslår at det legges inn et nytt avsnitt i kapittel 6 om hvordan
rekursive relasjoner skal håndteres før overskriften «Slette objekter
(Delete)»:

> #### Rekursive entitetshierarkier
> 
> Noen entiteter kan ha samme type entitet under seg, og slik danne et
> rekursivt hierarki av instanser.  Det gjelder Arkiv, Klasse og Mappe,
> og entiter som arver fra disse (som Saksmappe og Moetemappe).
>

> Da det ikke er i tråd med HATEOAS-prinsippene å la samme relasjon
> peke til flere ulike href-er, så må dette håndteres litt annerledes
> enn relasjoner mellom entiteter av ulik type.  Listen over
> under-instanser til en gitt instans kan hentes ut ved å følge href
> for relasjonen
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/underxx/, der xx er
> navnet på entitet.  Eksempler på slike relasjoner
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/underarkiv/ og
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/.
> 
> Av samme grunn er det ikke mulig å la foreldrerelasjonen gjenbruke
> entitetens relasjon.  En kan der finne foreldreinstans ved å følge
> href for relasjonen
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/forelderxx/.  Eksempler
> på slike relasjoner
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/forelderarkiv/ og
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/foreldermappe/.
> 
> JSON-listen over relasjoner for en mappe midt i et slikt hierarki kan
> for eksempel se slik ut:
> 
> ```Python
> "_links": [
>   {
>     "rel": "self",
>     "href": "http://localhost:49708/api/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/"
>   },
>   {
>     "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/",
>     "href": "http://localhost:49708/api/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/"
>   },
>   {
>     "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/foreldermappe/",
>     "href": "http://localhost:49708/api/arkivstruktur/mappe/6787ba68-53d7-11e9-a583-8f084aaf5d19/"
>   },
>   {
>     "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/undermappe/",
>     "href": "http://localhost:49708/api/arkivstruktur/mappe/?$filter=foreldermappe eq 7b3989b0-53d7-11e9-bd4e-17d6c4d53856"
>   },
>   ...
> }
> ```
> 
> Merk at konkrete href-verdier ikke er standardisert, det er valgfritt
> hvordan en implementerer oppslag i foreldre- og undermapper.

I tillegg til dette tillegget til kapittel 6, så skal attributt
«referanseForelderMappe» fjernes fra Mappe, og relasjonen for
«undermappe» endres til toveis og ha «foreldermappe 0..1» på
motstående side, da det i stedet for attributt brukes relasjon med
tilhørende relasjonsnøkkel.  Tilsvarende for arkiv og klasse.
