Klargjør formatet på dokumentobjekt.filstoerrelse  (M707)
=========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.2.1.7 (Dokumentobjekt)
         Sidenummer  105
        Linjenummer  n/a
    Innsendingsdato  2019-02-11 (github issue #69)
 ------------------  ---------------------------------

Beskrivelse
-----------

Dette er relatert til [tilsvarende mangelmelding om
metadatakatalogen](https://github.com/petterreinholdtsen/noark5-tester/blob/master/mangelmelding/sendt/2017-05-26-m707-filstoerrelse.md)
i Noark 5 (både versjon 4 og 5) sendt til Arkivverkets postmottak
2017-05-26.

Definisjonen på filstørrelse-feltet (M707) i Dokumentobjekt-klassen er
tvetydig og ikke optimalt.  For det første er det en numerisk verdi
som skal lagres som string, og for det andre er det uklart hva
stringen skal inneholde.  Definisjonen som brukes åpner for at
størrelsen skal være et desimaltall (dvs. «tall som er satt sammen av
en heltallsdel og en fraksjonsdel. Disse to delene er skilt med et
desimalskilletegn. Et eksempel kan være tallet «49,90» der
heltallsdelen er «49» og fraksjondelen er «90».» i følge norsk
Wikipedia).  Dette gjør det vanskeligere enn nødvendig for
API-klienter å tolke verdien.  Det er enklere for API-klienter om
verdien er definiert til å være et positivt heltall (det gir vel ikke
mening å arkivere tomme filer?).

Det vil være enklere for alle, både API-klienter og andre
implementasjoner, hvis dette feltet har en klar og entydig betydning,
og alltid er et heltall større eller lik null som oppgir filstørrelsen
i bytes.

Dette bør ha en konsekvens på hvordan filstoerrelse er definert i
metadatakatalog.xsdl.  Følgende forslag kan definere filstoerrelse
som heltall større eller lik 0.

```
<xs:simpleType name="filstoerrelse">
  <xs:annotation>
    <xs:documentation>M707</xs:documentation>
  </xs:annotation>
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-9]+"/>    
  </xs:restriction>
</xs:simpleType>
```

Dette vil også gjøre det klart at kun ikke-negative heltall aksepteres
i dette feltet.

En annen ide er å bytte type fra xs:string til en numerisk type.
Dette bør i så fall gjøres på en måte som ikke begrenser mulige
filstørrelser.  Feltet «filstørrelse» er brukt på sidene 29, 50, 52,
54, 105 og 203 i spesifikasjonen for Noark 5 Tjenestegrensesnitt.
Hvis typen skal endres i metadatakatalog.xsdl så må det endres også
her.

Ønsket endring
--------------

Endre oppføringen for M707 på side 61 i vedlegg 1 (Metadatakatalog)
til Noark 5 versjon 4.0, bytte ut

> Størrelsen på fila i antall bytes oppgitt med desimaltall

til

> Størrelsen på fila som en tekststreng med antall bytes i oppgitt som
> et ikke-negativt heltall i titallsystemet, f.eks. "123456890".

Endre beskrivelsen av M707 i metadatakatalog.xsdl, bytt ut

> ```
> <xs:restriction base="xs:string"/>
> ```

med

> ```
> <xs:restriction base="xs:string">
>   <xs:pattern value="[0-9]+"/>
> </xs:restriction>
> ```

Endre feltbeskrivelsen i del 7.2.1.7 (Dokumentobjekt) på side 105 i
spesifikasjonen for Noark 5 tjenestegrensenitt 1.0 beta fra

> Definisjon: Størrelsen på fila i antall bytes oppgitt med
> desimaltall

til

> Definisjon: Størrelsen på fila som en tekststreng med antall bytes i
> oppgitt som et ikke-negativt heltall i titallsystemet,
> f.eks. "123456890".

Respons
-------

Rapportert til
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/69 .

Arkivverket melder at felttype skal endres til 'integer' og bli et
positivt heltall.
