Dokumentere prosess for å melde feil og uklarheter i spesifikasjonen
====================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  2
         Sidenummer  8
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Det savnes en beskrivelse hvordan forslag til endringer i
spesifikasjonen bør struktureres og formateres, og hvordan slike
endringsforslag skal håndteres.  Det samme gjelder for forespørsler og
spørsmål om spesifikasjonen.  Spesifikasjonen er vag eller
selvmotsigende på flere områder, hvilket gjør det utfordrendre å vite
om en har forstått spesifikasjonen korrekt.  I slike tilfeller hadde
det vært veldig nyttig med svar som kunne avklare hva som er forventet
oppførsel i grensesnittet.  Hvis det skal være mulig å koble en
grensesnittklient til en hvilken som helst grensesnittimplementasjon,
så må spesifikasjonen være krystallklar og alle implementasjonen følge
spesifikasjonen på samme måte.

Det er uklart hva som er kontaktpunkt for å stille spørsmål om teksten
i spesifikasjonen eller for å melde om uklarheter og feil i
spesifikasjonen.

I følge
https://samdok.com/2016/09/20/noark5-tjenestegrensesnitt-v-1-0-beta-er-na-tilgjengelig/
skal innspill inntil videre sendes til samdok@arkivverket.no, men når
en gjør dette får en beskjed om at ansvaret er sendt videre.

Det hadde også vært svært nyttig hvis det eksisterte en prosess som
publiserte oppdaterert spesifikasjon etter hvert som det blir
korrigert slike svakheter, og som publiserte tidligere spørsmål og
svar slik at enhver kan få med seg disse.  Dvs. en offentlig
tilgjengelig liste med spørsmål og korreksjoner til NOARK5-relaterte
spesifikasjoner.

Et eksempel på en slik prosess finnes hos The Austin Group, som
vedlikeholder POSIX-standarden.  Der skal alle mangelmeldinger
(«defect reports») følge et fast format (se
http://www.opengroup.org/austin/mantis.html) og både meldinger og
respons fra ekspertgruppen gjøres tilgjengelig på Internett slik at
alle kan se hva som er kommet av innspill så langt, samt kommentere på
innspill som er kommet.

Litt utdaterte eksempler på slike henvendelser finnes samlet under
http://www.opengroup.org/austin/aardvark/latest/xshbug2.txt, fra den
gangen jeg sendte inn slike henvendelser til endringer i
POSIX-standarden.

Kan dere få på plass en lignende prosess for NOARK5-spesifikasjonen?

Ønsket endring
--------------

Lag en nettside som forklarer hvordan mangelmeldinger bør skrives og
hvor de bør sendes inn, og vedlikehold en liste lenket til fra denne
nettsiden med alle slike mangelmeldinger og responsen de har fått.

Basert på formatet til The Austin Group foreslår jeg at alle
mangelmeldinger inneholder følgende deler:

 1. Oppsummering / overskrift
 1. Prosjekt
 1. Kategori
 1. Alvorlighet
 1. Meldingstype
 1. Brukerreferanse
 1. Dokumentdel
 1. Sidenummer
 1. Linjenummer
 1. Innsendingsdato
 1. Beskrivelse
 1. Ønsket endring
 1. Respons

Delene fra og med Oppsummering til og med innsendingsdato er korte
nøkkelopplysninger om henvendelsen.  Beskrivelse er fritekstfelt som
forklarer hva henvendelsen gjelder, og Ønsket endring er et konkret og
spesifikk forslag til hvordan spesifikasjonsteksten bør endres for å
løse utfordringen som forklares i beskrivelsen.

Det legges inn lenketil den omtalte nettsiden i nytt avsnitt under
punkt 2 (Normative Referanser) med følgende tekst:

> Spørsmål, innspill til videre utvikling og/eller feilretting bør
> følge retninglinjene dokumentert på https://url.til/nettside/ og
> sendes inn i henhold til instruksene der.  Tidligere henvendelser og
> svar er tilgjengelig fra denne nettsiden.

Respons
-------

Ingen respons fra arkivverket så langt.
