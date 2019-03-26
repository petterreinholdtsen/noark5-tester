Savner standardisert felt for ekstern dokumentreferanse
=======================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5
           Kategori  Versjon 4.0
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com>
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Korrespondanse mellom organisajoner og etater har gjerne intern og
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

Tilsvarende felt finnes i GeoIntegrasjons-standarden omtalt på
`http://geointegrasjon.no/standard/`, både som felt noekkel (muligens
det samme som SakEksternNoekkel, referanseEksternNoekkel,
referanseMappeEksternNoekkel etc.) under punkt 4.4.5 EksternNoekkel
eller feltet deresReferanse under punkt 4.4.8 Korrespondansepart, som
begge ser ut til å ha felt for eksterne referanser.

Vi foreslår at et tekststrengfelt for ekstern referanse legges inn i
metadatakatalogen og i dokumentbeskrivelse.

Denne mangelmeldingen er basert på tips fra Mona Henriksen i
Fredrikstad kommune, som etterlyste tilsvarende felt i Arkivfaglig
forum på Facebook i 2016.

Ønsket endring
--------------

FIXME finn på feltnavn og hvor det bør inn i Noark 5-standarden.
