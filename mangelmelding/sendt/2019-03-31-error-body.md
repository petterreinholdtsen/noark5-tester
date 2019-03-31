Hvilken nyttelast skal returneres ved feil?
===========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger avklaring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6
         Sidenummer  28
        Linjenummer  n/a
    Innsendingsdato  2019-03-31
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det bør beskrives hva som skal returneres i HTTP «body» når det
returneres en feil, for å sikre at API-klienter vet hvordan de kan
finne ut mer om hva som feilet.  I dag gjøres dette på to ulike måter
i utkastene til implementasjon av API-spesifikasjonen.  Slik gjøres
det i Nikitas implementasjon:

```
{
  "error": "unauthorized",
  "error_description": "Full authentication is required to access this resource"
}
```

Det er helt ulikt hvordan det gjøres i Evrys implementasjon:

```
{
  "Message": "Uautorisert bruker '' eller det er ikke mulig til å autentisere brukeren."
}
```

Returverdien bør ses i sammenheng med hvordan andre resultater fra
APIet ser ut.  Det vil for eksempel være enklere for en API-klient
hvis det alltid returneres et JSON-objekt (det vil si omkranset av
{...}) både på toppnivå, som søkeresultat og for enkeltoppføringer.
Jeg tenker her spesielt på at en bør tenke på formattering av
feilmeldinger når en bestemmer hvordan tomme lister ([mangelmelding
#18](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/18)
og listeresultater ([mangelmelding
12](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/12))
skal formatteres.

Det er mange måter å gjøre dette på.  Det kan være nyttig å se på hva
[Google Drive](https://developers.google.com/drive/api/v3/handle-errors) og
[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html)
har spesifisert rundt feilmeldinger.  En kan også hente inspirasjon
fra bloggposten [REST API Error Codes
101](https://blog.restcase.com/rest-api-error-codes-101/) som går
igjennom flere tjenester og metoder.

Google Drives feilresponser kan se slik ut:

```
{
  "error": {
    "errors": [
      {
        "domain": "global",
        "reason": "notFound",
        "message": "File not found {fileId}"
      }
    ],
    "code": 404,
    "message": "File not found: {fileId}"
  }
}

```

Amazon S3s feilresponser kan se slik ut:

```
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>NoSuchKey</Code>
  <Message>The resource you requested does not exist</Message>
  <Resource>/mybucket/myfoto.jpg</Resource> 
  <RequestId>4442587FB7D0A2F9</RequestId>
</Error>
```

Jeg foreslår at feilmeldinger struktureres som JSON-objekt med
«feil»-attributt ala det Google Drive bruker.  Ved å strukturere
JSON-responsen som JSON-objekt med «feil»-attributt gis API-klienter
mulighet til å oppdage feil ved se etter «feil»-attributtet i
JSON-responsen i tillegg til å sjekke HTTP-statuskoden.  Det gjør det
mulig for klientkoden å kun forholde seg til JSON-responsen internt,
og kan forenkle implementeringen for API-klienter.  Det kan dermed bli
seende omtrent slik ut:

```
{
  "feil": {
    "kode": 404
    "beskrivelse": "Not Found: arkivstruktur/arkivdel/9d5bda48-52b5-11e9-abc0-002354090596/"
    "merInfo": "https://url/til/dokumentasjon/som/forklarer/feilen/"
  }
}
```

Det kan være hensiktsmessig å returnere informasjon om flere feil i
samme melding, f.eks. hvis oppretting av en entitetsinstans blir
avvist på grunn av feil i attributter, der det er feil i flere
attributter.  I så fall bør det legges til et liste-attributt med
individuelle feil, ala det Google Drive-feilmeldingene legger opp til.
Kanskje noe ala dette kunne fungere:

```
{
  "feil": {
    "kode": 400,
    "beskrivelse": "Bad Request: arkivstruktur/arkivdel/9d5bda48-52b5-11e9-abc0-002354090596/",
    "merInfo": "https://url/til/dokumentasjon/som/forklarer/feilen/",
    "feil": [
       {
         "begrunnelse" : "illegal value in tittel",
         "beskrivelse": "can not be empty or only contain whitespace"
       },
       {
         "begrunnelse" : "illegal value in dokumentmedium",
         "beskrivelse": "must have value from Dokumentmedium metadata set"
       },
    ]
  }
}
```

Selv om dette utvilsomt kan være nyttig med detaljert informasjon om
feilen, så foreslår jeg å gå for en enklere modell, for å gjøre det
enklere å implementere API-et.  Et alternativ kan være å utbrodere i
«beskrivelse», hvis det feltet gjøres til et fritekstfelt uten kjente
verdier.

Et spørsmål som må avklares er om teksten i attributten «beskrivelse»
alltid skal ha samme språk, eller om API-tjenermaskinen kan velge om
det skal sendes over på f.eks. engelsk, bokmål eller nynorsk.  Det er
enklere for API-klienter å maskinelt tolke meldingen hvis meldingene
er kjente og alltid har et fast språk, mens det er vanskeligere for
klienten hvis meldingen må oversettes på klientsiden før presentasjon
til en bruker, med mindre alle mulige meldinger er spesifisert i
API-spesifikasjonen slik at klienter kan oversette alle mulige
meldinger.  En mulig løsning her er å gi ut meldingen på to språk, et
fast og en oversettelse, ala dette, der meldingene er markert med to
eller trebokstavs språkkode i tråd med ISO 639:

```
{
  "feil": {
    "kode": 404
    "beskrivelse": {
       "en": "Not Found: {info-om-instans-sti/navn}",
       "nb": "Fant ikke : {info-om-instans-sti/navn}"
    }
    "merInfo": "https://url/til/dokumentasjon/som/forklarer/feilen/"
  }
}
```

Jeg foreslår at meldingene alltid er på samme språk, og har gått for
engelsk i mitt forslag.


Ønsket endring
--------------

Legg inn en ny seksjon i kapittel 6 etter del 6.2 (Validering av data)
som lyder som følger:

> 6.3 Håndtering av API-feil
>
> API-et returnerer to nivåer av tilbakemeldinger ved feil:
> 
>  * HTTP statuskoder og meldinger i HTTP-hodefelt
>  * Et JSON-objekt som HTTP-responsens innhold (aka «body») med
>    ytterligere detaljer for å forstå hva som gikk galt.  Denne har
>    en attributt «feil» som peker til et JSON-objekt med feltene
>    «kode», «beskrivelse» og «merInfo».
>
> Som et eksempel, hvis en forsøker å hente ned en instans
> «.../arkivstruktur/arkivdel/9d5bda48-52b5-11e9-abc0-002354090596/» som
> ikke finnes, så vil JSON-responsen være strukturert på denne måten:
> 
> ```
> {
>   "feil": {
>     "kode": 404
>     "beskrivelse": "Not Found: arkivstruktur/arkivdel/9d5bda48-52b5-11e9-abc0-002354090596/"
>     "merInfo": "https://url/til/dokumentasjon/som/forklarer/feilen/"
>   }
> }
> ```
>
> | Felt                  | Beskrivelse                                                                                |
> |-----------------------|--------------------------------------------------------------------------------------------|
> | kode                  | Feilkoden, samme som HTTP statuskoden til feilmeldingen                                    |
> | beskrivelse           | En kort melding som beskriver feilen                                                       |
> | merInfo (valgfritt)   | En URL med peker til en ressurs med mer informasjon om feilen og med forslag til løsninger |
>
> Lenken i merInfo kan peke til en leverandørspesifikk side med informasjon om feilsøking.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/93 .
