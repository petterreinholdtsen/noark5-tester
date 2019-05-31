Mangler organisasjonsnummer i metadatakatalogen?
================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5
           Kategori  versjon 5
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

jeg finner ikke en metadatadefinisjon for organisasjonsnummer i
metadatakatalogen for hverken Noark 5 versjon 3, 4 og 5.  Et slikt
felt hadde vært nyttig for å knytte sammen saker og koble
organisasjoner registrert i Norges enhetsregister med arkivsaker og
dokumenter.  Feltet finnes i GeoIntegrasjon som
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

Legg inn felt for organisasjonsnummer i metadatakatalogen og bruk det
i XML-skjemaet for arkivstruktur.xml i typene part og
korrespondansepart.
