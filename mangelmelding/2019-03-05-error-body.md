Hvilken nyttelast skal returneres ved feil?
===========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
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

Det bør beskrives hva som skal returneres i HTTP "body" når det
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

Returverdien bør ses i sammenheng med hvordan andre resultater fra API
ser ut.  Det vil for eksempel være enklere for en API-klient hvis det
alltid returneres et JSON-objekt (aka {...}) både på toppnivå, som
søkeresultat og for enkeltoppføringer.  Jeg tenker her spesielt på at
en bør tenke på feilmeldinger når en bestemmer hvordan tomme lister
([mangelmelding
#18](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/18)
og listeresultater ([mangelmelding
12](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/12))
skal formatteres.

Det er mange måter å gjøre dette på.  Det kan være lurt å se på
hvordan [Google
Drive](https://developers.google.com/drive/api/v3/handle-errors) og
[Amazon
S3](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html)
har spesifisert rundt feilmeldinger.

En kan også hente inspirasjon fra bloggposten [REST API Error Codes
101](https://blog.restcase.com/rest-api-error-codes-101/) som går
igjennom flere tjenester og metoder.

Ønsket endring
--------------

FIXME Beskriv JSON som returneres med tilbakemelding om konkret hva
som er galt.

```
{
  "status": 401
  "error": "Authentication Required"
  "more_info": "http://url-to-dokumentation"
}
```
