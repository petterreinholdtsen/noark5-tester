Definer foreldre-relasjon i hierarkiske strukturer
==================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
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

I stedet for eller i tillegg til relasjoner mellom entiteter som
navngis med relasjonsnøkler basert på entitetstype, så bør det
vurderes å legge inn en generisk forelder-relasjon.

http://rel.kxml.no/noark5/v4/api/arkivstruktur/forelder

Forholdet mellom dokumentobjekt og dokumentbeskrivelse kan da se slik
ut:

{
  ...,
  "_links": [
     { "rel": "self",
       "href": "http://localhost:49708/api/arkivstruktur/dokumentobjekt/532a9660-59c9-11e9-a93e-13b3ec698393/" },
     ...
     { "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/forelder",
       "href": "http://localhost:49708/api/arkivstruktur/dokumentbeskrivelse/532a9660-59c9-11e9-a93e-13b3ec698393/" },
     { "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse",
       "href": "http://localhost:49708/api/arkivstruktur/dokumentbeskrivelse/532a9660-59c9-11e9-a93e-13b3ec698393/" },
  ]
}

En bi-effekt av denne tilnærmingen er at det blir klart fra
relasjons-strukturen at det kun kan være en forelder-relasjon av flere
mulige, slik det for eksempel gjelder for Registrering.

Ønsket endring
--------------

FIXME
