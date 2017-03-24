Bedre beskivelse av filopplastingsprossesen
===========================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder også 7.2.1.7 side 99.

Det er uklarheter rundt filopplasting og angivelse av metadata til
dokumentobjekt og dokumentbesrkivelse. Man må lese gjennon linjene for
å forstå hvordan dette henger sammen.

Opprettelse av Noark objekter (arkiv osv) er ganske enkel da
avhengigheten mellom entiter angies i HTTP-requesten. Når det gjelder
filopplasting så er det en slags transaksjon som må skje.

Vi har tolket det slik at man først oppretter dokumentobjekt og angir
filnavn, filstørrelse, mimeType. Etter at filen er lastet opp beregner
vi sjekksum og oppdaterer dokumentobjekt med sjekksumverdi og
algoritme.

Det er da en to-trinns prossess for å få en endelig dokumentobjektet i
databasen.

Det er uklarheter rundt hva klienten skal gjøre og hva kjernen skal
gjøre.  Hvem av dem skal angi mimeType, filstørelse, format? Hva skal
skje hvis disse ikke samsvarer?

Når det gjelder sjekksummer så ser vi en interessant bi-effekt. Hvis
klienten angir sin sjekksum i innkommende dokumentobjekt så kan
serveren sjekke dette og hvis det ikke stemmer kan klienten få
tilbakemelding at noe er galt. Det samme kan skje kjernen returnerer
tilhørende dokumentobjekt som svar til en filopplasting.  Da kan
klienten sjekke at filen som er lagret er det samme som den som ble
lastet opp.

Ønsket endring
--------------

FIXME formuler konkret forslag til endring i spesifikasjonsteksten.

Det må komme en bedre beskrivelse av prossesen med opplasting av filer og
angivelse av metadata verdier.

Ideer til endringsforslag:

 - dokumentobjekt opprettes av klient med verdier i sjekksum og
   sjekksumAlgoritme.  Når filen så lastes opp kontrolleres
   sjekksumverdien mot den opplastede filen i det opplastingen er
   ferdig (dvs. 200 OK returneres for direkteopplasting eller 201
   Created returneres for bolkopplasting).  Hvis sjekksum ikke stemmer
   returneres en feilmelding og filopplastingen avvises.
   
 - når filen er opprettet returneres verdien av tilhørende
   dokumentobjekt som respons på site POST / PUT.
