Strukturer _links i tråd med siste utkast for HAL-lenker
========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.1 (Oppkobling og ressurslenker0
         Sidenummer  11
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I kapittel 2 er det sagt at normativ referanse for webtjenester med
REST/HATEOAS er [JSON Hypertext Application
Language](https://tools.ietf.org/html/draft-kelly-json-hal-08).  Men
relasjonslenkene er i dag ikke strukturert i tråd med den
spesifikasjonen, som beskriver følgnde struktur:

```
{
     "_links": {
       "self": { "href": "/orders/523" },
       "warehouse": { "href": "/warehouse/56" },
       "invoice": { "href": "/invoices/873" }
     },
     ...
}
```

Ved å bruke en slik struktur håndheves kravet om at alle rel-navn skal
være unike av seg selv.

Ønsket endring
--------------

Endre beskrivelsen av relasjonslenker i del 6.1.1.1 på side 11, samt
alle andre _links-oppføringer fra dette formatet:

```
"_links": [
  {
    "rel": "self",
    "href": "<base>/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/"
  },
  {
    "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/",
    "href": "<base>/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/"
  },
  ...
]
```

til dette:

```
"_links": {
  "self" : { "href": "<base>/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/" }
  "http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/" : {
    "href": "<base>/arkivstruktur/mappe/7b3989b0-53d7-11e9-bd4e-17d6c4d53856/"
  },
  ...
]
```
