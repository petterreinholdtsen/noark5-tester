Mangler direkte relasjon mellom Dokumentobjekt og Registrering
==============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.7 (Dokumentobjekt)
         Sidenummer  99
        Linjenummer  n/a
    Innsendingsdato  2019-04-09
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også dokumentdel 7.2.1.18 (Registrering) side 146.

I følge arkivstruktur.xsd for Noark 5 versjon 4 så kan en registrering
enten ha «dokumentbeskrivelse» eller «dokumentobjekt» under seg.
Dagens datastruktur i API-et tillater kun dokumenbeskrivelse.  Bør en
også tillate dokumentobjekt direktekoblet til registrering?  I motsatt
fall bør det dokumenteres i spesifikasjonen at det er et bevisst valg
å ikke støtte dette, med forklaring og begrunnelse.

Dette er definisjonen av registrering fra arkivstruktur.xsd:

```XML
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

Under del 7.2.1.18 (Registrering) legges det inn følgende Relasjoner:

| **Relasjon**                        | **Kilde**                              | **Mål**                        | **Merknad** |
| ----------------------------------- | -------------------------------------- | ------------------------------ | ----------- |
| **Aggregation** (Bi-Directional)    | dokumentobjekt 0..* Dokumentobjekt     | registrering 1..* Registrering |             |


Under samme del legges følgende relasjonsnøkler inn:

| **Tag**   | **Verdi**                                                                |
| --------- | ------------------------------------------------------------------------ |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt/           |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-dokumentobjekt/        |


Under del 7.2.1.7 (Dokumentobjekt) legges det inn følgende Relasjoner:

| **Relasjon**                        | **Kilde**                              | **Mål**                        | **Merknad** |
| ----------------------------------- | -------------------------------------- | ------------------------------ | ----------- |
| **Aggregation** (Bi-Directional)    | dokumentobjekt 0..* Dokumentobjekt     | registrering 1..* Registrering |             |


Under samme del legges følgende relasjonsnøkkel inn:

| **Tag**   | **Verdi**                                                              |
| --------- | ---------------------------------------------------------------------- |
| REST\_REL | http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/           |
