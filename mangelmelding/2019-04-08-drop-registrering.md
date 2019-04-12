Slå sammen «basisregistrering» og «registrering» til kombinert «registrering»?
==============================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger avklaring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.5 (Basisregistrering)
         Sidenummer  82
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Gjelder også del 7.2.1.18 (Registrering) side 145.

For å forberede overgang til Noark 5 versjon 5, der typene
«basisregistrering» og «registrering» er slått sammen til en entitet
med navn «registrering», så bør en se på om det er mulig å gjøre det
samme i tjenestegrensesnittet, for å slippe å måtte gjøre denne
endringen senere.  Vil det skape problemer ved import eller eksport
for deponering i tråd med XML-skjema for Noark 5 versjon 4?

I arkivstruktur.xsd fra
https://github.com/arkivverket/schemas/tree/avlevering-wip/N5/v5.0 ser
en følgende nye definisjon av registrering:


```XML
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

Listen er i sum unionen av feltene som er i Noark 5 versjon 4 for
«registrering» og «basisregistrering».

Det eneste påkrevde feltet som er lagt til den nye «registrering» er
«tittel».  Det betyr at en slik endring gjør at en ikke lenger vil
være i stand til å importere data som er strukturert i henhold til
avleveringsformatet beskrevet i XML-skjema for versjon 4 uten å måtte
finne på en tittel for alle instanser av «registrering».  En løsning
på dette er å spesifisere en tittelstreng som skal settes ved import
på alle «registrering»-instanser.  Den kan for eksempel være «n/a»,
«[blank]», «[mangler]», «[registrering]», «[importert registrering]»
eller noe annet som brukere av API-et vil gjenkjenne som importert
registrering uten tittel.

Det er ikke noe problem for eksport, da en vil kunne eksportere alle
instanser av en slik kombinert «registrering» som «basisregistrering»
hvis en eksporterer som versjon 4.

Ønsket endring
--------------

Slå sammen entitetene Registring og Basisregistrering i kapittel 7
under navnet Registrering, beskriv der at Noark 5 versjon 4-entietene
disse er slått sammen for å være fremoverkompatibel med versjon 5, og
skriv hvilken tittel som skal settes ved import av
Registrering-instanser.  Foreslår «[importert registrering]» som slik
tittel.

Beskrivelse, relasjoner, relasjonsnøkler, attributter og restriksjoner
må slås sammen til en samlet oversikt.

FIXME finn ut hvor og hvordan det skal inni teksten
