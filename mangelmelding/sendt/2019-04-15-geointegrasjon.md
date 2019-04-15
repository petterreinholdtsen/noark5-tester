Fullfør beskrivelsen av Nasjonalidentifikator (GeoIntegrasjon)
==============================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.22 (NasjonaleIdentifikatorer)
         Sidenummer  157
        Linjenummer  n/a
    Innsendingsdato  2019-04-15
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det bør beskrives nærmere hvordan API-et kan tilby de samme
operasjonene og lagringsmuligheten som GeoIntegrasjon tilbyr via sitt
SOAP-grensesnitt.  Egen pakke for GeoIntegrasjon er beskrevet i tekst
og UML-diagramer, men ikke fullt ut integrert i spesifikasjonen.  Mer
informasjon om GeoIntegrasjon er tilgjengelig fra
https://www.geointegrasjon.no.  Det er antagelig bedre å velge en
enklere tilnæring som passer til REST, i stedet for å forsøke å
gjenbruke GeoIntegrasjon-strukturen direkte.

Samme type ekstra identifiserende informasjon som tilbys i
GeoIntegrasjon er med i spesifikasjonens kapittel 7 under
overskriften/pakkenavnet "NasjonaleIdentifikatorer", men det mangler
beskrivelse av datatypene ByggIdent, Matrikkelnummer,
NasjonalArealplanId og Punkt.  Hvorfor er det lagt opp til for lagdelt
entitet og datatype, når det holder med en "flat" entitet?

F.eks. Matrikkel ser ut til å være lagt opp til noe slikt:

```
{
  "matrikkelnummer" : {
      "kommunenummer"  : "0101",
      "gaardsnummer"   : 1,
      "bruksnummer"    : 1,
      "festenummer"    : 1,
      "seksjonsnummer" : 1
   },
   "_links": ...
}
```

Det kan jo gjøres enklere ved å "pakke ut" matrikkelnummer slik:

```
{
   "kommunenummer"  : "0101",
   "gaardsnummer"   : 1,
   "bruksnummer"    : 1,
   "festenummer"    : 1,
   "seksjonsnummer" : 1,
   "_links": ...
}
```

Tilsvarende kan Posisjon "pakkes ut" slik at en instans for posisjonen
til Oslo i UTM32N ser slik ut.


```
{
   "x": 596933,
   "y": 6642781,
   "z": 100,
   "koordinatsystem": "EPSG:32632"
   "_links": ...
}
```

Merk at 'z' her er et valgfritt felt for høyde.  Jeg har ikke funnet
beskrivelse av Koordinat-typen til GeoIntegrasjon, så jeg vet ikke om
den kun inneholder x og y.

Tilsvarende utpakking kan gjøres for de andre datatypene.  Er det en
grunn til å lage datatyper i stedet for å pakke dem ut?  Vil de bli
gjenbrukt separat, eller alltid via NasjonalIdentifikator?  For
posisjon vil det trengs informasjon om koordinatsystem, og
koordinatsystem vil trenge en kodeliste over kjente koordinatsystemer.
GeoIntegrasjon bruker navn fra SOSI på koordinatsystemer.  Jeg tror
det er bedre å basere seg på navn fra en mer internasjonal standard
som GML, som ser ut til å bruke navn definert av
[EPSG](http://www.epsg.org/).

GeoIntegrasjon ser i tillegg ut til å ha endel flere eksterne
referanser enn dagens API-spesifikasjon legger opp til, kalt
Kjerne::EksternNøkkel.  Har noen sjekket om
virksomhetsspesifikkeMetadata kan brukes til å ta vare på og avlevere
disse?  Hvordan kan de legges inn i og søkes etter via denne
spesifikasjonen?

Dagens definisjon av Nasjonalidentifikator innholder attributten
"beskrivelse".  Det er uklart hva dette feltet skal inneholde, og jeg
finner ikke tilsvarende felt i GeoIntegrasjon.  Kanskje det bør
droppes?

Definisjonen av Personidentifikator virker uheldig, der en kan ende
opp med en identifikator uten innhold hvis hverken foedselsnummer
eller dNummer er satt.  Hva er tanken her?  Det virker mer naturlig å
dele entiteten i to, en for foedselsnummer og en annen for dNummer.

Det står ingenting om hvordan entitetene som arver fra
NasjonalIdentifikator skal avleveres, og verdiene har så vidt jeg kan
se ikke en plass i arkivstruktur.xml til Noark 5 versjon 4 og 5.  For
Mappe kan det lagres i virksomhetsspesifikkeMetadata, mens den finnes
ikke i Registrering, men derimot i Basisregistrering.  Kan løsningen
her være å slå sammen Registrering og Baisisregistrering i API-et, og
definere virksomhetsspesifikke felter som skal brukes ved avlevering?


Ønsket endring
--------------

Fullfør dokumentdel 7.2.1.22 (NasjonaleIdentifikatorer) slik at det er
klart og entydig hvordan slike ID-er skal registreres, hentes frem og
søkes i.

Ta i bruk Enhetsidentifikator or Personidentifikator i Sakspart og
Korrespondansepart.

Jeg har laget et utkast som jeg skal sende inn som endringsforslag.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/141 .
