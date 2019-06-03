Feil attributtnavn for kodelisteverdier i kapittel 6?
=====================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.3 (Opprette objekter (Create))
         Sidenummer  17
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også eksempler på side 18, 19, 20 osv. i hele kapittel 6.

I flere JSON-eksempler i kapittel 6 så er kodelisteverdier oppgitt med
kode og beskrivelse som del av en instans i arkivet.  Det første
eksemplet gjelder en Mappe og ser slik:

```Python
{
    "mappetype": {
        "kode": "BYGG",
        "beskrivelse": "Byggesak"
    },
    "tittel": "angi tittel på mappe",
    "dokumentmedium": {
        "kode": "E",
        "beskrivelse": "Elektronisk arkiv"
    },
    "_links": [
        {
            "href": "http://localhost:49708/api/kodelister/Dokumentmedium{?$filter&$orderby&$top&$skip}",
            "rel": "https://rel.arkivverket.no/noark5/v4/api/administrasjon/dokumentmedium/",
            "templated": true
        },
        {
            "href": "http://localhost:49708/api/kodelister/Mapetype{?$filter&$orderby&$top&$skip}",
            "rel": "https://rel.arkivverket.no/noark5/v4/api/administrasjon/mappetype/",
            "templated": true
        }
    ]
}
```

Det er bare det at i kapittel 7 er det ikke beskrevet noe som heter
`beskrivelse` for kodelister.  Det som ligner er under kolonnen
*Navn*, som i eksempel her hentet fra Mappetype:

| **Navn**                       | **Merknad** | **Multipl.** | **Kode** | **Type** |
| ------------------------------ | ----------- | ------------ | -------- | -------- |
| Merknad fra saksbehandler      | Valgfri     |              | MS       |          |
| Merknad fra leder              | Valgfri     |              | ML       |          |
| Merknad fra arkivansvarlig     | Valgfri     |              | MA       |          |

Tilsvarende eksempel hentet fra Dokumentmedium:

| **Navn**                                | **Merknad** | **Multipl.** | **Kode** | **Type** |
| --------------------------------------- | ----------- | ------------ | -------- | -------- |
| Fysisk medium                           |             |              | F        |          |
| Elektronisk arkiv                       |             |              | E        |          |
| Blandet fysisk og elektronisk arkiv     |             |              | B        |          |

Kapittel 6 og 7 bør bruke konsistent navngiving av den tekstlige
beskrivelsen av en kode i en kodeliste.  Enten bør det brukes **navn**
i eksemplene i kapittel 6, eller så bør alle tabellene i kapittel 7
bytte overskrift til **Beskrivelse**.

Uansett bør det forklares nærmere hvordan kodeliste-verdier skal
refereres i JSON, jamfør [mangelmelding
#148](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/148).

Jeg foreslår å endre i kapittel 6 til **navn**, da det er kortere enn
**beskrivelse** og dermed sparer oss for noen få bytes sendt over
protokollen, samt forklare at Navn blir navn i JSON-lister.

Ønsket endring
--------------

Endre eksempler til å bruke **navn** i stedet for **beskrivelse** i
JSON og beskriv i starten av 7.2.2 at kodelisteverdienes navn i
tabellen henvises til med JSON-attributten `navn`.  Alternativt kan en
gjøre som foreslått i mangelmelding [#148](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/148) og alltid bruke kode-verdien i JSON-instanser, og dermed unngå hele spørsmålet.
