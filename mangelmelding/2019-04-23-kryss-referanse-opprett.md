Beskriv hvordan Kryssreferanser opprettes
=========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  versjon git 2019-04-23
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  Finn ut
         Sidenummer  Finn ut
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart fra spesifikasjonen hvordan Kryssreferanse-instanser skal opprettes og forvaltes. Det er angitt en REL for 

    http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-kryssreferanse/

for basisregistrering (side 83), mappe (133) og klasse (side 117). Det er ikke beskrevet hvordan koblingen til den andre entitieten skal spesifiseres. Det er viktig at dette er spesifisert entydig, ellers er det sannsynlig at det håndteres ulikt av tjener implementasjoner. Et forslag er å bruke $ref (side 20) der det står "*... kan klienter benytte  ... $ref parameter for å slette, endre eller opprette referanser mellom objekter*". Det er ingen krav at en klient *må* bruke denne metoden. En klient kan feks bruke følgende tilnærming for å opprette en kryssreferanse:


```python
    http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/1fa94a89-3550-470b-a220-92dd4d709044
```

Følgende eksempel viser hvordan en kryssreferanse fra en mappe til en basisregistreging opprettes ved å bruke en OData $ref parameter:

```python
    http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/$ref?$id=api/arkivstruktur/basisregistrering/1fa94a89-3550-470b-a220-92dd4d709044
```

Det er viktig at klienter får en entydig måte å håndtere dette. Det er også verdt å merke at det er mer beskrivende dersom vi ser entitetstypen til entiteten det skal refereres til er. Dette oppnås ved å bruke $ref. 

$ref bør være spesisifert som måte å referere på og at det selvsagt ikke er mulig å referere til noe utenfor kjernen. Merk at i henhold til [OData](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752345) så trenger ikke en klient oppgi hele URLen til det interne objektet som skal refereres til. Vi forslår at tjenestegrensesnitt velger en slik tilnærming for å unngå at det kan tolkes at det er mulig å lage referanser på tvers av arkivkjerner.

Videre oppfattes det slik at en kryssreferanse er kun definert som en attributt men det bør være mulig å samhandle med de som relasjoner. Det er litt forvirrende når en attributt oppfører seg både som relasjon og attributt. 

Følgende JSON viser er hvordan vi ser en implementasjon av mappe med en kryssreferanse

```python
{
  ....
  _links : 
 {
   {
     "href" : "http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/kryssreferanse", 
     "rel"  : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/kryssreferanse/"
   }    
 }
}
```

"rel"  : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/kryssreferanse/" vil returne en liste av kryssreferanse. Dette kan se slik ut:


```python

{
 [
  {
   "referanseTilRegistrering" : "1fa94a89-3550-470b-a220-92dd4d709044",
    _links : 
    {
      {
       "href" : "http://localhost:49708/api/arkivstruktur/basisregistrering/1fa94a89-3550-470b-a220-92dd4d709044", 
       "rel"  : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/"
      }    
    }
  }
 ]
}
```

Det er uklart hvordan en kan hente ut, oppdatere og slette kryssreferanse instansen over. Det enkleste for å løse dette hadde vært å la Kryssreferanse arve fra Arkivenhet og at alle kryssreferanser hadde sin egen systemID. Dette hadde også gjørt det mulig å søke opp kryssreferanser i systemet. Dette kan viktig kontekst metadata.


Ønsket endring
--------------
Jeg vet ikke hvor endringen skal inn.


Jeg sender inn konkret forslag til endring som patch via github.
