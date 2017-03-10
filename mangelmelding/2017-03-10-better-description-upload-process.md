Bedre beskivelse av filopplastings prossesen
==============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  2017-03-10
 ------------------  ---------------------------------

Beskrivelse
-----------

Det er uklarheter rundt filopplasting og angivelse av metadata til 
dokumentobjekt og dokumentbesrkivelse. Man må lese gjennon linjene
for å forstå hvordan dette henger sammen. 

Opprettelse av Noark objekter (arkiv osv) er ganske enkel da avhengigheten 
mellom entiter angies i HTTP-requesten. Når det gjelder filopplasting så er 
det en slags transaksjon som må skje.

Vi har tolket det slik at man først oppretter dokumentobjekt og angir 
filnavn, filstørrelse, mimeType. Etter at filen er lastet opp beregner vi
sjekksum og oppdaterer dokumentobjekt med sjekksumverdi og algoritme.

Det er da en to-trinns prossess for å få en endelig dokumentobjektet i 
databasen. 

Det er uklarheter rundt hva klienten skal gjøre og hva kjernen skal gjøre. 
Hvem av de skal angi mimeType, filstørelse, format? Hva skal skje hvis disse
ikke samsvarer?

Når det gjelder sjekksummer så ser vi en interessant bi-effekt. Hvis klienten
angir sin sjekksum i innkommende dokumentobjekt så kan serveren sjekke dette og
 hvis det ikke stemmer kan klienten få tilbakemelding at noe er galt. Det samme
 kan skje kjernen returnerer et dokumentobjekt som svar til en filopplasting.
 Da kan klienten sjekke at filen so er lagret er det samme som den som ble 
 lastet opp. 


Ønsket endring
--------------

Det må komme en bedre beskrivelse av prossesen med opplasting av filer og
angivelse av metadata verdier.

Respons
-------

Ingen respons fra arkivverket så langt.
