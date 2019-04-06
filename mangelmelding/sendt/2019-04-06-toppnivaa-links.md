Beskriv hva som returneres når en henter ut informasjon fra toppnivå-relasjonsnøkler
====================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1 (Arkivstruktur)
         Sidenummer  37
        Linjenummer  n/a
    Innsendingsdato  2019-04-06
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er ikke forklart i spesifikasjonen hva som skal returneres når en
tar GET mot href som pekes til av relasjonsnøkkelen
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/`,
`http://rel.kxml.no/noark5/v4/api/sakarkiv/`,
`http://rel.kxml.no/noark5/v4/api/admin/` og
`http://rel.kxml.no/noark5/v4/api/loggingogsporing/`.

Her er det lille som står om temaet i spesifikasjonen.  I del 6.1.1.1
(Oppkobling og ressurslenker) på side side 12 står det:

> "Eksempelet viser at denne arkivkjernen støtter arkivstruktur
> (http://rel.kxml.no/noark5/v4/api/arkivstruktur) og sakarkiv
> (http://rel.kxml.no/noark5/v4/api/sakarkiv). Ved å følge Href til
> disse relasjonsnøkler vil tilgjengelige ressurser innen disse
> områder annonseres på samme måte."

I tillegg står det på side 13:

> | Relasjonsnøkkel (rel)                           | Beskrivelse                                          |
> |-------------------------------------------------|------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ | Arkivkjerne støtter konformitetsnivå 1 arkivstruktur |
> | http://rel.kxml.no/noark5/v4/api/sakarkiv/      | Arkivkjerne støtter konformitetsnivå for sakarkiv (2a) |
>
> Relasjonsnøkler under de forskjellige konformitetsnivå listes ut i
> kapittel 7 sammen med beskrivelse av klasser.

Det står ingenting om hvilke relasjoner som skal listes opp for
../arkivstruktur/, ../sakarkiv/ og ../admin/.  Det burde være
beskrevet i spesifikasjonen.

Det finnes to eksempler på hvordan det kan se ut for
../arkivstruktur/, det ene er fra
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/`, som ser slik ut:

```Python
{
  "_links": [
    {
      "href": "http://localhost:49708/api/arkivstruktur/arkiv{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/nytt-arkiv",
      "rel": "http://rel.kxml.no/noark5/v4/api/administrasjon/ny-arkiv",
      "templatedSpecified": false
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/arkivskaper{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivskaper",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/arkivdel{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/klassifikasjonssystem{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/klasse{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/mappe{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/registrering{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/basisregistrering{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/basisregistrering",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/dokumentbeskrivelse{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse",
      "templated": true,
      "templatedSpecified": true
    },
    {
      "href": "http://localhost:49708/api/arkivstruktur/dokumentobjekt{?$filter&$orderby&$top&$skip&$search}",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt",
      "templated": true,
      "templatedSpecified": true
    }
  ]
}
```

Det andre eksemplet er fra `http://n5test.kxml.no/api/arkivstruktur`
og ser slik ut: :

```Python
{
  "_links": [
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv",
      "href": "http://n5test.kxml.no/api/arkivstruktur/arkiv{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/administrasjon/ny-arkivskaper",
      "href": "http://n5test.kxml.no/api/arkivstruktur/ny-arkivskaper",
      "templated": false
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivskaper",
      "href": "http://n5test.kxml.no/api/arkivstruktur/arkivskaper{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel",
      "href": "http://n5test.kxml.no/api/arkivstruktur/arkivdel{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem",
      "href": "http://n5test.kxml.no/api/arkivstruktur/klassifikasjonssystem{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse",
      "href": "http://n5test.kxml.no/api/arkivstruktur/klasse{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe",
      "href": "http://n5test.kxml.no/api/arkivstruktur/mappe{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering",
      "href": "http://n5test.kxml.no/api/arkivstruktur/registrering{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/basisregistrering",
      "href": "http://n5test.kxml.no/api/arkivstruktur/basisregistrering{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse",
      "href": "http://n5test.kxml.no/api/arkivstruktur/dokumentbeskrivelse{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    },
    {
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt",
      "href": "http://n5test.kxml.no/api/arkivstruktur/dokumentobjekt{?$filter&$orderby&$top&$skip&$search}",
      "templated": true
    }
  ]
}
```


Ønsket endring
--------------

I starten av dokumentdel 7.2.1 (Arkivstruktur) på side 37 legges det
inn følgende tekst:

> Når en gjør GET mot href til relasjonsnøkkel
> http://rel.kxml.no/noark5/v4/api/arkivstruktur/, så returneres liste
> over relasjonsnøkler til de ulike entitetene som er tilgjengelig.
> Disse kan brukes til å søke etter instanser av hver enkelt entitet.
> I tillegg er det relasjonsnøkler for å opprette entiteter på
> toppnivå i arkivstrukturen, hvis brukeren har tilgang til å opprette
> nye instanser (her ny-arkiv og ny-arkivskaper).  Resultatet kan for
> eksempel starte slik:
>
> ```Python
> {
>   "_links": [
>     {
>       "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/",
>       "href": "http://localhost:49708/api/arkivstruktur/arkiv{?$filter&$orderby&$top&$skip&$search}",
>       "templated": true
>     },
>     {
>       "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkiv/",
>       "href": "http://localhost:49708/api/arkivstruktur/ny-arkiv",
>     },
>     ...
>   ]
> }
> ```
>
> Følgende relasjonsnøkler skal listes opp fra en implementasjon som
> støtter Arkivstruktur-pakken:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/                 |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/              |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivskaper/           |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/basisregistrering/     |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse/   |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/        |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse/                |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem/ |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/                 |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/          |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/hendelseslogg/         |
>
> Følgende relasjonsnøkler skal tilsvarende listes opp for privilgerte brukere
> etter innlogging:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkiv/              |
> | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivskaper/        |

Det legges inn tilsvarende tekstblokk først i 7.2.3 (Sakarkiv) på side 195:

> Når en gjør GET mot href til relasjonsnøkkel
> http://rel.kxml.no/noark5/v4/api/sakarkiv/, så returneres liste over
> relasjonsnøkler til de ulike entitetene som er tilgjengelig.
> Følgende relasjonsnøkler skal listes opp fra en implementasjon som
> støtter Sakarkiv-pakken:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/                |
> | http://rel.kxml.no/noark5/v4/api/sakarkiv/presedens/                  |
> | http://rel.kxml.no/noark5/v4/api/sakarkiv/saksmappe/                  |

Dernest, tilsvarende tekstblokk først i 7.2.4 (Admin) på side 252:

> Når en gjør GET mot href til relasjonsnøkkel
> http://rel.kxml.no/noark5/v4/api/admin/, så returneres liste over
> relasjonsnøkler til de ulike entitetene som er tilgjengelig.
> Følgende relasjonsnøkler skal listes opp fra en implementasjon som
> støtter Admin-pakken:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/admin/administrativenhet/            |
> | http://rel.kxml.no/noark5/v4/api/admin/bruker/                        |
> | http://rel.kxml.no/noark5/v4/api/admin/rettighet/                     |
>
> Følgende relasjonsnøkler skal tilsvarende listes opp for privilgerte brukere
> etter innlogging:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/admin/ny-administrativenhet/         |
> | http://rel.kxml.no/noark5/v4/api/admin/ny-bruker/                     |
> | http://rel.kxml.no/noark5/v4/api/admin/ny-rettighet/                  |

Til slutt, tilsvarende tekstblokk først i 7.2.5 (LoggingOgSporing) på side 264:

> Når en gjør GET mot href til relasjonsnøkkel
> http://rel.kxml.no/noark5/v4/api/loggingogsporing/, så returneres
> liste over relasjonsnøkler til de ulike entitetene som er
> tilgjengelig.  Følgende relasjonsnøkler skal listes opp fra en
> implementasjon som støtter LoggingOgSporing-pakken:
>
> | **Relasjonsnøkkel**                                                   |
> |-----------------------------------------------------------------------|
> | http://rel.kxml.no/noark5/v4/api/loggingogsporing/endringslogg/       |

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/107 .
