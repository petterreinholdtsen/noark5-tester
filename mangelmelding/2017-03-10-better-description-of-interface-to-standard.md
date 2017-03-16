Klargjør forhold mellom tjenestegrensesnittet og standarden / katalogene
========================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra https://github.com/petterreinholdtsen/noark5-tester/ .

Beskrivelse
-----------
Vi ser det er noen uoverensstemmelser mellom tjenestegrensesnittet og Noark 5
standarden, metadatakatalogene og tilhørende XSD-filer.

Eksempelvis:
Dokumentdel 7.2.1.7 Dokumentobjekt i tjenestegrensesnittet har et attributt 
som heter mimeType. Dette attributtet finnes ikke i metadatakatalogene eller
 i standarden.

Er feltene dokumentobjekt.format og dokumentobjekt.mimeType det samme? En 
kjerne vil feks publisere følgende data når den henter en 
dokumentObjekt:

```
{
"format": "PDF",
"formatDetaljer" : "PDF/A PDF 1.4"
"mimeType" : "application/pdf"
}
```
Det er ikke klart hvorfor det trengs to felter for å angi format.
Filformater er definert av IANA (http://www.iana.org/assignments/media-types/)
og kanskje Noark standarden kan forholde seg til dette. Det er også
mulig å lage egendefinerte mimetypes.

Vi ser en lignende problemstilling i filen arkivstruktur10.xsd som finnes her:

 http://skjema.kxml.no/arkivverket/noark5/v4.0/arkivstruktur10.xsd

Vi tror 'arkivdel' attributtet som er definert under mappe egentlig er 
'referanseArkivdel'.

Vi finner ingen referanse for elementet &lt;Hendelseslogg&gt; definert i Noark 5 
standarden, metadatakatalogene eller XSD-filene.

Videre vil vi påpeke at metadatakatalogen bruker camelCase og elementet 
&lt;Hendelseslogg&gt; følger ikke den generelle Noark navngivingsmåten. 

En rask gjennomgang av arkivstruktur10.xsd viser at det meste av navngiving er 
riktig.

Det er heller ikke opplagt hvorfor filen arkivstruktur10.xsd finnes når det virker 
som om dette egentlig en bare gjentagelse av filen arkivstruktur.xsd som finnes på
Riksarkivets hjemmesider. 

Ønsket endring
--------------
Det gjøres et arbeid med å få tjenestegrensesnittet og standarden i samsvar
 med hverandre. Spesielt gjelder å få avklart mimeType og format og om de 
egentlig er samme felt.

XSD-filene tilhørende tjenestegrensesnittet må kvalitetsikres.

Tjenestegrensesnitt gjenbruker den offisielle arkivstruktur.xsd
