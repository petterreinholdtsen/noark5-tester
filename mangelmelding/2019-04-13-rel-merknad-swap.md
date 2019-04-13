Snu relasjonene til Merknad?
============================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.17 (Merknad)
         Sidenummer  141
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også side 83 og 90.

Relasjonen fra Merknad til Mappe, Basisregistrering og
Dokumentbeskrivelse beskrevet på side 142 i del 7.2.1.17 (Merknad) er
motsatt vei (Destination → Source) enn andre tilsvarende relasjoner,
som enten er (Source → Destination) eller (Bi-Directional).  Hva er
det som gjør at relasjonene til Merknad er snudd andre veien i forhold
til de andre relasjonen av type *Association*?

Med mindre det er en god grunn til at denne relasjonen må være i
motsatt retning i forhold til alle andre tilsvarende relasjoner, så
foreslår jeg at den snus til samme vei som de øvrige, slik at det blir
mindre å forklare i spesifikasjonen.

Her er relasjonene slik de fordeler seg i dag i kapittel 7:

| Antall | Relasjon                                  |
|--------|-------------------------------------------|
|      6 | **Association** (Destination → Source)    |
|     10 | **Association** (Source → Destination)    |
|     12 | **Association** (Bi-Directional)          |
|     13 | **Aggregation** (Destination → Source)    |
|     22 | **Aggregation** (Bi-Directional)          |
|     49 | **Generalization** (Source → Destination) |

Kan det være en god ide å sørge for at alle rettede relasjonene i
spesifikasjonen konsistent enten går fra kilde til mål eller fra mål
til kilde, for å redusere sjansen for at at de som leser
spesifikasjonen leser feil?  I og med at dagens tabeller har kilde til
venstre for mål, tror jeg det er lurt at retningen er kilde til mål.
Hvis det anses som en god ide, så bør kanskje de 13 relasjonene som
fortsatt går motsatt vei også etter at dette forslaget går igjennom,
endres til å bli fra kilde til mål, hvis en vil redusere hvor store
endringer som må gjøres fra dagens spesifikasjon.

Ønsket endring
--------------

Bytt om innholdet i i de tre relasjonstabellene på side 83, 90 og 142
slik at det beskrevne retningen på forholdet til Merknad går motsatt
vei, slik at tabelloppføringene går fra dette:

| **Relasjon**                             | **Kilde**                                                | **Mål**                | **Merknad** |
| ---------------------------------------- | -------------------------------------------------------- | ---------------------- | ----------- |
| **Association** (Destination → Source)   | merknad 0..* Merknad                                     | Mappe                  |             |
| **Association** (Destination → Source)   | merknad 0..* Merknad                                     | Basisregistrering      |             |
| **Association** (Destination → Source)   | merknad 0..* Merknad                                     | Dokumentbeskrivelse    |             |

til dette:

| **Relasjon**                           | **Kilde**           | **Mål**              | **Merknad** |
|----------------------------------------|---------------------|----------------------|-------------|
| **Association** (Source → Destination) | Mappe               | merknad 0..* Merknad |             |
| **Association** (Source → Destination) | Basisregistrering   | merknad 0..* Merknad |             |
| **Association** (Source → Destination) | Dokumentbeskrivelse | merknad 0..* Merknad |             |

Alternativt, hvis retningen er ment å være vesentlig, beskriv i detalj
i spesifikasjonen hva som skal forstås ut fra retningen på disse
relasjonene.
