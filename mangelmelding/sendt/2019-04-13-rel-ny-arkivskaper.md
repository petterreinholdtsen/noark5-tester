Klargjør relasjonsnøkkelnavn for ny-arkivskaper
===============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.4 (Arkivskaper)
         Sidenummer  80
        Linjenummer  n/a
    Innsendingsdato  2019-04-13
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er avvik mellom spesifikasjonen og demonettstedet
http://n5test.kxml.no/ når det gjelder hva relasjonen for å lage ny
arkivskaper skal hete.  Jeg antok spesifikasjonen var korrekt og
spurte i https://github.com/Arkitektum/N5-net/issues/1 om
demonettstedet skulle endre relasjonsnavn , men fikk til svar fra Tor
Kjetil Nilsen at navnet
http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivskaper/ på side
80 (7.2.1.4 Arkivskaper) i spesifikasjonen muligens feil og at
'arkivstruktur' skulle vært 'administrasjon' slik det ser ut på
http://n5test.kxml.no/api/arkivstruktur.

Ønsket endring
--------------

Noen bør vurdere hva som er riktig her.  For meg virker det naturlig
og korrekt å bruke relasjonsnøkkel
`http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivskaper/` for
denne operasjonen, og det trengs dermed ingen endring i
spesifikasjonen, men derimot i demo-programmet som kjører på n5test,
men tar det opp her uansett i tilfelle det er feil.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/134 .
