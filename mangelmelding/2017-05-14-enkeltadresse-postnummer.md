Hvordan skal utenlandske adresser representeres i EnkeltAdresse?
================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.3 (EnkeltAdresse)
         Sidenummer  212
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Se også endringsforslag
[#80](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/pull/80)
og
[#86](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/pull/86).

I følge UML-diagrammen på side 199 og attributtlisten i dokumentdel
7.2.3.3 (EnkeltAdresse) på side 212 har datatypen EnkeltAdresse
attributt postnr av typen Postnummer og landkode av typen Land.  På
side 212 er det oppgitt følgende relasjonsnøkler med referanse til
metadatalistene http://rel.kxml.no/noark5/v4/api/metadata/land/ og
http://rel.kxml.no/noark5/v4/api/metadata/postnummer/.

Hvis jeg forstår det riktig, så skal attributter av type Postnummer ha
verdier fra kodelisten Postnummer, som i følge beskrivelsen skal
fylles med informasjon fra posten.no, antageligvis om norske
postnummer og sted.  Det betyr videre at det vil mangle utenlandske
postnummer i kodelisten.

Det er ikke omtalt i spesifikasjonen hva Postnummer-kodelisten skal
inneholde, hverken på klasseoversikten på side 165 og side 199 eller i
del 7.2.2.25 (Postnummer) på side 185.  Det er heller ikke omtalt i
spesifikasjonen hva Land-kodelisten skal inneholde, hverken på
klasseoversikten på side 165 og side 199 eller i del 7.2.2.18 (Land)
på side 179.  Det er rimelig å anta at kodelistene vil ha samme
struktur som de øvrige kodelistene, dvs. inneholde navn og kode.

En kan laste ned lister med norske postnummer fra
http://www.bring.no/radgivning/sende-noe/adressetjenester/postnummer.
Listene som er tilgjengelig uten bruksbetaling inneholder postnummer,
poststed, kommunekode (fylke 2 + kommune 2), kommunenavn og kategori.
Geoposisjon for postnummer kan fås fra
http://www.erikbolstad.no/geo/noreg/postnummer/ eller kjøpes fra
Posten.

I attributtlisten på side 212 er poststed definert med [1..1] så det
er obligatorisk.  Da norske postnummer kun brukes i Norge, så vil ikke
kodelistens innhold passe for utlandsadresser.  Hvis en skal tvinges
til å bruke verdier fra kodelisten også for utenlandsadresser, så vil
det føre til at "søppel" må legges inn i denne kodelisten for å kunne
representere en utenlandsadresse. Problemet kan delvis løses ved at
poststed blir [0..1], valgfri. Men det bør vurderes om å lage en
UtenlandsAdresse entitet som er litt mer fleksibel, sammen med å bytte
navn på EnkelAdresse til NorskAdresse.

Bring har [litt informasjon om
utenlandsadresser](https://www.bring.no/radgivning/sende-noe/klargjoring/klargjoring-adressert/adressering-til-mottakere-i-utlandet),
som kan være nyttig bakgrunnsinformasjon når en velger hvordan dette
skal gjøres.

Avleveringsformatet beskrevet i arkivstruktur.xsd for Noark 5 versjon
4 har ingen begresninger på innhold i postnummer, der den skal
representeres som en streng.

Ønsket endring
--------------

I dokumentdel 7.2.3.3 (EnkeltAdresse) på side 212, split EnkelAdresse
i to entiteter som arver fra EnkelAdresse, NorskAdresse og
UtenlandsAdresse og gjør EnkelAdresse til en virtuell entitet.  Kun
den første skal være koblet til kodelisten med Postnummer, og den
trenger ikke land, men det kan være greit å ha med land for å skille
ulike adressetyper.  Utvid beskrivelsen av EnkelAdresse til å forklare
når og hvordan NorskAdresse og UtenlandsAdresse skal brukes.

Det kan f.eks. se noe ala dette ut:

```Python
EnkelAdresse:
{
  postadresse string [0..1]
  poststed string [1..1]
  landkode Land [1..1]
}

NorskAdresse:
{
  postnummer Postnummer [1..1]
}

UtenlandsAdresse:
{
  postnummer string [1..1]
}
```

Merk at jeg her har redusert de tre adresselinjene til en linje for å
få en adresse som lar seg avlevere i XML-deponeringsformatet til Noark
5 versjon 4, jamfør [mangelmelding
#80](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/pull/80).

Utvid kodelistebeskrivelsen for Postnummer til å ta med kommunenummer
og geografisk plassering, slik at den blir teoretisk mulig å søke
etter alle adresser i et gitt fylke, en gitt kommune eller innenfor et
gitt geografisk område.

Beskriv hvilke felter som skal være med i kodelisten Land, at
landsnavn skal være i 'navn' og tobokstavs landskode skal være i
'kode, og gjør det klart at en kun setter landkode-verdien i adresser
i utlandet.

I dokumentdel 7.2.2.25 (Postnummer) på side 185 bør Nettadressen til
postens postnummerliste endres til
http://www.bring.no/radgivning/sende-noe/adressetjenester/postnummer .

Jeg sender inn konkret forslag til endring som patch via github.
