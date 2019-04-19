Hvordan vedlikeholdes kodeliste-oppføringer?
============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.2 (Kodelister)
         Sidenummer  165
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder del 7.2.2 (Kodelister) på side 165 og etterfølgende
sider.

Det fremgår ikke fra spesifikasjonen hvordan kodelister og andre
metadatalister får nye oppføringer, eller hvordan utdaterte
oppføringer fjernes.  Det er ikke oppgitt noen ny-* type relasjoner
for disse, og det er ikke nevnt noe om hvor de kan finnes.  Uten slike
operasjoner vil det ikke være mulig å vedlikeholde kodelistene via
API-et.

Det mangler både informasjon om hvordan POST for nye oppføringer skal
fungere (dvs. hvordan ny-* URL der slike POST skal gjøres skal finnes)
og hva som er den unike URL for hver enkelt metadataoppføring der PUT
og DELETE skal utføres.

I GeoIntegrasjons-spesifikasjonen har alle oppføringer i kodenlister
en bolsk verdi "erGyldig" som jeg antar markerer om kodeverdien kan
brukes ved oppretting og endring av instanser som bruker kodelisten,
for å sikre at utdaterte kodelisteverdier fortsatt er registrert i
databasen selv om de ikke lenger skal brukes.  Det virker som en god
ide også for tjenestegrensesnittet.  Foreslår at dette feltet heter
"aktiv" og antas å være "true" hvis det ikke er satt, slik at det kun
skal være satt for verdier som ikke skal brukes.

En ide for oppretting er å gjøre tilsvarende som for
http://localhost:8092/noark5v4/hateoas-api/arkivstruktur , der det
finnes relasjonsnøkler for .../ny-arkivskaper/ og .../ny-arkiv/ for å
lage nye instanser av arkivskaper og arkiv.  Ideen er å definiere et
nytt relasjonsnøkkeltre med base
http://rel.arkivverket.no/noark5/v4/api/metadata/ der alle
ny-*-relasjonene for oppretting av nye metadataoppføringer listes opp,
tilsvarende det som beskrives i mangelmelding #107 for arkivstruktur
og sakarkiv.  Det nye relasjonsnøkkeltreet bør inneholde lenke til
alle kodelister som er tilgjengelig.  Slike ny-*-relasjoner skal kun
være synlige for priviligerte brukere som har rett til å opprette nye
kodelisteoppføringer.  I tillegg til POST må i hvert fall operasjonene
GET og OPTIONS (helst også PATCH) fungere på disse ny-*-oppføringene,
tilsvarende for andre ny-*-operasjoner.

En tilsvarende ide for oppdatering og sletting er å gi hver
kodeliste-oppføring en SystemID og 'self'-relasjonnøkkel, for eksempel
for dokumentmedium href vil være
`http://localhost:8092/noark5v4/hateoas-api/metadata/dokumentmedium/&lt;systemID&gt;/`,
som så kan brukes til PUT og DELETE-opperasjoner ved oppdatering og
sletting.  Den bør naturligvis også fungere for GET for å kunne vite
hva som kan endres, selv om den normale måten å få ut kodelister og
andre metadata vil være å hente ut listen via den kjente
relasjonsnøkkelen bruker, for eksempel
http://rel.kxml.no/noark5/v4/api/metadata/dokumentmedium/ for alle
dokumentmedium.

Her er for eksempel hvordan arkivstatus kan se ut når en tar GET mot
href for relasjonen
`http://rel.kxml.no/noark5/v4/api/metadata/arkivstatus/`:


```
{
  "results": [
    {
      "systemID": "9ed3f5d3-9934-446d-85b8-b2ada9498aa7",
      "kode": "O",
      "beskrivelse": "Opprettet",
      "_links": [
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/9ed3f5d3-9934-446d-85b8-b2ada9498aa7/",
          "rel": "self"
        },
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/9ed3f5d3-9934-446d-85b8-b2ada9498aa7/",
          "rel": "http://rel.kxml.no/noark5/v4/api/metadata/arkivstatus/"
        }
      ]
    },
    {
      "systemID": "b94eb9cf-e71f-4d68-964b-b68c7f9962b6",
      "kode": "A",
      "beskrivelse": "Avsluttet",
      "_links": [
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/b94eb9cf-e71f-4d68-964b-b68c7f9962b6/",
          "rel": "self"
        },
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/b94eb9cf-e71f-4d68-964b-b68c7f9962b6/",
          "rel": "http://rel.kxml.no/noark5/v4/api/metadata/arkivstatus/"
        }
      ]
    },
    {
      "systemID": "43421e68-62bf-11e9-ae3a-002354090596",
      "kode": "U",
      "beskrivelse": "Påtenkt",
      "aktiv": false,
      "_links": [
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/43421e68-62bf-11e9-ae3a-002354090596/",
          "rel": "self"
        },
        {
          "href": "http://localhost:49708/api/metadata/arkivstatus/43421e68-62bf-11e9-ae3a-002354090596/",
          "rel": "http://rel.kxml.no/noark5/v4/api/metadata/arkivstatus/"
        }
      ]
    }
  ],
  "_links": [
    {
      "href": "http://localhost:49708/api/metadata/arkivstatus/",
      "rel": "self",
    }, {
      "href": "http://localhost:49708/api/metadata/arkivstatus/",
      "rel": "http://rel.kxml.no/noark5/v4/api/metadata/arkivstatus/"
    }
  ]
}
```

Det bør være krav om at DELETE av en eller flere kodeliste-verdier kun
kan gjennomføres hvis det ikke finnes noen instanser i databasen som
bruker den aktuelle kodeliste-verdien.

Ønsket endring
--------------

Legg inn i starten av dokumentdel 7.2.2 (Kodelister) en gjennomgang av
hvordan kodelister representeres i JSON og hva som gjelder generelt
for slike, der det står at de har SystemID og "self"-relasjonsnøkkel
som kan brukes ved oppdatering og sletting.  Definer relasjonsnøkler
ny-* for å opprette nye kodelisteoppføringer for hver enkelt
kodeliste.

Beskriv videre i samme del hvilke relasjonsnøkler som skal være
tilgjengelig på metadata-nivåen under toppen, ala det som er beskrevet
i mangelmelding #107 for andre deler av API-et.

Jeg sender inn konkret forslag til endring som patch via github.
