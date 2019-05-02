Beskriv hvordan Kryssreferanser opprettes, endres og slettes
============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  versjon git 2019-04-23
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.15 Kryssreferanse
         Sidenummer  130
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart fra spesifikasjonen hvordan Kryssreferanse-instanser
skal opprettes og forvaltes. Det er angitt en relasjonsnøkkel
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-kryssreferanse/`
knyttet til basisregistrering (side 83), mappe (133) og klasse (side
117). Det er ikke beskrevet hvordan koblingen til den andre entiteten
skal spesifiseres. Det er viktig at dette er spesifisert entydig,
ellers er det sannsynlig at det vil håndteres ulikt av ulike
API-implementasjoner.  Et forslag er å bruke $ref (side 20) der det
står "*... kan klienter benytte ... $ref parameter for å slette, endre
eller opprette referanser mellom objekter*".  Det er intet krav at en
klient *må* bruke denne metoden.  En fremgangsmåte for å opprette en
kryssreferanse kan for eksempel se slik ut:


```
POST http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/1fa94a89-3550-470b-a220-92dd4d709044
```

En annen fremgangsmåte, ved å bruke OData-parameteret $ref for å
opprette en kryssreferanse fra en mappe til en basisregistrering, kan
for eksempel se slik ut:

```
POST http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/$ref?$id=api/arkivstruktur/basisregistrering/1fa94a89-3550-470b-a220-92dd4d709044
```

Det finnes helt sikkert også andre måter å gjøre dette på.

Når det står ikke eksplisitt i spesifikasjonen hvordan slike skal
opprettes, så overlates det til de som implementerer API-et å lage sin
egen metode, hvilket fører til leverandørinnlåsing.  Det er viktig at
klienter får en entydig måte å håndtere dette.

Det er også verdt å merke at det er mer beskrivende dersom vi ser
hvilken entitetstype instansen har som det opprettes kryssreferanse
til.  Dette oppnås ved å bruke $ref-tilnærmingen.

$ref bør være spesifisert som måte å referere på og at det selvsagt
ikke er mulig å referere til noe utenfor kjernen.  Merk at i henhold
til
[OData](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752345)
så trenger ikke en klient oppgi hele URLen til det interne objektet
som det skal refereres til.  Da det vil åpne for at klienten må redigere
på URL-er den fikk via href i \_links, så anbefaler vi at det kreves
komplette URL-er i $ref.  For å sikre at det kun kan brukes URL-er
som refererer til instanser i API-et, så bør det skrives eksplisitt at
kun href-verdier fra API-et selv kan brukes i parameteret $ref.

Videre oppfattes det slik at en kryssreferanse er kun definert som en
attributt men det bør være mulig å samhandle med de som relasjoner.
Det er litt forvirrende når en attributt oppfører seg både som
relasjon og attributt, og det er enklere for API-klienter om en kun
representerer disse verdiene som relasjoner.

Følgende JSON-fragment viser hvordan en implementasjon av mappe med en
eller flere kryssreferanser burde se ut:

```Python
{
  "systemID": "cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e",
  ...
  "_links" : [
    {
      "href": "http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/",
      "rel": "self"
    }
    ...
    {
      "href": "http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/kryssreferanse",
      "rel": "http://rel.kxml.no/noark5/v4/api/arkivstruktur/kryssreferanse/"
    }
 ]
}
```

GET mot href for relasjonsnøkkelen
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/kryssreferanse/` vil
returnere en liste av kryssreferanse. Dette burde se slik ut:


```Python
{
  "results": [
    {
      "referanseTilRegistrering" : "1fa94a89-3550-470b-a220-92dd4d709044",
      "_links" : [
        {
          "href" : "http://localhost:49708/api/arkivstruktur/basisregistrering/1fa94a89-3550-470b-a220-92dd4d709044", 
          "rel"  : "http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/"
        }    
      ]
    }
  ]
}
```

Her ser en hvordan lenken til basisregistreringen er duplisert som
systemID-verdi i attributtlisten.  Det holder med en av dem, og
relasjon i \_links sikrer at en API-klient er i stand til å finne
informasjon om basisregistreringen direkte uten å måtte slå opp / søke
etter SystemID-verdien først.

Det er uklart hvordan en kan hente ut, oppdatere og slette
kryssreferanse-instansen over.  Det enkleste for å gjøre det mulig er
å la Kryssreferanse arve fra Arkivenhet slik at alle kryssreferanser
hadde sin egen systemID, jamfør mangelmelding #151. Hvis det samtidig
beskrives et endepunkt for kryssreferanser, så blir det mulig å søke
opp kryssreferanser i systemet.  Dette kan være viktig kontekst for
metadata.

Det mangler også en beskrivelse av kjente begrensninger rundt 
Kryssreferanse som er definert i Noark 5v4 standarden (01.12.2016). 
På side 76 står det følgende begrensninger som gjelder for Kryssreferanse:

> *Kryssreferanse kan knyttes en eller flere ganger til klasse, mappe
> og basisregistrering. Referansen går en vei, dvs. den kan kun være
> en referanse til en arkivenhet. I og med at kryssreferanser knyttes
> til Mappe og Basisregistrering, vil det si at Referanser også
> knyttes til alle utvidelsene (spesialiseringer) under disse
> (Saksmappe, Møtemappe og Journalpost, Møteregistrering).*

Dette er en viktig presisering som må inn i tjenestegrensesnittet,
enten med en henvisning til Noark 5v4-standarden eller ved å kopiere
inn teksten.

Ønsket endring
--------------

Følgende endringer ønskes

1. Beskriv entydig at $ref må brukes når en oppretter en ny kryssreferanse.
2. Gjør det klart at hele URL-en må være med som parameter til $ref,
   og at URL-en må være hentet fra href utlevert fra API-tjenesten.
3. Endre kryssreferanse til å arve fra Arkivenhet.
4. Nevn begresninger for kryssreferanser fra Noark 5 versjon
   4-standarden i tjenestegrensesnittet.

Jeg sender inn konkret forslag til endring som patch via github.
