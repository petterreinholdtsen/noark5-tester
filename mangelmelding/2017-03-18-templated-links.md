Klargjør om alle \_links-oppføringer skal ha templated-feltet
=============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.2
         Sidenummer  13
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Side 13 omtaler feltet «*templated*» som kan brukes i _links-lister
for ressurser som støtter oData-filter.  Men det står ikke om feltet
er påkrevd for de ressursene som ikke støtter slike filter?  Kan
klienter forvente at feltet alltid er tilstede i korrekte
API-implementasjoner eller ikke?

Feltet er så vidt jeg kan se alltid satt for elementer i
\_links-lister i testinstansen tilgjengelig fra
http://n5test.kxml.no/api/ .  Men feltet eksisterer ikke i
eksempelresponsen vist frem på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ .  Der finnes
det derimot et felt som heter «*templatedSpecified*».  Mens hvis en
besøker http://rel.kxml.no/noark5/v4/api/arkivstruktur/ så eksisterer
både «*templated*» og «*templatedSpecified*».  Er sistnevnte en
skrivefeil for «*templated*»?  Jeg finner ikke «*templatedSpecified*»
omtalt i spesifikasjonen.

For å spare noen få bytes under overføring i protokollen foreslår jeg
at feltet «*templated*» er valgfritt og kun må eksistere når det
settes til «true», og kan antas å være «false» hvis det ikke
eksisterer.

Ønsket endring
--------------

Legg inn en setning på side 13 under 6.1.1.2 (Finne objekter (Read))
etter «De ressurser som støtter filter skal annonserer dette under
_links med «templated=true» og parametre som kan brukes til dette i
«href» » som lyder:

> Feltet «templated» er valgfritt og antas å være «false» hvis det
> ikke finnes.
