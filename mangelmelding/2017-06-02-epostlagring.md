Korriger beskrivelse av epost og beskriv hvordan de bør arkiveres
=================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5
           Kategori  Versjon 3.1
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

FIXME sjekk om det samme gjelder versjon 4.

Se også docs/epostlagring.md

https://www.arkivverket.no/arkivverket/Offentleg-forvalting/Noark/Noark-5/Standarden

I NOARK 5 versjon 3.1 side 193 står følgende:

> "Selv om RFC2822 definerer syntaksen for e-posttransaksjoner, er den
> ingen standard som definerer dataformatet som skal bli brukt når
> e-posttransaksjonen er fanget som dokumenter."

Dette utsagnet gir ikke mening når en vet at E-post "fanges som
dokumenter" ved å lagre tekstinnholdet som utgjør e-posthode og
-kropp.  E-posthode og kropp er tekstlinjer definert i henhold til
RFC822 og etterfølgende IETF-standarder som RFC 2822 og 5322.  Et mye
brukt måte å gjøre dette på er å lagre en epost per fil slik den ble
sendt via SMTP-protokollen, slik
f.eks. [Maildir-](https://en.wikipedia.org/wiki/Maildir)-arkivering av
epost gjør.

FIXME

Denne delen av NOARK 5-spesifikasjonen bør endres til å forklare
hvordan epost kan lagres og arkiveres i sitt opprinnelige format.

Ønsket endring
--------------

FIXME formuler forslag til tekst basert på eget forslag om hvordan
lagre epost i Noark 5.
