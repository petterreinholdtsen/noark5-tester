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
    Innsendingsdato  ikke sendt inn
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

Tilsvarende kan Posisjon "pakkes ut" slik at entiteten ser slik ut,
for å slippe egen Punkt-datatype:


```
{
   "x": 10,
   "y": 69,
   "z": 100,
   "koordinatsystem": KoordinatsystemKode
   "_links": ...
}
```

Tilsvarende kan gjøres for de andre datatypene.  Er det en grunn til å
lage egne datatyper for de fleste av disse?  For posisjon vil det
trengs informasjon om koordinatsystem og koordinat, og spesielt
koordinatsystem vil trenge en kodeliste over kjente koordinatsystemer.
GeoIntegrasjon bruker navn fra SOSI på koordinatsystemer.  Det er
kanskje bedre å basere seg på navn fra en mer internasjonal standard
som GML, som ser ut til å bruke navn definert av
[EPSG](http://www.epsg.org/)?

GeoIntegrasjon ser ut til å ha endel flere eksterne referanser enn
dagens API-spesifikasjon legger opp til, kalt Kjerne::EksternNøkkel.
Har noen sjekket om virksomhetsspesifikkeMetadata kan brukes til å ta
vare på og avlevere disse?  Hvordan kan de legges inn i og søkes etter
via denne spesifikasjonen?

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
