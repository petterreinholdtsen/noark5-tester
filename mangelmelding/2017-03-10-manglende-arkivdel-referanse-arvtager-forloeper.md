Relasjoner mellom Arkivdel-instanser bør være relasjoner, ikke attributter
==========================================================================

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
referanseArvtager (M203) bør endres til pekere/relasjoner mellom
Arkivdel-instanser.  Det er jo rent faktisk peker mellom to
Arkivdel-instanser.  Relasjonen fungerer på samme måte som
forrige/neste- og til/fra-relasjonene i Moetemappe og
Moeteregistrering, og ligner på relasjonen underklasse/undermappe bare
at den går begge veier.  I tillegg til relasjoner, så trengs det
relasjonsnøkler til bruk i _links-listene.

Se [mangelmelding
#100](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/100)
for konkret forslag til hvordan undermappe, underarkiv og underklasse håndteres.

Foreslår at relasjons-navnene gjøres kortere og mer beskrivende med
entitetsnavn i relasjonsnavnet.  Konkret foreslår jeg at en bruker
forrigeArkivdel/nesteArkivdel i stedet for de feltnavnene for
M202/M203 som brukes i XML, slik at relasjonsnavnet inneholder hvilken
entitetstype relasjonen peker på.

Det bør nevnes i spesifikasjonen av hvis en oppdaterer en slik
relasjon på den ene "siden", så skal den automatisk dukke opp på den
andre siden av relasjonen.  Det gjelder i grunnen alle slike
relasjoner, så det hører kanskje hjemme i kapittel 6 eller i den
generelle delen om UML-diagrammene i kapittel 7?  Foreslår at det
legges inn en beskrivelse i kapittel 6, samt oppdaterte
attributter/relasjoner i kapittel 7.

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

Legg til følgende formulering i kapittel 6 under overskriften
«Oppdatere referanser mellom objekter», like før overskriften «For å
opprette ny referanse»:

> Når en oppdaterer en toveis relasjon mellom to instanser med navn på
> begge sider , så blir den også synlig i den andre ennen av
> relasjonen.  For eksempel hvis en legger inn en lenke fra en
> Arkivdel A til forrige Arkivdel B, så blir det automatisk en lenke
> til neste Arkivdel A i Arkivdel B.
