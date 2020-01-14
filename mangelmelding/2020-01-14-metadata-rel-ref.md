Dokumentere i _links hvilke metadata-lenker som gjelder for hvilken attributt?
==============================================================================n

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?n
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I dag må API-klienter vite hvilke relasjonsnøkler i _links som hører
til hvilke attributter.

Det ville være enklere om _links hadde nok informasjon til at klienten
slapp å ha kunnskap om dette fra yttersiden.

I dag:

```
{
   "dokumentmedium": "Elektronisk arkiv",
   ...
   "_links": {
       "https://rel.arkivverket.no/noark5/v5/api/metadata/dokumentmedium/": {
           "href": ""https://n5.example.com/api/metadata/dokumentmedium"
       }
   }
}
```

I fremtiden

```
{
   "dokumentmedium": "Elektronisk arkiv",
   ...
   "_links": {
       "https://rel.arkivverket.no/noark5/v5/api/metadata/dokumentmedium/": {
           "href": ""https://n5.example.com/api/metadata/dokumentmedium",
	   "kodelistefor": "dokumentmedium"
       }
   }
}
```

Dette gjør det mulig for API-klienter å vite hvor den kan slå opp
gyldige verdier for "dokumentmedium", og enklere for klienter å
håndtere nye attributter som kommer til i fremtiden.

Ønsket endring
--------------
