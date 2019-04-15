Korriger relasjonsnøkkelliste for Mappe
=======================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.16 (Mappe)
         Sidenummer  133
        Linjenummer  n/a
    Innsendingsdato  2019-04-15
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder side 133 og 134.

Spesifikasjonens del 7.2.1.16 (Mappe) lister opp en rekke relasjoner
aktuelle for en mappe, men når en ser på eksemplet på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ er det ingen av
relasjonene der som er omtalt i spesifikasjonen.  Base-URL er
forskjellig, dvs. at http://rel.kxml.no/noark5/v4/api/arkivstruktur/
og http://rel.kxml.no/noark5/v4/api/metadata/ brukes i
spesifikasjonen, mens http://rel.kxml.no/noark5/v4/ brukes i
eksempelet.

Selv om vi antar eksempelet har en skrivefeil, og
http://rel.kxml.no/noark5/v4/ skulle vært
http://rel.kxml.no/noark5/v4/api/arkivstruktur/, så er det likefullt
noen relasjoner som ikke er omtalt i spesifikasjonen:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/avslutt-mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-basisregistrering/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-journalpost/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-presedens/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-sakspart/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-sekundaerklassifikasjon/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-undermappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/presedens/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseArkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseKlasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseSekundaerKlassifikasjon/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/sakspart/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/utvid-til-moetemappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/utvid-til-saksmappe/

Flere av disse relasjonene ser ut til å være operasjoner det ville
vært nyttig å ha med i spesifikasjonen.  For eksempel er det ellers
uklart hvordan lage en ny basisregistrering knyttet til en mappe.

Det er til gjengjeld også noen relasjoner som kun finnes i
spesifikasjonen og ikke i eksempelet.

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/nasjonaleidentifikator/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-nasjonalidentifikator/
 * http://rel.kxml.no/noark5/v4/api/metadata/dokumentmedium/
 * http://rel.kxml.no/noark5/v4/api/metadata/mappetype/

Jeg mistenker for eksempel at /arkivdel/ og /referanseArkivdel/
omhandler samme relasjon, dvs. hvordan finne "foreldrearkivdel" for
den gitte mappen.  Jeg mistenker det samme for /klasse/ og
/referanseKlasse/.

Problemet er relatert til [mangelmelding
#28](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/28)
om opprettelse av journalpost og bruken av arv og [mangelmelding
#100](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/100)
om relasjonene for mappe/ny-mappe/undermappe.

Ønsket endring
--------------

Jeg er litt i tvil om hva som er riktig løsning her, da det kommer an
på hvordan arv skal håndteres og hvordan relasjoner skal representeres
som JSON og ved oppretting og oppdatering, men foreslår i første
omgang at følgende nye relasjonsnøkler legges inn i tabellen i
Dokumentdel 7.2.1.16 (Mappe) på side 133:

| **Tag**   | **Verdi**                                                                |
| --------- | ------------------------------------------------------------------------ |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-basisregistrering/     |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-journalpost/           |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-moeteregistrering/     |

Følgende relasjonsnøkler skal så fjernes:

| **Tag**   | **Verdi**                                                                |
| --------- | ------------------------------------------------------------------------ |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivdel/              |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klasse/                |

I tillegg trenger rel.kxml.no oppdatering slik at den stemmer overens
med spesifikasjonen.

Merk at denne tilnærmingen er basert på at en velger tilnærmingen med
ny-entitettype i stedet for utvid-til-entitettype.  Merk videre at det
forsatt er problemer med referanse-attributtene som heller bør
representeres som relasjoner til Bruker og Mappe.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/140 .
