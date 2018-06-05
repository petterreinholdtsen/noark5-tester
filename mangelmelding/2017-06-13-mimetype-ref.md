Klargjør hva attributtet mimeType kan inneholde
===============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  ?
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonens del 7.2.1.7 (Dokumentobjekt) side 104 har attributten
mimeType.  Dette er et metadatafelt som mangler i metadatakatalogen
for Noark 5 versjon 4.0.

Det virker rimelig å anta at dette feltet inneholder det samme som
HTTPs Content-type-hodefelt, slik det omtales i del 6.1.1.9 (Hente og
overføre filer) på side 25 og 26, men det kan med fordel nevnes
eksplisitt med [referanse til hodefeltet i HTTP-standarden / IETF RFC
2616](https://tools.ietf.org/html/rfc2616#page-124), definisjonen av
mediatyper i RFC
2616](https://tools.ietf.org/html/rfc2616#section-3.7) og [IANAs
register over offisielle
MIME-typer](https://www.iana.org/assignments/media-types/media-types.xhtml).

Det er uklart fra spesifikasjonen om feltet kun skal inneholde
mediatypen (dvs. type/undertype) eller om det også skal inneholde
parametre som tegnsett.  Parameter er svært nyttig for tekstformat,
der en kan oppgi hvilket tegnsett som er brukt.  Tilsvarende
informasjon kan muligens legges inn i metadatafeltene format (M701) og
formatDetaljer (M702), men det er ikke definert nærmere hva
formatDetaljer skal inneholde.  Derimot er det veldefinert i
HTTP-standarden hva parameteret betyr.  For eksempel vil formatet
RA-TEKST kunne ha en av følgende mimeType-verdier, som entydig
definerer hvilket tegnsett som er brukt i teksten:

 * text/plain; charset=UTF-8
 * text/plain; charset=ISO-8859-1

Det er naturligvis mange flere mulige mimeType-verdier som kan gjelde
for RA-TEKST.

Tilsvarende formatet RA-XML antagelig kunne representeres med mange
forskjellige mimeType-verdier, med og uten parameter:

 * application/xml; charset=UTF-8
 * image/svg+xml

Ønsket endring
--------------

FIXME bestem hva som bør endres.

inn i referanselisten?

inn i metadatakatalogen?

omtales i attributtlisten for dokumentobjekt?
