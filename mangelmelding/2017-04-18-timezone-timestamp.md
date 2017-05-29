Klargjør datohåndteringen
=========================

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

I følge del 6.1.1.8 side 25 skal datoformatet angis i henhold til
http://www.w3.org/TR/NOTE-datetime, og dette notatet sier at alle
tidspunkt som inneholder tid på døgnet skal oppgis med numerisk
tidssone i tråd med ISO 8601, men med firesifret årstall.  Det skal
dermed være mulig å oppgi datetime-verdier ala dette: 1997, 1997-07,
1997-07-16, 1997-07-16T19:20+01:00, 1997-07-16T19:20:30+01:00 og
1997-07-16T19:20:30.45+01:00.  Men gir det mening å akseptere kun
årstall og årstall/måned i API-et?  Spesifikasjonen i
tjenestegrensesnittet er i strid med metadatakatalog.xsdl for Noark 5
versjon 4.0, som sier at dato-typen hentes fra
http://www.w3.org/2001/XMLSchema, der det henvises til
https://www.w3.org/TR/xmlschema11-2/#date som spesifiserer at dato
består av år, måned og dag med valgfri tidssoneinformasjon.

  
Vil det noen gang være nødvendig å oppgi et "generisk" fremtidig
tidspunkt i et NOARK 5-arkiv?  Kravet om numerisk tidssone vil være
problematisk hvis det skal oppgis tidspunkt i fremtiden,
f.eks. kl. 12:00 om to måneder, eller hver tirsdag kl. 13:00 det neste
året.  Årsaken er at sommertid gjør at tidssoneverdien endrer seg (for
Norge fra +01 til +02 og tilbake), og et slikt lokalt tidspunkt dermed
ikke kan representeres med numerisk tidssone uten mer informasjon.

FIXME Finn ut om dette er en problemstilling med NOARK 5, eller om det
aldri oppgis lokal tid i fremtiden.

FIXME forsøk å finne forskjellen mellom 'datetime' og 'date' som datatype i spec.

FIXME camelcase eller ikke?  merknadsdato, kassasjonsdato, graderingsdato, nedgraderingsdato men slettetDato og presedensDato, skjermingOpphoererDato

Ønsket endring
--------------

FIXME
