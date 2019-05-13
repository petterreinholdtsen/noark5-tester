Mangler standardisert felt for ekstern referanse
================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5
           Kategori  Versjon 4.0
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com>
        Dokumentdel  7.2.1.6 (Dokumentbeskrivelse)
         Sidenummer  89
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Korrespondanse mellom organisasjoner og etater har gjerne intern og
ekstern referanse som gjør det enklere for mottaker å finne korrekt
sak/mappe.  I offentlig forvaltning brukes gjerne saksid
(dvs. saksår/saksnummer), mens ikke-offentlige instanser gjerne har
andre strukturer på sine referanser (f.eks. initialer til
brevskribent).  Disse verdiene er ofte oppgitt i brevhodet som 'Vår
referanse' og 'Deres referanse'.

I Noark 4 var det et felt i tabellen AVSMOT (avsender/mottaker) som
het AM.REF (referanse) som kunne brukes til denne eksterne referansen.
Dette feltet ser ut til å være forsvunnet fra spesifikasjonen av Noark
5, og det er ikke åpenbart hvordan ekstern referanse kan tas vare på i
en Noark 5-løsning.

Feltet er et svært aktuelt felt å bruke blant annet i integrasjoner
med andre systemer, der det eksterne systemets ID kan lagres som en
ekstern referanse for å kunne søke opp aktuelle dokumenter og saker.
Det er dessuten svært nyttig å legge inn ekstern referanse i arkivet
for å effektivt kunne søke etter når en skal finne aktuell sak/mappe
for innkommende brev.

Det kan argumenteres med at slik referanse skal knyttes til en part,
og ikke et dokument, men i og med at ekstern referanse vil hentes fra
et konkret dokument virker det mest naturlig å knytte det til entiteten
Dokumentbeskrivelse.

Tilsvarende eksterne referanse felt finnes i
GeoIntegrasjons-standarden omtalt på
`http://geointegrasjon.no/standard/`, både som felt noekkel (muligens
det samme som SakEksternNoekkel, referanseEksternNoekkel,
referanseMappeEksternNoekkel etc.) under punkt 4.4.5 EksternNoekkel
eller feltet deresReferanse under punkt 4.4.8 Korrespondansepart, som
begge ser ut til å ha felt for eksterne referanser.

Da feltet er etterlyst og i bruk, så virker det fornuftig at det
legges inn et standardisert tekststrengfelt for ekstern referanse inn
i metadatakatalogen og under dokumentbeskrivelse i arkivstruktur.xsd.

Et alternativ er å bruke et felt i virksomhetsspesifikkeMetadata hos
Dokumentbeskrivelse eller Sakspart, jamfør endringsforslag #78.  Det
vil ikke kreve endring i XML-skjema.

Denne mangelmeldingen er basert på tips fra Mona Henriksen i
Fredrikstad kommune, som etterlyste tilsvarende felt i Arkivfaglig
forum på Facebook i 2016.

Ønsket endring
--------------

Legg inn ny attributt i tabell under 7.2.1.6 (Dokumentbeskrivelse) på
side 97:

| **Navn**         | **Merknad**  | **Multipl.** | **Type** |
|------------------|--------------|--------------|----------|
| eksternReferanse | Ekstern referanse på innkommende dokumenter.  Brukes til søk, kan ikke avleveres på deponi-formatet til Noark 5 versjon 4 og 5. | \[0..1\] | string |

Jeg sender inn konkret endringsforslag til API-spesifikasjonen for å
fikse dette, men det hadde vært nyttig med tilbakemelding på
endringsforslag #78 og denne mangelmeldingen for å konkret vite
hvordan det er best å skrive inn dette i spesifikasjonen.
