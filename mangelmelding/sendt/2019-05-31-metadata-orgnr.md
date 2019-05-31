Mangler standardisert måte å avlevere organisasjonsnummer
=========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5
           Kategori  versjon 5
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  2019-05-31
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det mangler en metadatadefinisjon for organisasjonsnummer i
metadatakatalogen, både i Noark 5 versjon 3, 4 og 5.  Et slikt felt
trengs for å knytte sammen saker og koble organisasjoner registrert i
Norges enhetsregister med arkivsaker og dokumenter.  Felt for
organisasjonsnummer finnes i GeoIntegrasjon som
Kontakt:organisasjonsnummer samt er omtalt i tjenestegrensesnittet som
SakspartEnhet.organisasjonsnummer,
Korrespondansepart.organisasjonsnummer og
NasjonaleIdentifikatorer.Enhetsidentifikator.

Det at organisasjonsnummer mangler i XML-skjema til
avleveringsformatet for Noark 5 versjon 3, 4 og 5 gjør det [uklart
hvordan partinformasjon skal
avleveres](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/80),
samt gjør at avleveringsformatet ikke kan brukes som utvekslingsformat
mellom implementasjoner av tjenestegrensesnittet.

Ønsket endring
--------------

Legg inn felt for organisasjonsnummer i metadatakatalogen og da det i
bruk i XML-skjemaet for arkivstruktur.xml som del av typene part og
korrespondansepart.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/199 .
