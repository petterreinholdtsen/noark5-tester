Korriger staving av attributtnavn «elektroniskSignaturSikkerhetsnivå» og tilhørende entitet
===========================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.19 (ElektroniskSignatur)
         Sidenummer  107
        Linjenummer  n/a
    Innsendingsdato  2019-04-05
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder teksten side 107 og 170, samt UML-diagramer på side 36, 52, 54
og 203.

Spesifikasjonen bruker attributtnavnet
«elektroniskSignaturSikkerhetsnivå» (med å) i beskrivelsen av datatype
ElektroniskSignatur og i flere UML-diagrammer.  Dette er en skrivefeil
for metadatafelt M507 «elektroniskSignaturSikkerhetsnivaa».
Relasjonsnøkkelnavnet er korrekt.  Tilsvarende bør entitetsnavnet
«ElektroniskSignaturSikkerhetsnivå» endre navn til
«ElektroniskSignaturSikkerhetsnivå».

Ønsket endring
--------------

Endre alle forekomster av «elektroniskSignaturSikkerhetsnivå» til
«elektroniskSignaturSikkerhetsnivaa» og alle forekomster av
«ElektroniskSignaturSikkerhetsnivå» til
«ElektroniskSignaturSikkerhetsnivå».

Når diagrammer som PlantUML er tatt i bruk i master-grenen
([mangelmelding #76](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/76)),
så skal jeg sende inn konkret endringsforslag for å fikse dette.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/105 .
