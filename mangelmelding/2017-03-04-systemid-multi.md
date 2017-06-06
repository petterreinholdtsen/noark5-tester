Avklar når objekter skal ha SystemID (M001) og når det ikke er valgfritt
=====================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.3
         Sidenummer  75
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge 'Multipl.'-feltet for flere klasser, eksempelvis Arkivenhet
side 38 samt Arkiv og Arkivdel side 44 (muligens alle klasser, men jeg
har ikke sjekket samtlige), så er systemID et "[0..1]-felt", mens
merknaden til feltet sier systemID alltid skal eksistere.  Hvordan kan
begge deler stemme?  I hvilke tilfeller kan feltet SystemID i så fall
mangle for et objekt?  Er poenget at informasjonen som sendes inn ved
oppretting av nye objekter skal være uten SystemID-verdi, da den
settes ved opprettelsen?  I så fall er det vel mer korrekt å droppe
[0..1]-notasjonen og i stedet klargjøre at alle objekter skal ha slik
verdi etter opprettelsen, samt nevne i del 6.1.1.3 (Opprette objekter
(Create)) at systemID-attributten aldri skal være satt ved POST.

I følge blant annet punkt 7.2.1.1 (Arkiv) side 62 skal systemID være
utfylt etter registrering av arkiv.  Dette kan tolkes å være i strid
med attributtbeskrivelsene som bruker [0..1] i UML-dokumentasjonen og
verdien av Multipl. for arkivenhet på side 77.

Det virker mest rimelig på meg at intensjonen er at alle objekter skal
ha en systemID-attributt, og at bruken av [0..1] er feil i
spesifikasjonen.

Ønsket endring
--------------

Fjern [0..1] i alle forekomster i tekst og UML-diagram der [0..1] er
brukt som beskrivelse av SystemID for et opprettet prosjekt for å
gjøre det klart at feltet ikke er valgfritt.  Det gjelder side 29, 30,
31, 38, 44, 45, 46, 47, 48, 49, 50, 52, 54, 55, 77, 100, 126, 142,
157, 161, 197, 199, 201, 202, 203, 204, 224, 231, 247, 253, 254, 259,
263, 264 og 265.

Endre i del 6.1.1.3 (Opprette objekter (Create)), legg inn nytt
avsnitt foran 'Resultat' på side 17:

> Når en oppretter objekter med POST skal feltet systemID ikke være
> satt.  Det settes automatisk når objektet opprettes, og korrekt
> verdi returneres etter at objektet er opprettet i databasen.
