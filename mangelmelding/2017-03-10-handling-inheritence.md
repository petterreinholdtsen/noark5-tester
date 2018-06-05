Savner konsekvent håndtering av arv i datamodellen
==================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Arv i datamodellen er synlig i følgende forhold:

 * mappe -> saksmappe
 * registrering -> basisregistrering -> journalpost
 * korrespondansepart -> korrespondansepartenhet|korrespondansepartperson|korrespondansepartintern

Disse arvforholdene håndteres ikke konsistent i spesifikasjonen.  Hvis
vi ser på forholdet mappe -> saksmappe, så ser vi at relasjonene som
returneres når en lager en ny arkivdel inkluderer

 * "href": "http://localhost:49708/api/arkivstruktur/Arkivdel/12345/ny-mappe"
 * "rel": "http://rel.kxml.no/noark5/v4/api/ny-mappe"

For å opprette en saksmappe må en bruke relasjonen
utvid-til-saksmappe:

 * "href": "http://n5test.kxml.no/api/sakarkiv/Saksmappe/12345/utvid-til-saksmappe"
 * "rel": "http://rel.kxml.no/noark5/v4/utvid-til-saksmappe"

FIXME spesifikasjonen nevner ikke 'utvid-til-saksmappe, den kommer fra http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/

Hvis vi ser på forholdet registrering -> basisregistrering, så ser vi
at under "arkivdel" kan du kun opprette en registrering:

 * "href": "http://localhost:49708/api/arkivstruktur/Arkivdel/12345/ny-registrering",
 * "rel": "http://rel.kxml.no/noark5/v4/api/ny-registrering",

mens under "mappe" kan en opprette både en "registrering" og en
"basisregistrering:"

 * "href": "http://n5test.kxml.no/api/arkivstruktur/Mappe/12345/ny-registrering"
 * "rel": "http://rel.kxml.no/noark5/v4/ny-registrering"

 * "uri": "http://n5test.kxml.no/api/arkivstruktur/Mappe/12345/ny-basisregistrering"
 * "rel": "http://rel.kxml.no/noark5/v4/ny-basisregistrering"

Det er dermed ikke konsistent beskrevet i spesifikasjonen hvordan arv
håndteres.

Videre vil det å opprette en mappe gjøre at mappen blir tilordnet en
arkivdel.  En arkivdel kan ha et klassifikasjonssystem tilknyttet seg,
og å tillate at mappen endrer "type" kan føre til feil som bryter med
gjeldende tenking i Noark, om at en arkivdel kun har ett
klassifikasjonssystem.

FIXME forklar nærmere hvordan feilen oppstår

Dette betyr at tilnærmingen med "utvid-til-saksmappe" kanskje ikke er
i tråd med hvordan Noark brukes i dag.

Ønsket endring
--------------

FIXME Konkret forslag til formuleringer?

Noen bør se nærmere på hvordan arv håndteres i spesifikasjonen.  Fra
ståstedet til oss som implementerer tjenestegrensesnittet er mitt
personlige syn at en bør droppe "utvid-til-"-strategien og tvinge
klienten til å gjøre et aktivt valg om hva den ønsker å oppprette og
opprette mappe, saksmappe, byggesaksmappe eller møtemappe.  Hvis
"utvid-til-"-strategien skal brukes så må det klargjøres i
spesifikasjonen hvordan dette skal håndteres når det gjelder
klassifikasjonssystem knyttet til arkivdel.
