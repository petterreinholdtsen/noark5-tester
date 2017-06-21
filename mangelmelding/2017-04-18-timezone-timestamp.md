Formattering av dato og tid er i strid med Noark 5-krav for avlevering
======================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.8
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er ikke samsvar mellom formattering av dato med og uten klokkeslett i
tjenestegrensesnittspesifikasjonen og kravene i Noark 5 versjon 4.0.
Noark 5-Kravene 5.12.7 (datoer uten klokkeslett) og 5.12.8 (datoer med
klokkeslett) sier at disse skal representeres ved hjelp av XML Schema
1.0 henholds datatypen date og dateTime, tilgjengelig fra
https://www.w3.org/TR/xmlschema11-2/.  I følge
tjenestegrenesnittspesifikasjonens del 6.1.1.8 side 25 skal
datoformatet angis i henhold til notatet "Date and Time Formats" fra
W3C tilgjengelig fra http://www.w3.org/TR/NOTE-datetime.

Notatet fra W3C sier at alle tidspunkt som inneholder tid på døgnet
skal oppgis med numerisk tidssone i tråd med ISO 8601, men med
firesifret årstall.  Det tillates dermed følgende datetime-verdier:

 * 1997
 * 1997-07
 * 1997-07-16
 * 1997-07-16T19:20+01:00
 * 1997-07-16T19:20:30+01:00
 * 1997-07-16T19:20:30.45+01:00

Det virker nærliggende å anta at verdier som legges inn i en attributt
via tjenestegrensesnittet også må kunne hentes ut av
tjenestegrensesnittet, og i så tilfelle må det være mulig å lagre
enkeltårstall i et date-felt.

Men gir det mening å akseptere kun årstall og årstall/måned i API-et?
I definisjonen av date og dateTime i XML Schema 1.0 date er det krav
om at en dato må inneholde både år, måned og dag, og det er ikke
tillatt å ha kun årstall eller kun årstall og måned.  Dermed vil en
kunne ende opp i en situasjon der arkivdatabasen inneholder dato og
tid som ikke kan avleveres i tråd med kravene i Noark 5.  Det virker
mer fornuftig å be de som legger metadata inn i kjernen å vurdere
hvordan 1997 og 1997-07 skal omformes til en dato på formen
ÅÅÅÅ-MM-DD, enn å finne ut av dette først når arkivet skal deponeres,
og jeg foreslår derfor at definisjonen av lovlige datoverdier i
tjenestegrensesnittet endres til å være i samsvar med kravene i Noark
5.  Alternativt kan jo tjenestegrensesnittet endres til å kreve
formatet beskrevet i date og dateTime-definisjonen i XML Schema 1.0?

En utfordring med denne definisjonen er bruken av
tjenestegrensesnittet i generell saksbehandling, der det vil være
behov for å oppgi fremtidige tidspunkt i lokal tidssone.  Dette kan
ikke uten videre gjøres med numeriske tidssoner i land som Norge der
en har sommer og vintertid.  Der vil jo for eksempel kl. 12:00+0100 en
uke etter dagene før bytte til sommertid bli til 12:00+0200 etter
bytte til sommertid.  Dette bør kanskje nevnes i
tjenestegrensesnittet?

En annen utfordring er hvordan datoer og tidspunkt skal håndteres hvis
samme instans av tjenestegrensesnittet brukes i flere tidssoner.  Et
tenkt eksempel er hvis alle ambassadene i utenrikstjenesten skal
dele arkivløsning og arkivere enten via lokale klienter som snakker
direkte med tjenestegrensesnittet via Internett, klienter tilgjengelig
via fjerntilgang (for eksempel RDP) som kjører sentralt eller
webklient.  Hvis datoer og tidspunkt skal gi mening her må alle datoer
inkludere tidssone, da samme tidspunkt på to forskjellige steder på
jordkloden kan ha forskjellige datoer.  Tilsvarende gjelder for
klokkeslett.

Forøvrig kan det nevnes at tjenestegrensesnittet ikke ser ut til å ha
konsekvent navngiving av datofelter.  Noen består av kun små bokstaver
(merknadsdato, kassasjonsdato, graderingsdato, nedgraderingsdato),
mens andre består av camelCase (slettetDato, presedensDato,
skjermingOpphoererDato).  Det bør vurderes å konsekvent navngiving for
å forenkle livet til de som skal ta i bruk tjenestegrensesnittet.

Ønsket endring
--------------

Endre del 6.1.1.8 side 25 fra "Datoformat skal være angitt ihht
http://www.w3.org/TR/NOTE-datetime" til

> Datoformat skal være angitt ihht http://www.w3.org/TR/NOTE-datetime,
> med det unntak at datoer alltid må inneholde år, måned og dag.
