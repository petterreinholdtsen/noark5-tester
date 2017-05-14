Hvordan håndterer EnkeltAdresse utenlandske adresser?
=====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  199
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge klasseoversikten på side 199 har datatypen EnkeltAdresse
feltet postnr av typen Postnummer og landkode av typen Land.

Men Postnummer-typen er basert på kodelisten Postnummer, som skal
fylles med informasjon fra posten.no.  Det vil dermed mangle
utenlandske postnummer i den kodelisten.

Tilsvarende står i del 7.2.3.3 (EnkeltAdresse) på side 212, med
referanse til metadatalistene
http://rel.kxml.no/noark5/v4/api/metadata/land/ og
http://rel.kxml.no/noark5/v4/api/metadata/postnummer/.

Det er ikke omtalt i spesifikasjonen hva Postnummer-kodelisten skal
inneholde, hverken på klasseoversikten på side 165 og side 199 eller i
del 7.2.2.25 (Postnummer) på side 185.

Det er heller ikke omtalt i spesifikasjonen hva Land-kodelisten skal
inneholde, hverken på klasseoversikten på side 165 og side 199 eller i
del 7.2.2.18 (Land) på side 179.

En kan laste ned lister med norske postnummer fra
http://www.bring.no/radgivning/sende-noe/adressetjenester/postnummer.
Listene som er tilgjengelig uten bruksbetaling inneholder postnummer,
poststed, kommunekode (fylke 2 + kommune 2), kommunenavn og kategori.

Geoposisjon kan fås fra
http://www.erikbolstad.no/geo/noreg/postnummer/ eller kjøpes fra
Posten.

På side 212 er poststed definert som [1..1] så det er obligatorisk.
Det finnes mange land i verden som ikke har postnummer og å tvinge
et postnummer vil føre til "søppel" som blir introdusert i kjernen
for dette feltet. Problemet kan delvis løses ved at poststed blir [0..1], 
valgfri. Men det bør også vurderes om å lage en UtenlandsAdresse entitet
som er litt mer fleksibel. 

Ønsket endring
--------------

FIXME mer konkret beskrivelse

Forklar hvordan utenlandske adresser med ikke-norske postnummer skal
lagres i databasen.

Forklar hvilke felter som skal være i postnummer-kodelisten.  I
tillegg til nummer og sted, hva med land, kommune og geografisk
plassering?

Forklar hvilke felter som skal være i land-kodelisten.

Adressen til postens postnummerliste på side 185 bør endres til
http://www.bring.no/radgivning/sende-noe/adressetjenester/postnummer .
