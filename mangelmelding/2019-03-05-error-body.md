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
returneres en feil.  Se for eksempel
https://developers.google.com/drive/api/v3/handle-errors for hvordan
det kan gjøres.

Et annet eksempel er for lagrings-API-spesifikasjonen S3, dokumentert
på https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html .

https://blog.restcase.com/rest-api-error-codes-101/

Evrys implementasjon:

```
{
  "Message": "Uautorisert bruker '' eller det er ikke mulig til å autentisere brukeren."
}
```

Nikitas implementasjon:

```
{
  "error": "unauthorized",
  "error_description": "Full authentication is required to access this resource"
}
```

Ønsket endring
--------------

FIXME Beskriv JSON som returneres med tilbakemelding om konkret hva
som er galt.
