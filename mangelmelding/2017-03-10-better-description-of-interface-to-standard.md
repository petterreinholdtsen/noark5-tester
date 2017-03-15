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

Beskrivelse
-----------
Vi ser det er noen uoverensstemmelser mellom tjenestegrensesnittet, standarden
 og metadatakatalogene.

Eksempelvis:
Dokumentdel 7.2.1.7 Dokumentobjekt i tjenestegrensesnittet har et attributt 
som heter mimeType. Dette attributtet finnes ikke i metadatakatalogene eller
 i standarden.

Er feltene dokumentobjekt.format og dokumentobjekt.mimeType det samme? I dag
ser jeg for meg at en kjerne vil ha følgende data i dokumentObjekt:

{
"format": "PDF",
"formatDetaljer" : "PDF/A PDF 1.4"
"mimeType" : "application/pdf"
}

Vi ser noe lignende i filen arkivstruktur10.xsd som finnes her:

 http://skjema.kxml.no/arkivverket/noark5/v4.0/arkivstruktur10.xsd

Vi tror 'arkivdel' attributtet som er definert under mappe egentlig er 
'referanseArkivdel'.

Vi finner ingen referanse for elementet <Hendelseslogg> definert i standarden, 
metadatakatalogene eller XSD-filene.

Videre vil vi påpeke at metadatakatalogen bruker camelCase og elementet 
<Hendelseslogg> følger ikke den generelle Noark navngivingsmåten. 

En rask gjennomgang av arkivstruktur10.xsd viser at det meste av navngiving er riktig.

Ønsket endring
--------------
Det gjøres et arbeid med å få tjenestegrensesnittet og standarden i samsvar
 med hverandre. Spesielt gjelder å få avklart mimeType og format og om de 
egentlig er samme felt.

XSD-filene tilhørende tjenestegrensesnittet må kvalitetsikres.


Respons
-------

Ingen respons fra arkivverket så langt.
