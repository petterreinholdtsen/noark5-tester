Beskriv metode for å identifisere entiteter i instanslister
===========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.1 (Finne objekter (Read))
         Sidenummer  13
        Linjenummer  n/a
    Innsendingsdato  2019-04-09
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Som bruker av API-et savner jeg en beskrivelse av hvordan en kan
identifisere entiteten til en instans i en liste med instanser, der
det finnes flere underentiteter.  Eksempler på dette er Saksmappe som
arver fra Mappe og Journalpost som arver fra Basisregistrering som igjen
arver fra Registrering.

Utgangspunktet er at relasjonenes relasjonsnøkkel er standardisert i
spesifikasjonen, mens href-innholdet er implementasjonsavhengig.
Dermed kan en ikke se på innholdet i href-feltet for å gjette på
entitetstype.

Det som ser ut til å være en god metode for å finne entitetstypen til
en instans er å se etter 'self'-relasjonen, deretter se etter en
relasjon med samme href-verdi.  Denne andre relasjonens
relasjonsnøkkel identifiserer entitetens type.  Det vil typisk se slik
ut:

```Python
{ "results": [
  { ...
    "_links": [
    ...
   {
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-registrering/",
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/ny-registrering/"
    }, {
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/",
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/registrering/"
    }, {
      "rel" : "http://rel.kxml.no/noark5/v4/api/sakarkiv/saksmappe/",
      "href" : "http://something/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/"
    }, {
      "rel" : "self",
      "href" : "http://something/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/"
    } ]
   },
   ]
}
```

Her kan en se at 'self har samme href som
`http://rel.kxml.no/noark5/v4/api/sakarkiv/saksmappe/`, hvilket betyr
at instansen er en saksmappe.

For å sikre at alle implementasjoner har slike relasjoner for hver
instans, så må det beskrives eksplisitt i spesifikasjonen.  Da vil det
være trivielt for API-klienter å finne ut hvilken entitet en gitt
instans har i en liste med foreldre-instanser i et arvetre.

Jeg tenker her på når en f.eks. søker i alle Registrering-instanser,
så kan denne prosedyren brukes for å finne ut hvilke
Registrering-instanser som egentlig er Journalposter.

Ønsket endring
--------------

Foreslår at det legges inn en ny underoverskrift mellom 6.1.1.1
(Oppkobling og ressurslenker) og 6.1.1.2 (Finne objekter (Read)) på
side 13 som lyder slik:

> #### Identifisere entitetstype
>
> En kan identifisere hvilken entitet en oppføring har ved å først
> identifisere "self"-relasjonsnøkkelen i "_links"-listen, deretter
> identifisere hvilken annen oppføring som har samme href som
> "self"-relasjonsnøkkelen.  Relasjonsnøkkelen til oppføringen som har
> samme href som "self" representerer entitetsrelasjonsnøkkelen til
> "self".    Dette kan se slik ut:
>
> ```Python
> { "results": [
>   { ...
>     "_links": [
>       {
>         "rel": "self",
>         "href": "http://localhost:49708/api/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/"
>       }, {
>         "rel": "http://rel.kxml.no/noark5/v4/api/sakarkiv/saksmappe/",
>         "href": "http://localhost:49708/api/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/"
>       },
>       ...
>     ]
>   } ]
> }
> ```

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/119 .
