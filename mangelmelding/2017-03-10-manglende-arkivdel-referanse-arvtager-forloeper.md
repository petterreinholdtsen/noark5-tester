Relasjoner mellom Arkivdel-instanser bør ikke være attributter med SystemID-verdier
===================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  7.2.1.2 (Arkivdel)
         Sidenummer  66
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Arkivdel-attributtene med navn referanseForloeper (M202) og
referanseArvtager (M203) bør gjøres om til en peker/relasjon mellom
Arkivdel-instanser.  Denne relasjonen fungerer på samme måte som
forrige/neste- og til/fra-relasjonene i Moetemappe og
Moeteregistrering, og som en underklasse/undermappe bare at den går
begge veier.  I tillegg til relasjonene, så trengs det relasjonsnøkler
til bruk i _links-listene.

Se [mangelmelding
#100](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/100)
for konkret forslag til hvordan undermappe med venner skal håndteres.

Foreslår at relasjons-navnene gjøres kortere og mer beskrivende, og at
en bruker forrigeArkivdel/nesteArkivdel i stedet for de feltnavnene
for M202/M203 som brukes i XML, slik at relasjonsnavnet inneholder
hvilken entitetstype relasjonen peker på.

Det bør kanskje nevnes i spesifikasjonen av hvis en oppdaterer en slik
relasjon på den ene "siden", så skal den automatisk legges inn på den
andre siden relasjonen.  Det gjelder i grunnen alle slike relasjoner,
så det hører kanskje hjemme i kapittel 6 eller i den generelle delen
om UML-diagrammene i kapittel 7?  Foreslår at det legges inn en
beskrivelse i kapittel 6, samt oppdaterte attributter/relasjoner i
kapittel 7.

Ønsket endring
--------------

Legg inn følgende i del 7.2.1.2 (Arkivdel) sin tabell over Relasjoner
på side 65:

| **Relasjon**                              | **Kilde**                                                | **Mål**                | **Merknad** |
| ----------------------------------------- | -------------------------------------------------------- | ---------------------- | ----------- |
| **Aggregation** (Bi-Directional)           | forrigeArkivdel 0..1 Arkivdel                                   | nesteArkivdel 0..1 Arkivdel          | SystemID for forrige/neste Arkivdel avleveres som referanseForloeper(M202)/referanseArvtaker(M203). |

Legg inn to nye oppføringer i tabellen over relasjonsnøkler på side
66:

| **Tag**   | **Verdi**                                                                |
| --------- | ------------------------------------------------------------------------ |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/forrigearkivdel/          |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/nestearkivdel/            |

Dokumenter i spesifikasjonen at hvis en legger inn en slik lenke fra
en Arkivdel til en annen, så vil tilsvarende lenke dukke opp hos den
motstående instansen av Arkivdel.

