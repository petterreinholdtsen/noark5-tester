DNummer eller dNummer som feltnavn?
===================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.9
         Sidenummer  198
        Linjenummer  n/a
    Innsendingsdato  2019-03-27
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder sidene 198, 199, 229 og 250 samt delene 7.2.3.9
(KorrespondansePerson) og 7.2.3.14 (SakspartPerson).

Det er ulik presentasjon av felt for D-nummer i forskjellige
UML-diagrammer og entiteter.  I entiteten
NasjonaleIdentifikatorer.Personidentifikator er det stavet «dNummer»,
mens i Sakarkiv.KorrespondansepartPerson og Sakarkiv.SakspartPerson er
det stavet «DNummer».  Den samme forskjellen er reflektert i teksten.
Det vil være enklere for brukere av API-et hvis samme feltstaving
brukes over alt.  Foreslår derfor at «dNummer» endres til «DNummer»
eller «DNummer» endres til «dNummer» over det hele.  «dNummer» virker
å være mest i tråd med andre feltnavn, som har kamelformat.

I tillegg til felt for D-nummer, hva med H-nummer som omtalt i
«[Hjelpenummer for personer uten kjent
fødselsnummer](https://sh.ehelse.no/hkode/arkiv/Delte%20dokumenter/KITH/upload/939/R11-98Hjelpenummer.pdf)»
av Torbjørn Nystadnes, Kompetansesenter for IT i helsevesenet AS
(KITH).  KITH-rapport, Rapportnummer 11/98, ISBN 82-7846-051-5,
1998-12-11?

Et relatert problem i denne sammenhengen er at XML-formatet for
avleveringspakker mangler felt for både D-nummer og fødselsnummer i
korrespondansepart og sakspart, slik at det er uklart hvorvidt dette
feltet kan avleveres ved eksport fra arkivsystemet.  Dette er meldt
inn som [sak #80 i
github](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/80).

Ønsket endring
--------------

Endre i den tekstlige beskrivensen av KorrespondansepartPerson og
SakspartPerson til å bruke «dNummer» i stedet for «DNummer».
Tilsvarende må det også endres i UML-diagrammene
uml-klasse-avskrivning og uml-klasse-person-og-organisasjonsdata.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/87 .
