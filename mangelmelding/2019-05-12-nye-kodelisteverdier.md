Legg inn nye kodelisteverdier fra Noark 5 versjon 4.0 
=====================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.2.3 (Avskrivningsmåte)
         Sidenummer  168
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også 7.2.2.17 (Korrespondanseparttype) på side 179.

I [metadatakatalog.xsd for Noark 5 versjon
4](https://github.com/arkivverket/schemas/blob/master/N5/v4.0/metadatakatalog.xsd)
er det tatt inn noen nye verdier i metadatafeltene M087
korrespondanseparttype og M619 avskrivningsmaate.

M087 korrespondanseparttype har fått ny akseptert verdi "Medavsender".

M619 avskrivningsmaate har fått nye aksepterte verdier "Besvart med
notat" og "Saken ble avsluttet".

Disse verdiene må inn i de aktuelle kodelistene.

Ønsket endring
--------------

Endre 7.2.2.3 (Avskrivningsmåte) på side 168, legg inn nye verdier i
Attributter-tabellen:

| **Navn**                  | **Merknad** | **Multipl.** | **Kode** | **Type** |
| ------------------------- | ----------- | ------------ | -------- | -------- |
| Besvart med notat         |             |              | BN       |          |
| Saken ble avsluttet       |             |              | SA       |          |

Endre 7.2.2.17 (Korrespondanseparttype) på side 179, legg inn ny verdi
i Attributter-tabellen:

| **Navn**                | **Merknad** | **Multipl.** | **Kode** | **Type** |
| ----------------------- | ----------- | ------------ | -------- | -------- |
| Medavsender             |             |              | IS       |          |
