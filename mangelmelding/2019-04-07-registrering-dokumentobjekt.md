Direkte relasjon fra registrering til dokumentobjekt mangler
============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge arkivstruktur.xsd for Noark 5 versjon 4 så kan en registrering
enten ha "dokumentbeskrivelse" eller "dokumentobjekt" under seg.
Dagens datastruktur i API-et tillater kun dokumenbeskrivelse.  Bør en
også tillate dokumentobjekt direktekoblet til registrering?

Dette er definisjonen av registrering fra arkivstruktur.xsd:

```
<xs:complexType name="registrering">
  <xs:sequence>
    <xs:element name="systemID" type="n5mdk:systemID"/>
    <xs:element name="opprettetDato" type="n5mdk:opprettetDato"/>
    <xs:element name="opprettetAv" type="n5mdk:opprettetAv"/>
    <xs:element name="arkivertDato" type="n5mdk:arkivertDato"/>
    <xs:element name="arkivertAv" type="n5mdk:arkivertAv"/>
    <xs:element name="referanseArkivdel" type="n5mdk:referanseArkivdel" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="kassasjon" type="kassasjon" minOccurs="0"/>
    <xs:element name="skjerming" type="skjerming" minOccurs="0"/>
    <xs:element name="gradering" type="gradering" minOccurs="0"/>
    <!-- Tillater registreringer uten forekomster av dokumentbeskrivelse og dokumentobjekt -->
    <xs:choice>
      <xs:element name="dokumentbeskrivelse" type="dokumentbeskrivelse" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="dokumentobjekt" type="dokumentobjekt" minOccurs="0" maxOccurs="unbounded"/>
    </xs:choice>
  </xs:sequence>
</xs:complexType>
```

Ønsket endring
--------------

FIXME
