Klargjør om attributtnavn 'filstørrelse' er korrekt
===================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.1
         Sidenummer  29
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder også side 50, 52, 54, 105 og 203.

Spesifikasjonen bruker attributtnavnet 'filstørrelse' flere steder:

 * 7.1 (Om UML og notasjon som er benyttet) UML-skjema for 'foto' side 29
 * 7.2.1 (Arkivstruktur) UML-skjema for 'dokumentobjekt' side 50, 52, 54
 * 7.2.1.7 (Dokumentobjekt) side 105
 * 7.2.3 (Sakarkiv) UML-skjema for 'dokumentobjekt' side 203

Dette virker å være eneste eksempel på et attributtnavn som inneholder
særnorske tegn, og stemmer ikke over ens med XSD-filer som i stedet
bruker 'filstoerrelse'.

FIXME finn autorative XSD-filer å henvise til

Eksempelet på side 29 omtaler datatyper 'foto', som ikke er nevnt
andre steder i spesifikasjonen.  Mangler definisjonen, eller bør
eksemplet endres til å kun bruke datatyper som er definert i
spesifikasjonen?

Attributten er ikke brukt på demonettstedet
http://n5test.kxml.no/api/arkivstruktur/dokumentobjekt, slik at det
ikke er noe hjelp å få der med tolkingen.

Den er heller ikke omtalt på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/, som
ser ut til å vise frem feil datastruktur (mappe) i stedet for
dokumentobjekt.

Ønsket endring
--------------

Endre attributtnavnet 'filstørrese' til 'filstoerrelse' alle steder
der det brukes i spesifikasjonen:

 * 7.1 (Om UML og notasjon som er benyttet) UML-skjema for 'foto' side 29
 * 7.2.1 (Arkivstruktur) UML-skjema for 'dokumentobjekt' side 50, 52, 54
 * 7.2.1.7 (Dokumentobjekt) side 105
 * 7.2.3 (Sakarkiv) UML-skjema for 'dokumentobjekt' side 203
