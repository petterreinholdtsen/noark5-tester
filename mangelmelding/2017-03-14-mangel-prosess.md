Prosessen for å melde feil og uklarheter i beskrivelse av NOARK 5 Tjenestegresesnitt bør klargjøres
===================================================================================================

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

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra https://github.com/petterreinholdtsen/noark5-tester/ .

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

 1. `Oppsummering / overskrift` - Enlinjers kort oppsummering av
    mangelmeldingen.
 1. `Prosjekt` - Kort navn på spesifikasjon/prosjektet meldingen
    omhandler, f.eks. 'NOARK 5 Tjenestegresesnitt'.
 1. `Kategori` - Hvilken del / utgave av prosjektet meldingen gjelder.
    Her kan en legge inn versjon for spesifikasjonen som diskuteres,
    f.eks. 'Versjon 1.0 beta'.
 1. `Alvorlighet` - Enten 'kommentar' eller 'protest', der 'protest'
    betyr at spesifikasjonen ikke bør godkjennes før mangelen er
    utbedret, mens 'kommentar' er et innspill for å gjøre
    spesifikasjonen bedre.
 1. `Meldingstype` - Enten 'utelatt' eller 'trenger klargjøring'. ` Bruk
    'utelatt' hvis spesifikasjonen mangler noe som burde vært omtalt,
    og 'trenger klargjøring' hvis eksisterende tekst ikke er klar og
    entydig nok.
 1. `Brukerreferanse` - Navn, epostadresse eller annen måte for
    innsender å kjenne igjen sine meldinger.
 1. `Dokumentdel` - Hvilken del av spesifikasjonen meldingen gjelder.
 1. `Sidenummer` - Hvilken side i spesifikasjonen meldingen gjelder.
 1. `Linjenummer` - Hvilken linje på siden meldingen gjelder.
 1. `Innsendingsdato` - Når meldingen ble sendt inn til arkivverket,
    eller 'ikke sendt inn' hvis den ennå ikke er sendt inn.
 1. `Beskrivelse` - En presis beskrivelse av problemet som forklarer
    hvorfor det er et problem.  Husk å ta med tilstrekkelig forklaring
    til at noen som er kjent med temaet kan ta en avgjørelse.
 1. `Ønsket endring` - Konkrete og spesifikke forslag til endringer i
    spesifikasjonen, inkludert formuleringer, slik at de som vurderer
    meldingen vet hva du mener vil løse problemet.
 1. `Respons` - Tilbakemeldingen som er kommet fra arkivverket, hvis det
    er kommet respons.  Droppes hvis ingen respons er kommet

Delene fra og med Oppsummering til og med innsendingsdato er korte
nøkkelopplysninger om henvendelsen.  Beskrivelse er fritekstfelt som
forklarer hva henvendelsen gjelder, og Ønsket endring er et konkret og
spesifikk forslag til hvordan spesifikasjonsteksten bør endres for å
løse utfordringen som forklares i beskrivelsen.  Se forøvrig
feltbeskrivelsene fra The Austin Group.

Felt som ikke er aktuelle eller relevant gis verdien 'n/a'.

Det legges inn lenketil den omtalte nettsiden i nytt avsnitt under
punkt 2 (Normative Referanser) med følgende tekst:

> Spørsmål, innspill til videre utvikling og/eller feilretting bør
> følge retninglinjene dokumentert på https://url.til/nettside/ og
> sendes inn i henhold til instruksene der.  Tidligere henvendelser og
> svar er tilgjengelig fra denne nettsiden.
