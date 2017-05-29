Klargjør om attributtnavn «journalår» (M013) er korrekt
=======================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.4
         Sidenummer  214
        Linjenummer  n/a
    Innsendingsdato  2017-05-29
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også side 54, 197, 198, 202, 203, 214, 222

Spesifikasjonen bruker attributtnavnet «journalår» (med å) flere
steder:

 * 7.2.1 (Arkivstruktur) UML-entitet for «journalpost» side, 54.
 * 7.2.3 (Sakarkiv) UML-entitet for «journalpost» side 197, 198, 202 og 203.
 * 7.2.3.4 (Journalpost) side 214 og 222.

Dette virker å være et av få eksempel på et attributtnavn som
inneholder særnorske tegn.  Vi tror det kan være lurt å begrense seg
til ASCII når det gjelder attributtnavn.  Spesifikasjonen henvises til
M013 journalaar på side 214, som i
[metadatakatalog.xsdl](http://arkivverket.no/arkivverket/content/download/21282/191627/version/1/file/metadatakatalog.xsdl)
er definert uten å:

```
  <xs:simpleType name="journalaar">
    <xs:annotation>
      <xs:documentation>M013</xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:integer"/>
  </xs:simpleType>
```

Attributtnavnet «journalår» er ikke brukt i Noark 5 standarden eller
tilhørende XSD-filer.  Attributtnavnet er heller ikke brukt på
demo-nettstedet når vi ser på
http://n5test.kxml.no/api/sakarkiv/journalpost, slik at det ikke er
noe hjelp der å få når det gjelder riktig attributtnavn.
Attributtnavnet «journalår» er heller ikke omtalt på
http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/, som forøvrig
er helt uten tekst.  Jeg antar derfor at det er feil, og skulle vært
«journalaar».

Hvis attributtnavnet «journalår» er korrekt og ment å avvike fra
navnet til M013, så bør det nevnes eksplisitt i spesifikasjonen på
side 214.

Ønsket endring
--------------

Endre attributtnavnet «journalår» til «journalaar» alle steder
der det brukes i spesifikasjonen:

 * 7.2.1 (Arkivstruktur) UML-entitet for «Sakarkiv::Journalpost» på side 54
 * 7.2.3 (Sakarkiv) UML-entitet Journalpost på side 197, 202 og side 203
 * 7.2.3.4 (Journalpost) under Attributter side 214 og 215 og under Restriksjoner på side 222.
