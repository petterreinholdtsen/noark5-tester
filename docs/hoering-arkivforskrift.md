Høringsuttalelse om Riksarkivarens forskrift
============================================

Teksten vedlikeholdes på https://titanpad.com/noark5-forskrift

https://www.arkivrad.no/aktuelt/riksarkivarens-forskrift-pa-horing
http://www.arkivverket.no/arkivverket/Offentleg-forvalting/Noark/Noark-5

Frist for innsending er 1. mai 2017

Riksarkivaren
Pb. 4013 Ullevål Stadion
0806 OSLO

Riksarkivarens referanse 2016/9840 HELHJO.

Av Petter Reinholdtsen

Viser til høring sendt ut 2017-02-17, og tillater meg å sende inn noen
innspill om revisjon av Forskrift om utfyllende tekniske og
arkivfaglige bestemmelser om behandling av offentlige arkiver
(Riksarkivarens forskrift).  Innspillene følger samme rekkefølge som
forskriften, så langt det lot seg gjøre.

Forskriftens § 5-12 (Tekstfilformater i arkivuttrekk) punkt b) omtaler
tegnseparert format (kommaseparert format) uten å henvise til en fri
og åpen standard som beskriver dette formatet i detalj. 
Kommaseparerte filer er beskrevet av IETF RFC 4180.  For å sikre en
entydig beskrivelse av formatet foreslår jeg at forskriften henviser
til denne formatbeskrivelsen.  Slik forskriften står i dag mangler
forskriften krav om beskrivelse av hvordan poster som inneholder
feltskilletegn, linjeskift, anførselstegn og så videre skal håndteres,
mens dette er klart beskrevet i RFC 4180,
https://tools.ietf.org/html/rfc4180 .

Klargjøring av godkjente dokumentformat
---------------------------------------

Kommentarer relatert til § 5-16 (Godkjente dokumentformater ved
innlevering), der punkt 1 lister opp godkjente dokumentformat ved
innlevering.

Punkt  § 5-16 1a nevner formatet TXT uten nærmere beskrivelse, uten å
henvise til § 5-11, og uten å forklare hvordan en skal vite hvilket
tegnsett som skal brukes for 'TXT'.  Hvis poenget er at § 5-12 er ment
å beskrive 'TXT'-formatet nærmere bør det legges inn en kryssreferanse
i punkt 1a.  Det er ikke klart fra forskriften hva konkret TXT er
slags format.  Beskrivelsen «ren tekst» kan være så mangt, og både
HTML og XML består jo av en tekstlig beskrivelse.  Er det ment å være
tilsvarende text/plain definert i IETF RFC 2046?  Der beskrives den
som

  «"text/plain", which is a generic subtype for plain text.  Plain
  text does not provide for or allow formatting commands, font
  attribute specifications, processing instructions, interpretation
  directives, or content markup.  Plain text is seen simply as a
  linear sequence of characters, possibly interrupted by line breaks
  or page breaks.  Plain text may allow the stacking of several
  characters in the same position in the text. Plain text in scripts
  like Arabic and Hebrew may also include facilitites that allow the
  arbitrary mixing of text segments with opposite writing
  directions.».

Punkt § 5-16 1a omtaler TIFF som «"ren tekst».  Jeg antar en her
snakker om bilder av papir med tekst.  Men TIFF er bilde av tekst,
ikke ren tekst og det virker misvisende å likestille den med TXT, XML
og PDF/A. Bilder av tekst, uavhengig av om det er pakket inn som TIFF
eller PDF, bør vel heller legges under punkt 1c.

Punkt § 5-16 1f nevner «PCM-basert wave» uten å beskrive nærmere hva
som mener med dette.  Det er dermed uklart hvilken av lydformatene med
wave i navnet det refereres til. Er det Waveform Audio File Format
definert i Multimedia Programming Interface and Data Specification 1.0
av IBM Corporation og Microsoft Corporation i august 1991 det gjelder?
Det beste hadde vært å referere til en klar og offentlig
spesifikasjon, helst en fri og åpen standard, som beskriver formatet.

Punkt § 5-16 1h) nevner HTML, men nevner ikke hvordan eksterne
referanser i HTML (f.eks skrifttyper, JavaScript-kode, bilder eller
video skal håndteres for å kunne gjenskape en web-side.  § 5-19 sier
derimot at formatet ikke skal brukes.  Kanskje HTML ikke burde være på
listen over godkjente dokumentformater?

Legge inn Internett-e-post (IETF RFC 5322) som godkjent dokumentformat
----------------------------------------------------------------------

Forskriftens oversikt over godkjente dokumentformater ved innlevering
i § 5-16 bør inneholde Internett-e-post.  Jeg foreslår at det legges
inn et nytt punkt k) under punktet om websider, som for eksempel kan
lyde::

  k) For Internett-e-post aksepterer følgende:
    - RFC822 som spesifisert i IETF RFC 5322.  Eventuelle vedlegg
      lagres i tillegg som separate vedleggsdokumenter i aksepterte
      dokumentformater der dette er mulig.

Jeg foreslår å bruke 'RFC822' som formatnavn for slik e-post, da RFC
822 er opprinnelig beskrivelse av Internett-e-post, siden etterfulgt av
RFC 2822 og RFC 5322, https://tools.ietf.org/html/rfc5322, med
oppdatert beskrivelse.

E-post er beskrevet i Noark 5 versjon 3.1 på sidene 193 til 207. I
beskrivelsen av krav 8.1.8 (side 197) står det at e-post skal lagres i
et enhetlig, samlet format som gjengir både e-posthode og
e-postmelding, men forklarer ikke hvordan det skal gjøres. Side 193
dokumenterer det som for meg ser ut som en misforståelse:

  "Selv om RFC2822 definerer syntaksen for e-posttransaksjoner, er den
  ingen standard som definerer dataformatet som skal bli brukt når
  e-posttransaksjonen er fanget som dokumenter."

En kan jo "fange en e-post som et dokument" for lagring ved å ta vare
på teksten som utgjør e-posten, dvs. hode og kropp.  Det er standard
måte å ta vare på e-post, f.eks. i mbox, maildir, mh og en rekke andre
kjente måter å ta vare på e-post, og håndteres av ethvert
e-postprogram.  En e-post lagres tradisjonelt ved å lagre tekstlinjene
som utgjør e-posten.  Formatet er enkelt, der e-postens hode består av
tekstlinjer med feltnavn, kolon og feltverdi, så en blank linje og
deretter tekstlister som utgjør e-postens kropp.  Det er beskrevet i
e-postens hode hvordan tekstlinjene i kroppen skal tolkes.  Detaljene
er beskrevet i detalj i IETF RFC 5322.

Jeg savner dermed informasjon i forskriften hvordan Noark 5-løsninger
skal ta vare på e-post uten informasjonstap.  Det bør være mulig
gjenskape hele den originale e-posten slik den så ut ved mottak hvis
en skal kunne sjekke kryptosignaturer (for eksempel der S/MIME eller
OpenPGP er brukt).  Det vil også gjøre det mulig å sjekke hvor e-posten
kommer fra ved hjelp av felter brukt av Domain Keys Identified Message
(DKIM) i e-posten.  DKIM er definert i IETF RFC 6376.

Formatet for Internett-e-post er spesifisert i IETF RFC 5322, og
består i grove trekk av et sett med tekstlinjer som e-posthode, en
blank linje som skilletegn og så et sett med tekstlinjer som består av
e-postens kropp.  E-postens kropp kan være strukturert i underdeler i
tråd med MIME-formattering og inneholde for eksempel både ren tekst,
HTML-sider og vedlegg med formater uten en klar og offentlig
spesifikasjon (f.eks. proprietære binærformater).  E-posten kan også
henvise til eksterne filer (f.eks. bilder i HTML-e-post) som kun er
tilgjengelig i en tidsbegrenset periode.  Arkivering av e-post på
formatet beskrevet i IETF RFC 5322 bør antagelig derfor ha endel
begresninger når det gjelder aksepterte vedlegg, for å sikre at e-post
og tilhørende vedlegg kan forstås også i fremtiden, selv når det ufrie
programmet som kan tolke slike proprietære binærformater er gått tapt
eller lenger lar seg bruke (noe som kan skje hvis programmet for å
fungere er avhengig av nettjenester som ikke lenger eksisterer), eller
nettjenesten der eksternt henviste filer befant er borte.

En naturlig begresning for slik e-postarkiver er å kreve at
e-postvedlegg skal være et av de godkjente dokumentformatene omtalt i
forskriften.  Et spørsmål som må besvares i den forbindelse er hva som
skal gjøres med mottatt arkivverdig e-post som inneholder vedlegg på
formater som ikke er godkjent for arkivering.  En konvertering til
andre formater før arkivering vil ødelegge for kontroll av eventuelle
kryptosignaturer i e-posten.  Det grunnleggende spørsmålet er om
arkivet skal ta vare på informasjon det er uklart hvordan skal tolkes
eller ikke.  Det tryggeste er kanskje å både ta vare på
originalinformasjonen i tillegg til å kreve at det der mulig blir
lagret omformede utgaver der det er klart hvordan de skal tolkes.

En e-post inneholder referanser til hvilke e-post den er svar på i
e-posthodefeltene In-Reply-To og References.  Disse feltene inneholder
referanser til tidligere e-post ved hjelp av verdier hentet fra
e-posthodefeltet Message-ID.  For å automatisk kunne finne hvilke
e-post som "henger sammen" når nye e-post skal arkiveres er det
hensiktsmessig å raskt kunne søke opp e-post ved hjelp av e-postens
Message-ID.  Det gjør det enklere å finne aktuelle mapper å foreslå
for å plassere en ny e-post som skal arkiveres.  Det vil dermed være
hensiktsmessig å bestemme hvilket felt i Noark 5-strukturen dette skal
lagres inn for å sikre gjenfinning i deponerte arkiver.  En god
kandidat kan være feltet 'filnavn' fra Noark 5
Tjenestekatalog-spesifikasjonen side 104.

Klargjøre hvordan SMS/MMS skal arkiveres
----------------------------------------

Det står ingenting i forslaget til forskrift hvordan
øyeblikksmeldinger som SMS/MMS skal arkiveres.  Det er en utfordring
flere etater har i dag, og det er kanskje naturlig å gi instrukser
eller anbefalinger til forvaltningen om hvordan slike meldinger bør
langtidslagres. Kan det være en ide å bestemme et XML-basert format
for lagring av SMS?  Eller kanskje det er mer fornuftig å arkivere
originalmeldingen slik den ble oversendt til mobilen?  SMS-formatet er
beskrevet og vedlikeholdes av 3GPP som TS 23.041.  MMS-formatet er
beskrevet og vedlikeholdes av Open Mobile Alliance som OMA MMS. 
Kanskje XML-format i MMS-spesifikasjonen kan brukes?

Det bør kanskje nevnes hva slags informasjon som bør registreres for
hver SMS?  Tekst, sender, mottaker(e), sendetidspunkt,
mottakertidspunkt?

http://www.3gpp.org/DynaReport/23041.htm
http://www.openmobilealliance.org/
