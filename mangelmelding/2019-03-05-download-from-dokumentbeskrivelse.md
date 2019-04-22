Nedlasting av alternative filformater direkte fra dokumentbeskrivelse?
======================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Kan det være en ide å bruke Accept-hodefeltet til å laste ned fil(er)
direkte fra en dokumentbeskrivelse-entitet, der samme dokument finnes
i flere formater koblet til ulike dokumentobjekt-entiteter?  Det vil
gjøre det mulig å be om å få laste ned en av flere filer fra et
dokumentbeskrivelse-objekt.

Det kan gjøres ved å legge inn relasjonsnøkkelen
'http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/' i \_links for
dokumentbeskrivelse, og at denne kan brukes til å laste ned en av de
tilhørende dokumentobjekt-filene?  Dermed kunne en laste ned enten
PDF- eller XLS-fil ved å gjøre en slik forespørsel:

```
GET .../referanseFil
Accept: application/pdf; q=0.5, application/vnd.ms-excel,
```

Det må i så fall beskrives hvordan API-tjenesten skal velge mellom
likeverdige formater og versjoner.  Det virker naturlig å velge høyest
tilgjengelig versjon, men det er mer vanskelig å vite hva som skal
gjøres hvis foretrukket format kun finnes med eldre versjonsnummer.
En slik tilnærming vil gjøre det vanskeligere for en
API-implementasjon å vite hvilken fil som skal returneres.

Ønsket endring
--------------

FIXME Formuler konkret forslag
