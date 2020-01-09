Er Mappe.mappetype overflødig eller kan det beskrives hva den skal brukes til?
==============================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Noark 5.5.0 TG versjon 1.0
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.16 (Mappe)
         Sidenummer  135
        Linjenummer  n/a
    Innsendingsdato  2020-01-09
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I listen over attributter knyttet til Mappe, så står det følgende:

| **Navn**  | **Merknad**   | **Multipl.**  | **Kode**  | **Type**  |
|-----------|---------------|---------------|-----------|-----------|
| mappetype | angir mappetype som blant annet kan brukes som hint til hva som ligger i virksomhetsspesifikkemetadata| \[0..1\] | | Mappetype |

Dette feltet står ikke i arkivstruktur.xsd for Noark 5 versjon 5.5, og
det er uklart hva det skal brukes til.  Det er ingen nærmere
informasjon i beskrivelsen for metadata-kodelisten Mappetype.

Vårt beste gjett er at dette er et felt som er ment å formidle om det
er snakk om en mappe, saksmappe eller moetemappe.  Det trengs ikke en
egen attributt for dette, da det vil fremgå av innholdet i _links, der
'self'-lenken kan brukes til å finne en gitt instans entitet/type,
jamfør beskrivelsen under overskriften "Identifisere enhetstype" i
kapittel 6.

Attributten er også listet opp i beta 1.0, og sidenummerene oppgitt
i ønsket endring er fra den PDF-en.

Ønsket endring
--------------

Fjern attributten mappetype fra listen over attributter knyttet til
Mappe i del 7.2.1.16 på side 135, og fjern Mappetype i del 7.2.2.19 på
side 180 fra listen over metadata-kodelister.

Fjern også henvisning til mappetype fra del 6.1.14 (Preutfylling av
objekt) på siden 18 og alle UML-diagram.
