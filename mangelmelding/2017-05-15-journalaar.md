Klargjør om attributtnavn «journalår» er korrekt
================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.4
         Sidenummer  214
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder også 54, 197, 198, 202, 203, 214, 222


Spesifikasjonen bruker attributtnavnet «journalår» (med å) flere
steder:

 * 7.2.1 (Arkivstruktur) UML-skjema for «journalpost» side, 54.
 * 7.2.3 (Sakarkiv) UML-skjema for «journalpost» side 197, 198 202 og 203.
 * 7.2.3.4 (Journalpost) side 214 og 222.

Dette virker å være et av få eksempel på et attributtnavn som inneholder
særnorske tegn.  Det henvises til M013 journalaar på side 214, som ganske riktig
i
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

Attributtet «journalår» er ikke brukt i Noark 5 standarden eller
tilhørende XSD-filer.  Attributten er heller ikke brukt på
demonettstedet, f.eks. på
http://n5test.kxml.no/api/arkivstruktur/journalpost, slik at det
ikke er noe hjelp der å få når det gjelder riktig attributtnavn.

Attributtet «filstørrelse» er heller ikke omtalt på
http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/, som
forøvrig her helt tom.

Ønsket endring
--------------

FIXME formuler ønsket endring.  Se sendt/2017-04-18-filtstoerrelse for
relatert mangelmelding.
