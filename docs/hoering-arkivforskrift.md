Høringsuttalelse om Riksarkivarens forskrift
============================================

Teksten vedlikeholdes på https://titanpad.com/noark5-forskrift

http://www.arkivrad.no/aktuelt/riksarkivarens-forskrift-pa-horing

Frist for innsending er 1. mai 2017

Riksarkivaren
Pb. 4013 Ullevål Stadion
0806 OSLO

Deres referanse 2016/9840 HELHJO.

Viser til høring sendt ut 2017-02-17, og tillater meg å sende inn noen
innspill om revisjon av Forskrift om utfyllende tekniske og
arkivfaglige bestemmelser om behandling av offentlige arkiver
(Riksarkivarens forskrift).

Av Petter Reinholdtsen

Klargjøring av godkjente dokumentformat
---------------------------------------

Kommentarer relatert til § 5-16 (Godkjente dokumentformater ved
innlevering), der punkt 1 lister opp godkjente dokumentformat ved
innlevering.

Punkt 1a nevner TXT uten nærmere beskrivelse og uten å henvise til §
5-11, og uten å forklare hvordan en skal vite hvilket tegnsett som
skal brukes for 'TXT'.  FIXME slå opp hvor text/plain er beskrevet?

Punkt 1a omtaler TIFF som "ren tekst".  Jeg antar en her snakker om
bilder av papir med tekst.  Men TIFF er bilde av tekst, ikke ren tekst
og det virker misvisende å likestille den med TXT, XMP og
PDF/A. Bilder av tekst, uavhengig av om det er pakket inn som TIFF
eller PDF, bør vel heller legges under punkt 1c.

Punkt 1f nevner "PCM-basert wave" uten å beskrive nærmere hva som
mener med dette.  Det bør refereres til en klar og offentlig
spesifikasjon, helst en fri og åpen standard, som beskriver formatet.

Punkt 1h) nevner HTML, men nevner ikke hvordan eksterne referanser i
HTML (f.eks skrifttyper, JavaScript-kode, bilder eller video skal
håndteres for å kunne gjenskape en web-side.  § 5-19 sier derimot at
formatet ikke skal brukes.  Kanskje HTML ikke burde være på listen
over godkjente dokumentformater?

Legge inn epost (IETF RFC 5322) som godkjent dokumentformat
-----------------------------------------------------------

Jeg savner informasjon i forskriften hvordan Noark 5-løsninger skal ta
vare på epost uten informasjonstap.  Det må være mulig gjenskape hele
den originale eposten slik den så ut ved mottak hvis en skal kunne
sjekke kryptosignaturer (for eksempel der S/MIME eller OpenPGP er
brukt).  Det vil også gjøre det mulig å sjekke hvor eposten kommer fra
ved hjelp av DMARC-felter i eposthodet (FIXME sjekk ref).

Formatet for Internett-epost er spesifisert i IETF RFC 5322, og består
i grove trekk av et sett med tekstlinjer som eposthode, en blank linje
som skilletegn og så et sett med tekstlinjer som består av epostens
kropp.  Epostens kropp kan være strukturert i underdeler i tråd med
MIME-formattering og inneholde for eksempel både ren tekst, HTML-sider
og vedlegg med formater uten en klar og offentlig spesifikasjon
(f.eks. proprietære binærformater).  Arkivering av epost på formatet
beskrevet i IETF RFC 5322 bør antagelig derfor ha endel begresninger
når det gjelder aksepterte vedlegg, for å sikre at epost og tilhørende
vedlegg kan forstås også i fremtiden, selv når det ufrie programmet
som kan tolke slike proprietære binærformater er gått tapt eller
lenger lar seg bruke (noe som kan skje hvis programmet for å fungere
er avhengig av nettjenester som ikke lenger eksisterer).

En naturlig begresning for slik epostarkiver er å kreve at
epostvedlegg skal være et av de godkjente dokumentformatene omtalt i
forskriften.  Et spørsmål som må besvares i den forbindelse er hva som
skal gjøres med mottatt arkivverdig epost som inneholder vedlegg på
formater som ikke er godkjent for arkivering.  En konvertering til
andre formater før arkivering vil ødelegge for kontroll av eventuelle
kryptosignaturer i eposten.  Det grunnleggende spørsmålet er om
arkivet skal ta vare på informasjon det er uklart hvordan skal tolkes
eller ikke.  Det tryggeste er kanskje å både ta vare på
originalinformasjonen i tillegg til å kreve at det der mulig blir
lagret omformede utgaver der det er klart hvordan de skal tolkes.

I beskrivelsen av Noark 5 sitt krav 8.1.8 (side 197) står det at epost
skal lagres i et enhetlig, samlet format som gjengir både e-posthode
og e-postmelding, men forklarer ikke hvordan det skal gjøres.

Klargjøre hvordan SMS/MMS skal arkiveres
----------------------------------------

Det står ingenting i forslaget til forskrift hvordan
øyeblikksmeldinger som SMS/MMS skal arkiveres.  Det er en utfordring
flere etater har i dag, og det er kanskje naturlig å gi instrukser
eller anbefalinger til forvaltningen om hvordan slike meldinger bør
langtidslagres. Kan det være en ide å bestemme et XML-basert format
for lagring av SMS?  Eller kanskje det er mer fornuftig å arkivere
originalmeldingen slik den ble oversendt til mobilen?  SMS-formatet er
beskrevet og vedlikeholdes av 3GPP som TS 23.041.  MMS-formatet er
beskrevet og vedlikeholdes av Open Mobile Alliance som OMA MMS.
Kanskje XML-format i MMS-spesifikasjonen kan brukes?

Det bør kanskje nevnes hva slags informasjon som bør registreres for
hver SMS?  Tekst, sender, mottaker(e), sendetidspunkt,
mottakertidspunkt?