Klargjør forhold mellom tjenestegrensesnittet og standarden / katalogene
========================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

FIXME Få inn sidehenvisninger for eksemplene?

Det er noen uoverensstemmelser mellom tjenestegrensesnittet og Noark
5-standarden, metadatakatalogene og tilhørende XSD-filer.

FIXME er eksempellisten komplett?

Et eksempel er i del 7.2.1.7 (Dokumentobjekt) på side 104 i
tjenestegrensesnittspesifikasjonen, der det er et attributt som heter
mimeType.  Dette attributtet finnes ikke i metadatakatalogene eller i
Noark 5-standarden versjon 4.0.

Det kan virke som om feltene dokumentobjekt.format og
dokumentobjekt.mimeType representerer samme informasjon, men er det
samme verdi?  Et tjenestegresesnitt vil for eksempel returnere
følgende når en henter en dokumentObjekt:

```
{
  "format": "PDF",
  "formatDetaljer" : "PDF/A PDF 1.4"
  "mimeType" : "application/pdf"
}
```

Det er ikke klart hvorfor det trengs to felter for å angi format.  PDF
og application/pdf virker redundant her.  Mimeformater inkludert
filformater er definert av organisasjonen IANA og en oversikt er
tilgjengelig fra http://www.iana.org/assignments/media-types/.
Kanskje Noark 5-standarden burde forholde seg til denne katalogen i
stedet for å ha sin egen formatkatalog.  Det er definert hvordan en
kan lage sine egendefinerte MIME-typer, slik at en ikke er avhengig av
IANA hvis det behovet skulle melde seg.

Et annet eksempel med en lignende problemstilling gjelder filen
```arkivstruktur10.xsd``` som er tilgjengelig fra
http://skjema.kxml.no/arkivverket/noark5/v4.0/arkivstruktur10.xsd .

Vi tror 'arkivdel' attributtet som er definert under mappe egentlig er 
'referanseArkivdel'.

Vi finner ingen referanse for elementet &lt;Hendelseslogg&gt; definert
i Noark 5-standarden, metadatakatalogene eller XSD-filene.

Videre vil vi påpeke at metadatakatalogen bruker camelCase og elementet 
&lt;Hendelseslogg&gt; følger ikke den generelle Noark navngivingsmåten. 

En rask gjennomgang av arkivstruktur10.xsd viser at det meste av
navngiving er riktig.

Det er ikke opplagt hvorfor filen arkivstruktur10.xsd finnes når det
virker som om dette egentlig er bare en gjentagelse av filen
arkivstruktur.xsd som finnes på Riksarkivets hjemmesider.

Ønsket endring
--------------

FIXME har vi et forslag til endring i formuleringer?

Det gjøres et arbeid med å få tjenestegrensesnittet og standarden i
samsvar med hverandre.  Spesielt gjelder å få avklart mimeType og
format og om de egentlig er samme felt.

XSD-filene tilhørende tjenestegrensesnittet må kvalitetsikres.

Tjenestegrensesnitt gjenbruker den offisielle arkivstruktur.xsd

FIXME hva betyr de to siste sentningene?
