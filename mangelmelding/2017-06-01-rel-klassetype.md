Mekanisme for å identifisere entiteters klasse i entitetslister
===============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Som bruker av API-et savner jeg en mekanisme som kan brukes for å
identifisere klassen til en entitet i en liste med entiteter, der det
finnes flere underklasser.  Eksempler på dette er saksmapper som er en
underklasse av mapper, journalposter som er underklasse av
basisregistreringer som igjen er underklasse av registreringer, og
korrespondansepartperson som er underklasse av korrespondansepart.

Utgangspunktet er at relasjonenes rel-innhold er standardisert i
spesifikasjonen, mens href-innholdet er implementasjonsavhengig.
Dermed kan en ikke se på innholdet i href-feltet for å gjette på
klassetype.

En utsnitt av en liste med mapper kan for eksempel se slik ut:

```
{ "results": [
  { ...
    "_links": [
    ...
   {
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/ny-registrering/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-registrering/",
      "templated" : false
    }, {
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/registrering/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/",
      "templated" : false
    }, {
      "href" : "http://something/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/",
      "rel" : "self",
      "templated" : false
    } ]
   },
   ]
}
```

En metode for å finne klassen til en entitet kunne være å oppgi samme
href to ganger med to ulike rel-verdier, en for 'self' som over, og en
med klassenavnet som relasjon.  Det ville dermed se slik ut:

```
{ "results": [
  { ...
    "_links": [
    ...
   {
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/ny-registrering/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-registrering/",
      "templated" : false
    }, {
      "href" : "http://something/arkivstruktur/mappe/2624ed49-dc39-47d5-8966-52f9fdc75868/registrering/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/",
      "templated" : false
    }, {
      "href" : "http://something/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/",
      "rel" : "http://rel.kxml.no/noark5/v4/api/sakarkiv/saksmappe/",
      "templated" : false
    }, {
      "href" : "http://something/sakarkiv/saksmappe/2624ed49-dc39-47d5-8966-52f9fdc75868/",
      "rel" : "self",
      "templated" : false
    } ]
   },
   ]
}
```

Hvis alle implementasjoner har slike relasjoner for hver entitet så
vil det være trivielt for API-klienter å finne ut hvilken klasse en
gitt entitet har i en liste med foreldre-entiteter i et arvetre.

Ønsket endring
--------------

FIXME formuler og finn ut hvor spesifikasjonen bør endres.
