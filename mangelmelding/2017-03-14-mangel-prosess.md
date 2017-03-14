Dokumentere prosess for å melde feil og uklarheter i spesifikasjonen
====================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Det er uklart hva som er kontaktpunkt for å stille spørsmål om teksten
i spesifikasjonen eller for å melde om uklarheter og feil i
spesifikasjonen.


FIXME rydd opp i teksten


Hei.  Jeg leser for tiden spesifikasjonen tilgjengelig via
<URL:
https://samdok.com/2016/09/20/noark5-tjenestegrensesnitt-v-1-0-beta-er-na-tilgjengelig/
>,
som del av et prosjekt for å implementere API-et med fri programvare, og
lurer på hvor jeg burde sende spørsmål jeg sitter med i den
forbindelse.  Er dette en god epostadresse å bruke?  Jeg har mange
spørsmål, men venter med å stille dem til jeg har funnet en god kanal å
formidle dem.

Et eksempel er at jeg har sett at spesifikasjonen oppgir relasjonsnøkler
både med ut uten avsluttende skråstrek.  Tabellene har med skråstrek,
mens det i teksten finnes noen få eksempler der de er oppgitt uten
skråstrek (se side 12-13 og 25-26).  Skal det være
<URL: http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/ > eller
<URL: http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil > eller er det
meningen at begge skal brukes om hverandre?

Jeg tror det er lurt om spesifikasjonen kun bruker en av disse, for å
gjøre det enklere å implementere klienter til API-et.

  Takk.

  Saken er at jeg skriver på et verktøy for å teste et NOARK 5
  tjenestegresesnitt for å se at det oppfører seg i tråd med
  spesifikasjonen.  Og utfordringen er at spesifikasjonen er vag eller
  selvmotsigende på flere områder, hvilket gjør det utfordrendre å vite om
  jeg har forstått spesifikasjonen korrekt.  I slike tilfeller hadde det
  vært veldig nyttig med svar som kunne avklare hva som er forventet
  oppførsel i grensesnittet.  Det hadde også vært svært nyttig hvis det
  eksisterer en prosess som publiserte oppdaterert spesifikasjon etter
  hvert som det blir korrigert slike svakheter.

  Hvis det skal være mulig å koble en grensesnittklient til en hvilken som
  helst implementasjon, så må spesifikasjonen være krystallklar og alle
  implementasjonen følge spesifikasjonen på samme måte.  Er det gjort noen
  undersøkelser på om det er mulig i dag?

  Som jeg nevnte i min første epost, er dette med bakgrunn i et prosjekt
  for å lage en fri progamvareimplemtnasjon av grensesnittet der Thomas er
  hovedutvikler.  Jeg tester dermed hvorvidt han har programmert riktig,
  og vi bruker spesifikasjonen som fasit.  Sistnevnte blir veldig
  vanskelig når fasiten er uklar.

  Mitt system for å teste tar sakte form på
  <URL: https://github.com/petterreinholdtsen/noark5-tester >, hvis dere
  vil teste selv.

   Finnes det forresten en offentlig tilgjengelig liste med spørsmål og
   korreksjoner til NOARK5-spesifikasjonen?  Jeg tenker på noe ala det The
   Austin Group gjør tilgjengelig for POSIX-standarden, der alle
   forespørsler ('defect reports') er forventet å følge  et forholdsvis
   fast format (se <URL: http://www.opengroup.org/austin/mantis.html >), og
   gjøres tilgjengelig på Internet slik at alle kan se hva som er kommet av
   innspill så langt, samt kommentere på innspill som er kommet.

   Litt utdaterte eksempler på slike henvendelser finnes samlet under
   <URL: http://www.opengroup.org/austin/aardvark/latest/xshbug2.txt >, fra
   den gangen jeg sendte inn slike henvendelser til endringer i
   POSIX-standarden.

   Har dere en lignende prosess på plass for NOARK5-spesifikasjonen?  Hvis
   ikke, kan dere vurdere å ta i bruk en slik prosess?


Ønsket endring
--------------

Definer kontaktpunkt (f.eks. epostadresse eller webskjema) og mal for
hva meldinger bør inneholde.

Respons
-------

Ingen respons fra arkivverket så langt.
