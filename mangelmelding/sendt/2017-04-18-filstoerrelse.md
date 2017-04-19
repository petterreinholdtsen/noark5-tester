Klargjør om attributtnavn «filstørrelse» er korrekt og relatert feil på demosiden
=================================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.1
         Sidenummer  29
        Linjenummer  n/a
    Innsendingsdato  2017-04-18
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder også side 50, 52, 54, 105 og 203.

Spesifikasjonen bruker attributtnavnet «filstørrelse» (med ø) flere
steder:

 * 7.1 (Om UML og notasjon som er benyttet) UML-skjema for «foto» side 29
 * 7.2.1 (Arkivstruktur) UML-skjema for «dokumentobjekt» side 50, 52, 54
 * 7.2.1.7 (Dokumentobjekt) side 105
 * 7.2.3 (Sakarkiv) UML-skjema for «dokumentobjekt» side 203

Dette virker å være eneste eksempel på et attributtnavn som inneholder
særnorske tegn.  Det henvises til M707 på side 105 og 106, men når en
slår opp M707 i
[metadatakatalog.xsdl](http://arkivverket.no/arkivverket/content/download/21282/191627/version/1/file/metadatakatalog.xsdl)
er M707 definert uten ø:

```
  <xs:simpleType name="filstoerrelse">
    <xs:annotation>
      <xs:documentation>M707</xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:string"/>
  </xs:simpleType>
```

I tillegg bør det nevnes at eksempelet på side 29 omtaler datatypen
«foto» som skal inneholde atributten «filstørrelse».  Datatypen «foto»
er ikk nevnt andre steder i spesifikasjonen.  Skulle
tjenestegrensesnitt-definisjonen hatt foto definert?  Kanskje
eksemplet på side 29 bør endres til å kun bruke datatyper som er
definert i spesifikasjonen?

Attributtet «filstørrelse» er ikke brukt i Noark 5 standarden eller
tilhørende XSD-filer.  Attributten er heller ikke brukt på
demonettstedet, f.eks. på
http://n5test.kxml.no/api/arkivstruktur/dokumentobjekt, slik at det
ikke er noe hjelp der å få når det gjelder riktig attributtnavn.

Attributtet «filstørrelse» er heller ikke omtalt på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/, som
forøvrig ser ut til å vise frem feil datastruktur (mappe) i stedet for
dokumentobjekt.

Ønsket endring
--------------

Endre attributtnavnet «filstørrese» til «filstoerrelse» alle steder
der det brukes i spesifikasjonen:

 * 7.1 (Om UML og notasjon som er benyttet) UML-skjema for «foto» side 29
 * 7.2.1 (Arkivstruktur) UML-skjema for «dokumentobjekt» side 50, 52, 54
 * 7.2.1.7 (Dokumentobjekt) side 105
 * 7.2.3 (Sakarkiv) UML-skjema for «dokumentobjekt» side 203

Når det gjelder problemet med UML-eksemplet på side 29, ser vi to
måter å løse dette på.  Enten (1) Forklar at klassediagramet har
ingenting med NOARK å gjøre:

> Legg til setning på side 29, etter «For kompliserte modeller (som
> NOARK-modellen) trengs flere klassediagram for å vise hele
> modellen.» som forklarer at eksemplet ikke har noe med NOARK å
> gjøre:

> > «Merk, UML-eksemplet til venstre inneholder klasser som ikke
> > finnes i NOARK-modellen.»

eller (2), bruk kun  gyldig NOARK-data i eksemplet:

> Diagramet på side 29 erstates av et nytt diagram som inneholder
> NOARK-klasser.  Dette er foretrukket endring.

Legg inn attributt med størrelse på opplastet fil på
http://n5test.kxml.no/api/arkivstruktur/dokumentobjekt .

Når det gjelder feil på demo-siden foreslår vi å endre
http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/ slik at
den viser datastruktur for dokumentobjekt og ikke mappe.

Respons
-------

Ingen respons fra Arkivverket så langt.
