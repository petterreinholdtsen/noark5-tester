Avklar når det kreves SystemID
==============================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.3
         Sidenummer  75
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge 'Multipl.'-feltet for flere klasser, eksempelvis Arkivenhet
side 38 samt Arkiv og Arkivdel side 44 (muligens alle klasser, men jeg
har ikke sjekket samtlige), så er systemID et "[0...1]-felt", mens
merknaden til feltet sier systemID alltid skal eksistere.  Hvordan kan
begge deler stemme?  I hvilke tilfeller kan feltet SystemID i så fall
mangle for et objekt?

I følge punkt 7.2.1.1 (Arkiv) side 62 skal systemID være utfylt etter
registrering av arkiv.  Dette virker å være i strid med beskrivelsen i
UML-dokumentasjonen.

Tilsvarende gjelder for andre objektbeskrivelser.

Ønsket endring
--------------

Gjør det klart at alle unike dataenheter skal ha SystemID, og endre
UML-diagram fra 'systemID: SystemID [0..1]' til 'systemID: SystemID'.

Endre "Multipl." felt i tabell på side 77 fra '[0..1] til '[1].

Legg inn SystemID i atributtlisten under punkt 7.2.1.4 (Arkivskaper)
og andre objekter der det mangler.

FIXME lag komplett liste med forslag til endringer?
