Slå sammen basisregistrering og registrering til kombinert registrering?
========================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

For å forberede overgang til versjon 5, der basisregistrering og
registrering er slått sammen til en entitet med navn registrering, så
bør en se på om det er mulig å gjøre det samme i
tjenestegrensesnittet, for å slippe å måtte gjøre denne endringen
senere.  Vil det skape problemer ved eksport for deponering?

I arkivstruktur.xsd fra
https://github.com/arkivverket/schemas/tree/avlevering-wip/N5/v5.0 ser
en følgende nye definisjon av registrering:


```
<xs:complexType name="registrering">
  <xs:sequence>
    <xs:element name="systemID" type="n5mdk:systemID"/>
    <xs:element name="opprettetDato" type="n5mdk:opprettetDato"/>
    <xs:element name="opprettetAv" type="n5mdk:opprettetAv"/>
    <xs:element name="arkivertDato" type="n5mdk:arkivertDato"/>
    <xs:element name="arkivertAv" type="n5mdk:arkivertAv"/>
    <xs:element name="referanseArkivdel" type="n5mdk:referanseArkivdel" minOccurs="0" maxOccurs="unbounded"/>

    <xs:element name="part" type="part" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="kassasjon" type="kassasjon" minOccurs="0"/>
    <xs:element name="skjerming" type="skjerming" minOccurs="0"/>
    <xs:element name="gradering" type="gradering" minOccurs="0"/>

    <!-- Tillater registreringer uten forekomster av dokumentbeskrivelse og dokumentobjekt -->
    <xs:choice>
      <xs:element name="dokumentbeskrivelse" type="dokumentbeskrivelse" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="dokumentobjekt" type="dokumentobjekt" minOccurs="0" maxOccurs="unbounded"/>
    </xs:choice>

    <xs:element name="registreringsID" type="n5mdk:registreringsID" minOccurs="0"/>
    <xs:element name="tittel" type="n5mdk:tittel"/>
    <xs:element name="offentligTittel" type="n5mdk:offentligTittel" minOccurs="0"/>
    <xs:element name="beskrivelse" type="n5mdk:beskrivelse" minOccurs="0"/>
    <xs:element name="noekkelord" type="n5mdk:noekkelord" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="forfatter" type="n5mdk:forfatter" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="dokumentmedium" type="n5mdk:dokumentmedium" minOccurs="0"/>
    <xs:element name="oppbevaringssted" type="n5mdk:oppbevaringssted" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="virksomhetsspesifikkeMetadata" type="xs:anyType" minOccurs="0"/>

    <xs:element name="merknad" type="merknad" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="kryssreferanse" type="kryssreferanse" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="korrespondansepart" type="korrespondansepart" maxOccurs="unbounded"/>

  </xs:sequence>
</xs:complexType>
```

Det eneste påkrevde feltet som er lagt til 'registrering' er 'tittel'.
Det betyr at en slik endring gjør at en ikke lenger vil være i stand
til å importere data som er strukturert i henhold til
avleveringsformatet beskrevet i XML-skjema for versjon 4 uten å måtte
finne på en tittel for alle instanser av 'registrering'.

Det er ikke noe problem for eksport, da en vil kunne eksportere alle
instanser av en slik kombinert 'registrering' som 'basisregistrering'
hvis en eksporterer som versjon 4.

Ønsket endring
--------------

FIXME finn ut hva som kan gjøres
