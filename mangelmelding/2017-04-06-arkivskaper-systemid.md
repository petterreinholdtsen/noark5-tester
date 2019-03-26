Mangler systemID i attributtlisten for arkivskaper?
===================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.4
         Sidenummer  81
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Etter listen med attributter i del 7.2.1.4 (Arkivskaper) på side 81
står det i restriksjoner på side 82 at "Etter registrering skal
systemID være utfylt".  Men I selve listen med attributter på side 81
og 82 så er ikke systemID nevnt.  Skulle systemID vært med i
attributtlisten?

FIXME Hvordan er forholdet mellom arkivskaper and arkiv?  kan
arkivskaper eksistere uten arkiv?

Ønsket endring
--------------

Legg inn følgende attributtbeskrivelse før arkivskaperID på side 81:

 Navn     | Merknad   | Multipl. |Kode | Type
 ---------+-----------+----------+-----+---------------------------
 systemID |           | [1..1]   |     | SystemID

FIXME vurder om forslaget er tilstrekkelig.
